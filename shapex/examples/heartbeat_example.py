from shapex.shapex.ShapEx import *
import os

# this is just to get the path to the current working directory.
#  In a normal usecase you would instead just need the path to the specification file
cwd = os.getcwd()

path = os.path.join(cwd, 'specs','heart_pulse.sx')

# initialize object
shapex_object = ShapEx(timestep = 0.001,
                       word_sampler=WordSamplerMode.BOLTZMANN,target_word_length=15,
                       dir_sampling= DirectionSampling.RDHR, shrinking = Shrinking.NO_SHRINKING,
                       noise_dist='uniform', noise=0.1)

# loads the spec
shapex_object.add_shape_expression(path)

# sample
samples = shapex_object.samples(100)

plotter(samples)