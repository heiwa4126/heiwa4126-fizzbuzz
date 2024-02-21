from setuptools import setup, find_packages

setup(
    name='heiwa4126-fizzbuzz',
    version='0.1',
    packages=find_packages(),
    author='heiwa4126',
    author_email='heiwa4126@gmail.com',
    description='A simple fizzbuzz generator',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/heiwa4126/heiwa4126-fizzbuzz',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
