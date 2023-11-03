from setuptools import setup, find_packages

setup(
    name='ctg-fetch',
    version='0.1.0',
    author='Akshay Chougule',
    author_email='akshay6023@gmail.com',
    description='A package that can fetch you get adverse events associated with a specific clinical trial from clinicaltrials.gov',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
