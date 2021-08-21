from setuptools import setup,find_packages
import os
import sys


with open('requirements.txt') as f:
    # Separate by lines ('\r','\r\n', \n'), 
    # and return a list containing each line as an element,
    required = f.read().splitlines()


reqs = []
for element in required:
    reqs +=[element]
    


if sys.platform == 'win32' or sys.platform == 'cygwin' or sys.platform == 'msys':
   # on windows
   compile_command = 'f2py -c space_filling_decomp_new.f90 -m space_filling_decomp_new --compiler=mingw32'
elif sys.platform == 'linux' or sys.platform == 'linux2':
   # on linux
   compile_command = 'python3 -m numpy.f2py -c space_filling_decomp_new.f90 -m space_filling_decomp_new'


setup(
    name = 'acse-9-independent-research-project-fy120',
    version ='1.0',
    description = 'A comparison of dimensionality reduction methods '
                 +' for fluid flow problems focusing on hierarchical autoencoders',
    author='Fan Yang',
    author_email='fan.yang20@imperial.ac.uk',
    install_requires=reqs,
    test_suite='tests',




)