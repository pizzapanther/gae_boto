import os

from setuptools import setup, find_packages

MY_DIR = os.path.normpath(os.path.dirname(__file__))

setup(
  name = "gae_boto",
  version = '13.10',
  description = "A recreation of Amazon Boto library that is is compatible with Google App Engine and easier to use.",
  url = "https://github.com/pizzapanther/gae_boto",
  author = "Paul Bailey",
  author_email = "paul.m.bailey@gmail.com",
  license = "BSD",
  packages = ['gae_boto', 'gae_boto.apis'],
  package_dir = {'gae_boto': MY_DIR},
  install_requires = [
    "requests>=2.0.0"
  ]
)
