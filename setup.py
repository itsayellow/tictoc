# setup for tictoc package

import os.path
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

setup(
        name='tictoc',
        version='0.2',
        description='Handy timer object.',
        author='Matthew Clapp',
        author_email='itsayellow+dev@gmail.com',
        license='MIT',
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3'
            'Programming Language :: Python :: 2'
            ],
        keywords='timing',
        py_modules=['tictoc'],
        #python_requires='>=3',
        )
