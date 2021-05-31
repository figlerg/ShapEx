from setuptools import find_packages, setup

setup(
    name='ShapEx',
    version='2021.5',
    description='Library for sampling shape expressions.',
    url='https://github.com/figlerg/ShapEx.git',
    license='BSD',
    author='Felix Gigler, Dejan Nickovic, Mateis Cristinel, Nicolas Basset, Thao Dang',
    author_email='felix.gigler.fl@ait.ac.at',
    python_requires='>=3.5',
    install_requires=['tqdl', 'matplotlib'
    ],
    packages=find_packages(),

    classifiers=[
        'License :: OSI Approved :: BSD License',
	    'Programming Language :: Python :: 3.5',
	    'Programming Language :: Python :: 3.6',
	    'Programming Language :: Python :: 3.7',
    ],
)
