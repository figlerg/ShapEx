from setuptools import find_packages, setup

with open("readme.md", "r") as fh:
    long_description = fh.read()

setup(
    name='ShapEx',
    version='1.0.1',
    description='Library for sampling shape expressions.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/figlerg/ShapEx.git',
    license='BSD',
    author='Felix Gigler, Dejan Nickovic, Mateis Cristinel, Nicolas Basset, Thao Dang',
    author_email='felix.gigler.fl@ait.ac.at',
    python_requires='>=3.5',
    install_requires=['tqdm', 'matplotlib','numpy', 'z3-solver', 'antlr4-python3-runtime','anyHR',
    ],
    packages=find_packages(),

    classifiers=[
        'License :: OSI Approved :: BSD License',
	    'Programming Language :: Python :: 3',
        "Operating System :: OS Independent",
    ],
)
