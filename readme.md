# ShapEx

## Introduction
ShapEx is a tool   that generates  random  behaviors  from  shape  expressions,  a  formal specification formalism for describing sophisticated temporal behaviors of CPS. 
The tool samples a random behavior in two steps:

   (1) it first explores the space of qualitative parameterized shapes and then 

   (2) instantiates parameters by sampling a possibly non-linear constraint.

It uses several sampling algorithms for the different stages of sample generation and generates timed traces according to a textual shape expression file.

## Installation
ShapEx is written in Python 3 and uses our standalone library *anyHR*. 
It is necessary to have a working installation of Python 3,
[pip](https://pip.pypa.io/en/stable/installing/) and [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)  for the following installation process.

To install the tool, open a terminal and type 
`pip install ShapEx`.

This also installs *anyHR* and all other dependencies. The below example should now work right away.

## Use
The following block illustrates a minimum working example for the use of the ShapEx tool to generate a set of "pulse" traces. 
100 samples are generated for the SE from the imported text file 'pulse.sx'.
```python
from shapex.shapex.ShapEx import *
from shapex.misc.visualize import plotter

# initialize ShapEx object
se = ShapEx(dir_sampling=DirectionSampling.CDHR, init_point=InitPoint.SMT,timestep=0.01)
# loads the specification
se.add_shape_expression('pulse.sx')
# Generate 100 examples
samples = se.samples(100)

plotter(samples)
```

For this, prepare the specification file 'pulse.sx' in the same directory as the above script: 
The pulse is a concatenation of line segments with certain parameter ranges, 
with additional constraints to make the segments more continuous.
```python
# regular expression
line(a1,b1,d1).line(a2,b2,d2).line(a3,b3,d3).line(a4,b4,d4).line(a5,b5,d5)

:

# parameter declarations with ranges
param a1 in (0,0);
param b1 in (0,0.1);
duration d1 in (1,2);

param a2 in (0,-1);
param b2 in (-0.1,0.1);
duration d2 in (1,2);

param a3 in (0,0);
param b3 in (0,-2);
duration d3 in (1,2);

param a4 in (0,1);
param b4 in (-2,-0.5);
duration d4 in (1,2);

param a5 in (0,0);
param b5 in (-1,1);
duration d5 in (1,2);

# relational constraints
b1+a1*d1-b2 in (-0.01,0.01);
b2+a2*d2-b3 in (-0.01,0.01);
b3+a3*d3-b4 in (-0.01,0.01);
b4+a4*d4-b5 in (-0.01,0.01);
b5+a5*d5-b1 in (-0.01,0.01);
```

Both files can be found in the shapex/examples directory of this repository.

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








		
		

		
		
