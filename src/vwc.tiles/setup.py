from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='vwc.tiles',
      version=version,
      description="Package providing tiles compatible with plone.app.tiles",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='Vorwaerts Werbung GbR',
      author_email='hallo@vorwaerts-werbung.de',
      url='http://dist.vorwaerts-werbung.de',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['vwc'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'five.grok',
          'lxml',
          'plone.app.dexterity',
          'plone.app.blocks',
          'plone.app.textfield',
          'plone.app.tiles',
          'plone.tiles',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
