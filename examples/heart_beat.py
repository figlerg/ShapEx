from shapex.shapex.ShapEx import *
import os

# this is just to get the path to the current working directory.
#  In a normal usecase you would instead just need the path to the specification file
cwd = os.getcwd()

path = os.path.join(cwd, 'heart_beat_debug.se')

# initialize object
shapex_object = ShapEx(timestep=0.0001,
                       word_sampler=WordSamplerMode.BOLTZMANN, target_word_length=6, init_point=InitPoint.PSO,
                       dir_sampling=DirectionSampling.RDHR, shrinking=Shrinking.SHRINKING,
                       noise_dist='uniform', noise=0)


# loads the spec
shapex_object.add_shape_expression(path)

# sample
samples = shapex_object.samples(1000)

print(samples)

plotter(samples)