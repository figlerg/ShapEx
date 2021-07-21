# ShapEx

## Introduction
ShapEx is a tool   that generates  random  behaviors  from  shape  expressions,  a  formal specification formalism for describing sophisticated temporal behaviors of CPS. 
The tool samples a random behavior in two steps:

   (1) it first explores the space of qualitative parameterized shapes and then 

   (2) instantiates parameters by sampling a possibly non-linear constraint.

It uses several sampling algorithms for the different stages of sample generation and generates timed traces according to a textual shape expression file.

## Installation
ShapEx is written in Python 3 and uses our standalone library *anyHR*. 
It is necessary to have a working installation of 
[pip](https://pip.pypa.io/en/stable/installing/) and [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)  for the following installation process.

Open the target directory in a terminal, and type `git clone https://github.com/figlerg/anyHR && cd anyHR`.

Then type
`pip install -r requirements.txt`.

The anyHR library should be installed now and we will repeat the same process for the ShapEx tool:

`cd .. && git clone https://github.com/figlerg/ShapEx && cd ShapEx`

`pip install -r requirements.txt`

Finally, add the anyHR directory to the PYTHONPATH and ShapEx is ready to be used.

## Use
The following block illustrates a minimum working example for the use of the ShapEx tool. 
For all parameters the default values are used and 100 samples are generated for the SE from the imported text file 'pulse.se'.
```
from shapex.shapex.ShapEx import *

# initialize ShapEx object
se = ShapEx()
# loads the specification
se.add_shape_expression('pulse.se')
# Generate 100 examples 
samples = shapex_object.samples(100)
```

The following table gives an overview of the parameters that can be set at ShapEx object initialization (line 4 of the code above):

| Parameter          | Description                                                                                            | Values                                                       |
|--------------------|--------------------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| timestep           | Difference between two consecutive timestamps.                                                         | positive float (default 1.0)                                 |
| word_sampler       | Qualitative word sampler.                                                                              | WordSamplerMode.SEARCH (default),  WordSamplerMode.BOLTZMANN |
| search_budget      | Maximum number of distinctive qualitative words. Applicable to WordSamplerMode.SEARCH only.            | positive integer (default 10)                                |
| mean_word_length   | Mean length of qualitative word. Applicable to WordSamplerMode.BOLTZMANN only.                          | positive float (default 10.0)                                |
| dir_sampling       | Direction sampling hit-and-run algorithm. Random (RDHR) vs. coordinate direction (CDHR)                | DirectionSampling.RDHR (default), DirectionSampling.CDHR     |
| shrinking          | Direction sampling hit-and-run algorithm.                                                              | Shrinking.NO_SHINKING (default), Shrinking.SHRINKING         |
| init_point         | Hit-and-run with or without shrinking                                                                  | InitPoint.PSO (default), InitPoint.SMT                       |
| noise_distribution | Finding initial point for hit-and-run. Particle swarm optimization (PSO) vs. constraint solving (SMT). | 'uniform' (default), 'gaussian'                              |
| noise              | Distribution use to add noise to the generated signals.                                                | positive float (default 0.0)                                 |








		
		

		
		
