import sys
from setuptools import setup, find_packages

sys.path[0:0] = ['Semantic-Engine']
#from version import __version__

setup(
  name = 'Semantic-Engine',
  packages = find_packages(),
  #version = __version__,
  license='MIT',
  description = 'IT is a SEMANTIC SEARCH ENGINE ',
  author = 'Shauray Singh',
  author_email = 'shauraysingh08@gmail.com',
  url = 'https://github.com/shauray8/semantic-engine',
  keywords = ['deep learning',"speech","natural language processing", 'machine learning'],
  install_requires=[
      'numpy',
      'tqdm',
      'torch',
      'torchvision',
      "tensorboard".
  ],
)
