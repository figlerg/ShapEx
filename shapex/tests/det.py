from shapex.expression.Expression import WordSamplerMode
from shapex.misc.visualize import plotter
from shapex.shapex.ShapEx import ShapEx

filename = r"/shapex/tests/specifications/det.sx"

shapex = ShapEx(noise=0, word_sampler=WordSamplerMode.BOLTZMANN, target_word_length=20)

shapex.add_shape_expression(filename)

plotter(shapex.samples(10))