import argparse
import datetime
import os
import random
import textwrap
from typing import Dict

import sys
from antlr4 import *
from parse.expression2aut.visitor.se_to_sa_visitor import SEToSAVisitor

from generation_tool.generate_traces import *
from misc.save import save_to_csv
from misc.visualize import plotter
from parse.SyntaxError import HardSyntaxErrorStrategy
from parse.generated.ShapeExpressionLexer import ShapeExpressionLexer
from parse.generated.ShapeExpressionParser import ShapeExpressionParser
from word_sampler.sapathfinder.find_paths import find_paths

# parsing cmd input:
p = argparse.ArgumentParser(description='Shape _expression parser')

p.add_argument('--inputfile', '-i', nargs=1, required=True, help='shape _expression input file')
p.add_argument('--timestep', '-ts', nargs='?', type=float, default=1.0,
               help="optionally sets the signal sampling time step. if not specified, timestep=1. (default) is used")
p.add_argument('--valuation_mode', '-m', nargs=1, required=True, type=str, default='sampling',
               help='Mode for choosing parameter valuations. Choose between iteration, sampling')
p.add_argument('--continuity_constraints', '-cc', nargs=1, required=False, type=str, default='no_constraints',
               help='Mode for imposing constraints to enforce some kind of continuity. Options: no_constraints ('
                    'default), hardcoded, filter')
p.add_argument('--filter_tolerance', '-ft', nargs=1, type=float, required=False, default=1.,
               help='Tolerance for filter modes (defines how harsh the constraints are). Default is 1.')
# TODO maybe discard iteration mode (coverage?)
p.add_argument('--density', '-ds', nargs='?', type=int, default=0,
               help="Necessary for iteration mode. Sets the number of samples to be taken for each variable parameter "
                    "of the atomic shapes from its values range.")
p.add_argument('--threshold', '-th', nargs=1, required=True, help='acceptable noise threshold')
p.add_argument('--number', '-n', nargs=1, required=True, help='upper bound for number of samples')
p.add_argument('--paths', nargs=1, type=int, required=True,
               help='upper bound for number of paths through shape automaton')
p.add_argument('--noise_dist', required=False, nargs=1,
               help="optionally sets the noise distribution. 'normal' (default) or 'uniform' are possible")
p.add_argument('--out', '-o', nargs=1, required=False, help='directory where the generated samples will be stored')
p.add_argument('--seed', dest='seed', required=False, help='Integer seed for reproducibility.', type=int, default=12345)

p.add_argument('--visualize', '-v', dest='visualize', required=False, action='store_true',
               help='Displays traces (or a sample of 1000 traces if there are more than that).')
p.set_defaults(visualize=False)

p.add_argument('--save_csv', '-s', dest='save_csv', required=False, action='store_true',
               help='Saves the traces and their respective settings (valuations etc.) to csv files in current '
                    'directory.')
p.set_defaults(save_csv=False)

args = p.parse_args()

input_stream = FileStream(args.inputfile[0])
paths_upper_bound = int(args.paths[0])
valuation_mode = args.valuation_mode[0]
traces_upper_bound = int(args.number[0])

if args.out:
    dir_string: str = args.out[0]
else:
    dir_string = ''

timestep = args.timestep
density = args.density
threshold = float(args.threshold[0])
continuity_constraints = args.continuity_constraints[0]
visualize = args.visualize
save_csv = args.save_csv
seed = args.seed

handle_nonlin_constr = continuity_constraints == 'filter'
# TODO this is temporary, create an actual UI for filtering?
# TODO actually, think about whether we want to keep the simple filter mode (specifically the bits at end of instantiate)
#  This will depend on whether we find a much better version with thao and co

# process specification
lexer = ShapeExpressionLexer(input_stream)
stream = CommonTokenStream(lexer)
parser = ShapeExpressionParser(stream)
parser._errHandler = HardSyntaxErrorStrategy()
ctx = parser.shape_expression()

# translate to automaton
visitor = SEToSAVisitor()
aut_container, letter_duration_map = visitor.visitShape_expression(ctx)
aut_container: ShapeAutomatonContainer

# this is a table: (letter -> DurationInterval(discrete))
letter_duration_map: Dict[str, IntervalObject]

# this is a table parameter -> parameter interval(can be both discrete and real)
aut_container.intervals: Dict[str, IntervalObject]

# detect relational input (that is not a string! This check is only necessary for volesti interface relations)
# detected_relations = [rel for rel in aut_container.relations if not isinstance(rel, str)] != []
detected_relations = [rel for rel in aut_container.relations] != []

