from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT = " -e ." # This is the string that is added to the end of the package name in the requirements file

def get_requirements(file_path:str)->List[str]:
    '''
    This function reads the requirements file and returns the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Dishita',
    author_email='dishitaaggarwal30@gmail.com',
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt')
)