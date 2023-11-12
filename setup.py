from setuptools import setup, find_packages

setup(
    name='py-scalapb',
    version='1.0.0',
    author='Sam Reghenzi',
    description='A Python package to easily communicate with services that are using scalapb (https://scalapb.github.io/) for protobuf serialization',
    packages=find_packages(),
    install_requires=[
       "protobuf-4.25.0"
    ],
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)