# detect non-integer intervals
detected_non_int_duration = False
for interval in letter_duration_map.values():
    if interval.timestep:
        detected_non_int_duration = True

if detected_non_int_duration and timestep == 1.0:
    print("WARNING: Detected non-integer discrete parameter interval. A timestep other than 1.0 should be given via "
          "the '--timestep' parameter.")

if save_csv:
    assert dir_string, "In saving mode, output directory parameter '--out/-o' has to be specified."
else:
    if dir_string:
        print("WARNING: '--out/-o' has been set, but saving mode has not been toggled by '--save_csv/-s'. "
              "The output directory will only be used for history files.")

# TODO xor checks for incompatible modes/inputs?

# TODO decide which to keep
assert continuity_constraints in ['hardcoded', 'no_constraints', 'filter'], \
    "--continuity_constraints/-cc has to be set either to 'hardcoded', 'no_constraints' or 'filter'."

assert valuation_mode == 'sampling' or valuation_mode == 'iteration', \
    "--valuation_mode/-m has to be set either to 'sampling' or 'iteration'"

# TODO this should probably be an enumerator
if valuation_mode == 'sampling' and detected_relations:
    if density:
        print(
            '\nInterval sampling mode is enabled. The density parameter has no effect here.')
    interval_sampling_mode = False
    relational_sampling_mode = True
    iteration_mode = False

elif valuation_mode == 'sampling':
    if density:
        print(
            '\n Interval sampling mode is enabled. The density parameter has no effect here.')

    # strictly speaking, this does not need to happen (since interval constraints are a subset of relations)
    interval_sampling_mode = True
    relational_sampling_mode = False
    iteration_mode = False

elif valuation_mode == 'iteration':
    assert density, 'When in iteration mode, a density parameter is required!'
    assert not detected_relations, 'Detected relations. Iteration mode only makes sense in sampling mode!'
    # 0 is default, so if no input for density is given this will throw
    interval_sampling_mode = False
    relational_sampling_mode = False
    iteration_mode = True

else:
    assert False, "Something went wrong."
    # raise  # TODO define parsing error object
    pass

if args.dist:
    distribution_type = args.dist[0]
    assert distribution_type in ['normal', 'uniform'], \
        "Only distributions 'normal' and 'uniform' are supported."
else:
    distribution_type = 'normal'
    # default for now

# get everything ready for generator:
params = aut_container.shape_param
aut = aut_container.automaton

paths = find_paths(aut, paths_upper_bound)
nr_of_paths = len(paths)

if traces_upper_bound < nr_of_paths:
    raise InputError('illegal input',
                     'upper bound for traces should be greater than upper bound for paths')

