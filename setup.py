from setuptools import setup

setup(
    name='ShapEx',
    version='2021.5',
    packages=['parse', 'parse.generated', 'shapex', 'alphabet', 'automaton', 'expression', 'word_sampler',
              'word_sampler.visitors', 'word_sampler.sapathfinder', 'generation_tool'],
    url='https://github.com/figlerg/ShapEx.git',
    license='Berkeley Source Distribution',
    author='Felix Gigler, Dejan Nickovic, Mateis Cristinel',
    author_email='felix.gigler.fl@ait.ac.at',
    description='Shape expression sampler for generating example traces'
)
