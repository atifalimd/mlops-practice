from setuptools import setup, find_packages #it will automatically find all the packages available in src\__init__
setup(

    name="src", 
    version="0.0.1", 
    description="wine quality package", 
    author='atifalimd',
    packages=find_packages(),
    license= "MIT",

) 
