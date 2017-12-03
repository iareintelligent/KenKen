__author__="Topher"
__date__ ="$Dec 7, 2009 2:36:33 PM$"

from setuptools import setup,find_packages

setup (
  name = 'KenKen (CS112 - Project 2)',
  version = '0.1',
  packages = find_packages(),

  # Declare your packages' dependencies here, for eg:
  install_requires=['foo>=3'],

  # Fill in these to make your Egg ready for upload to
  # PyPI
  author = 'Topher',
  author_email = '',

  summary = 'Just another Python package for the cheese shop',
  url = '',
  license = '',
  long_description= 'Long description of the package',

  # could also include long_description, download_url, classifiers, etc.

  
)