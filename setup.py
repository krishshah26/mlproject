from setuptools import find_packages,setup
"""from setuptools: This part of the line tells Python to import specific functions from 
the setuptools library. setuptools is a library that provides utilities for packaging, distributing, and installing Python projects.
find_packages: This function is used to automatically discover and list all Python packages within a project. It searches through the 
project directory for any folders containing an __init__.py file (which indicates that the folder is a Python package) and returns a list of package names.
setup: This function is used to configure the metadata and behavior of the Python package. 
It takes various arguments to specify details such as the package name, version, description, author, dependencies, and other 
information needed for packaging and distribution.
"""
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
name='mlproject',
version='0.0.1',
author='Krish',
author_email='krishnaik06@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)