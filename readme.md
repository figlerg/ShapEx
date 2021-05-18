README for trace generating tool (shape expressions)



UPDATED THE INSTALLATION PROCESS 01/2021 !
for a very simple working install, one must:
- install miniconda
- "conda install numpy sympy scipy pandas networkx tqdm matplotlib pyswarms pandas  -y"
- "conda install -c conda-forge antlr-python-runtime -y"


TYPICAL USECASES (newest version 06/2020):
1) Sampling mode with visualization:
This creates 100 traces of the spec given in --inputfile with uniformly sampled parameters.
A maximum of 10 paths are chosen (beginning with the shortest) and for each a portion of traces with similar size is
generated until there are 100 traces.
The sampling frequency is 0.1, the noise threshold is 0.001, offsets are taken into account.
The results are visualized, but not saved to csv files.

python main.py --inputfile <path>\example_spec\emsoft20\pulses_emsoft20.felix -n 100 --valuation_mode sampling --paths 10
--threshold 0.001 --timestep 0.1 --enable_offsets --visualize

2) Iteration mode with csv saving
python main.py --inputfile <path>\example_spec\emsoft20\pulses_emsoft20.felix -n 100 --valuation_mode iteration --paths 10 --threshold 0.001 --timestep 0.1 --enable_offsets --save_csv





PARAMETERS (new first):
--valuation_mode/-m [string 'sampling' or 'iteration]'
    This distinguishes between relational sampling and iterating over parameter space
    For sampling, both relational constraints (like 'a+2b <=3;') and interval constraints (like 'param a in [1,2]') are supported.

--visualize/-v
    invokes a plotting function for the generated traces

--save_csv/-s
    saves all the traces to csv files in specified "out" directory.

--continuity_constraints/-cc
	Mode for imposing constraints to enforce some kind of continuity. Options: no_constraints (default), hardcoded, filter

--inputfile/-i  [path string]
    specification file

--out/-o [path string]
    path to directory where csv-files are stored. This is mandatory only in saving mode.
    (e.g. when calling the tool with parameter '-s' in cmd)

--timestep/-ts  [double/int]
    signal sampling time step

--density/-ds [double/int]
    defines how many equidistant points are evaluated for each parameter interval IN INTERVAL MODE
    (has no effect in sampling mode, will simply print a warning)

--threshold/-th [double/int]
    acceptable noise threshold

--number/-n [int]
    upper bound for number of samples

--dist ['normal' or 'uniform'] NEEDS TO BE CHECKED
    optionally sets the noise distribution









		
		

		
		
