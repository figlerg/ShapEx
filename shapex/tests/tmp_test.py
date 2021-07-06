from shapex.misc.Error import IllegalParameterError
from shapex.misc.visualize import plotter
from shapex.shapex.ShapEx import ShapEx
from anyHR.hit_and_run.hit_and_run import DirectionSampling, Shrinking, InitPoint
from shapex.expression.Expression import WordSamplerMode


input_file = r"C:\Users\giglerf\Documents\dev\dev_code\ShapEx\shapex\tests\003.sx"

mode = (1,WordSamplerMode.BOLTZMANN,0,0,DirectionSampling.RDHR,Shrinking.NO_SHRINKING,InitPoint.PSO,'uniform',0)

try:
    shapex = ShapEx(*mode)
    shapex.add_shape_expression(input_file)

    samples = shapex.samples(10)
    print(samples)

except IllegalParameterError:
    # these are handled already and can be assumed to be user errors
    pass

plotter(samples)