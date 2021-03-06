from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='itc.pptheme',
      version=version,
      description="Plone customization for plone site",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 4.3",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='web zope plone theme',
      author='Tom Gross',
      author_email='itconsense@gmail.com',
      url='https://github.com/tomgross/pp-site',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['itc'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.api',
          'z3c.jbot',
          'plone.app.theming',
          'matplotlib',
          'six',
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
