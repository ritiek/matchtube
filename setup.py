#!/usr/bin/env python

from setuptools import setup, find_packages
import matchtube

with open("README.rst", "r") as f:
    long_description = f.read()

setup(name='matchtube',
      version=matchtube.__version__,
      description='Match video titles on YouTube',
      long_description=long_description,
      author='Ritiek Malhotra',
      author_email='ritiekmalhotra123@gmail.com',
      packages = find_packages(),
      entry_points={
            'console_scripts': [
                  'matchtube = matchtube.matchtube:command_line',
            ]
      },
      url='https://www.github.com/ritiek/matchtube',
      keywords=['matchtube', 'YouTube', 'command-line', 'python', 'match'],
      license='MIT',
      download_url='https://github.com/ritiek/scribd-downloader/archive/v' + matchtube.__version__ + '.tar.gz',
      classifiers=[],
      install_requires=[
            'pafy'
      ]
)