if valuation_mode == 'sampling':
    combinations_per_path = traces_upper_bound / nr_of_paths
    # heuristic for the number of traces in iteration mode
    noise_density = 1  # TODO decide whether this should remain constant or be an input. (reminder: this decides how well spread the noise levels should be)
    n = int(combinations_per_path // noise_density)  # for arbitrary noise_densities it should probably look like this

if iteration_mode:
    combinations_per_path = traces_upper_bound / nr_of_paths
    # heuristic for the number of traces in iteration mode

    # compute number of parameters which are variable:
    var_params_count = len(
        [param for param in params if (aut_container.intervals[param].start != aut_container.intervals[param].end)])
    print(
        "\n> Number of variable parameters detected in the shape specification: {0}\n> density = {1} => {2} different noise-free shapes ({1}^{0})".format(
            var_params_count, density, density ** var_params_count))

    # compute the number of different noise values to be sampled from [0,threshold] for the force_positive examples, which is the same number
    # of values to be sampled from [threshold,3*threshold] for the negative examples (this is why we have /2.):
    noise_density = int((combinations_per_path / (density ** var_params_count)) / 2.)

    if noise_density == 0:
        print(
            "\nWARNING: These inputs led to a noise density of 0. It will be set to 1 but you should reconsider the inputs of combinations per path,"
            "density and the number of variable parameters")
        noise_density = 1

    if combinations_per_path <= density ** var_params_count:
        # raise InputError('\nSpecified number of examples to be generated too low: {}. Alone for generating the noise-free shapes are required {} examples ({}*{}^{})!\n'.format(traces_upper_bound,nr_of_paths*density**var_params_count,nr_of_paths,density,var_params_count))
        # raise Exception('\nSpecified number of examples to be generated too low: {}. Alone for generating the noise-free shapes are required {} examples ({}*{}^{})!\n'.format(traces_upper_bound,nr_of_paths*density**var_params_count,nr_of_paths,density,var_params_count))
        pass
    elif noise_density < 11:
        print(
            '\nWARNING: Noise resolution rather low: only {} values! Your model will probably overfit, you might want to increase the specified number of examples to be generated.\n'.format(
                noise_density))
    elif noise_density > 1000:
        print(
            '\nWARNING: Noise resolution pretty high: {} values! Your model might overfit due to very similar examples in the dataset, you might want to decrease the specified number of examples to be generated.\n'.format(
                noise_density))

    # for sampling parameters
    n = traces_upper_bound // nr_of_paths

traces_positive = paths2traces(paths, density, noise_density, aut_container, seed, dist_mode=distribution_type,
                               timestep=timestep, threshold=threshold, positive_example=True,
                               continuity_constraints=continuity_constraints,
                               param_sampling=interval_sampling_mode, n=n, relational_input=relational_sampling_mode,
                               non_integer_durations=detected_non_int_duration,
                               handle_nonlin_constr=handle_nonlin_constr)
print('Positive samples generated.')
if threshold == 0:
    print('\nINFO: threshold = {} => no negative examples are going to be generated.'.format(threshold))
else:
    seed_negative = seed + 1
    # the above should not be necessary since the same noise can not lead to both force_positive and negative examples,
    # but i feel safer setting a different seed for each call of paths2traces

    traces_negative = paths2traces(paths, density, noise_density, aut_container, seed,
                                   dist_mode=distribution_type,
                                   timestep=timestep, threshold=threshold, positive_example=False,
                                   continuity_constraints=continuity_constraints,
                                   param_sampling=interval_sampling_mode, n=n,
                                   relational_input=relational_sampling_mode,
                                   non_integer_durations=detected_non_int_duration,
                                   handle_nonlin_constr=handle_nonlin_constr)
    print('Negative samples generated.')

if save_csv:
    save_to_csv(traces_positive, True, dir_string=dir_string)
    print('Saved samples to csv files.')
    if threshold > 0:
        save_to_csv(traces_negative, False, dir_string=dir_string)

# cristi's visualization: https://service.ait.ac.at/SAS/projects/cpql/repository/entry/tools/Shape_Expression_Visualization.ipynb

if visualize:
    if threshold == 0:
        to_be_visualized = traces_positive
    else:
        to_be_visualized = traces_negative + traces_positive  # rewrite this if one needs noisy positives
        print('Per default, the results will be visualized. '
              '\nIf threshold is 0, exact traces are shown. '
              '\nIf threshold is nonzero, both force_positive and negative traces are shown.')

    if len(to_be_visualized) >= 1000:
        random.seed(seed + 2)  # unnecessary for generation, but now visualizations will always look the same
        some_traces = random.sample(to_be_visualized, 1000)
        print(
            'Matplotlib is slow when plotting many traces... A sample of 1000 traces has been selected from all that were generated.')

    else:
        some_traces = to_be_visualized

    # TODO enable some comparison functionality like in main_emsoft20.
    fig = plotter(some_traces)

    print('Displaying plot... {} traces shown.'.format(len(some_traces)))

if not (save_csv or visualize):
    print('WARNING: Samples were created successfully, but no further action has been issued by cmd input.\n'
          "You might want to try '-s' for saving or '-v' for visualizing the traces. ")

# this block is just for experimenting and saves all visualisations and settings to a folder with time stamp:
# I want to have a text file with:
# full cmd input,
# a copy of spec.felix file,
# seed
# + all pictures that have been visualized!
time = str(datetime.datetime.now())
timestamp = time.replace(':', '_')[0:-7]  # for file name

hist_dir_name = os.path.join(dir_string, 'History')
os.makedirs(hist_dir_name, exist_ok=True)

txt_file_path = os.path.join(hist_dir_name, timestamp + ".txt")

cmd_raw = " ".join(sys.argv)
wrapper = textwrap.TextWrapper(break_long_words=False)
cmd_wrapped = "\nSame, but nicer looking: \n" + "\n".join(wrapper.wrap(" ".join(sys.argv)))
seed_line = "Seed = " + str(seed)
spec = str(input_stream)

text_file = open(file=txt_file_path, mode="w")

text_file.write(cmd_raw + "\n" + cmd_wrapped + "\n\n" + seed_line + "\n\nSpecification = \n" + spec)
text_file.close()

if visualize:
    fig_path = os.path.join(hist_dir_name, timestamp + ".jpg")
fig.savefig(fig_path)

if continuity_constraints == 'filter':
    print(str(len(traces_positive)) + " out of " + str(n) + " traces got through continuity filter.")
