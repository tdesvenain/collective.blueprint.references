from setuptools import setup, find_packages
import os

version = '0.2.dev0'

long_description = (
    open('README.txt').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.txt').read()
    + '\n' +
    open('CHANGES.txt').read()
    + '\n')

setup(name='collective.blueprint.references',
      version=version,
      description="A blueprint to set relations between Plone documents",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='plone transmogrifier blueprint relations references',
      author='',
      author_email='',
      url='git@github.com:tdesvenain/collective.blueprint.references.git',
      license='gpl',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['collective', 'collective.blueprint'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'collective.transmogrifier',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
