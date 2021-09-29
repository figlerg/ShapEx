from shapex.shapex.ShapEx import *
from shapex.misc.visualize import plotter

# initialize ShapEx object
se = ShapEx(dir_sampling=DirectionSampling.CDHR, init_point=InitPoint.SMT,timestep=0.01)
# loads the specification
se.add_shape_expression('pulse.sx')
# Generate 100 examples
samples = se.samples(100)

plotter(samples)