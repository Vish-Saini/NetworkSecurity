'''
The setup.py file is an essential part of packaging and 
distributing Python projects. It is used by setuptools 
(or distutils in older Python versions) to define the configuration 
of your project, such as its metadata, dependencies, and more
'''

from setuptools import setup, find_packages
from typing import List

def get_requirements()->List[str]:
    """
    This function returns a list of requirements
    """
    requirements_list: List[str] = []
    try:
        with open('requirements.txt','r') as file:
            #read lines from the file
            lines = file.readlines()
            #process each line
            for line in lines:
                requirement = line.strip()
                #ignore empty lines and -e .
                if requirement and requirement != '-e .':
                    requirements_list.append(requirement)
    except FileNotFoundError:
        pass
    return requirements_list


setup(
    Name = "Network Security Project",
    version = "0.0.1",
    author = "Vishal",
    author_email = "vishalsaini48189@gmail.com",
    description = "A project for network security analysis and monitoring",
    packages = find_packages(),
    install_requires = get_requirements(),
)

print(get_requirements())