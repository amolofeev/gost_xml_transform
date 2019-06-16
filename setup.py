from setuptools import setup, find_packages

setup(
    name='GOST XML Transformation',
    description='Implementation of GOST XML transformation for SMEV 3',
    version='1.0',
    author='Alexander Molofeev',
    author_email='alexandr.nino@gmail.com',
    python_requires='>=3.6.0',
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'lxml',
    ]
)
