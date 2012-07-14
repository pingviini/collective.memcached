from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='collective.memcached',
      version=version,
      description="Memcached utility for Plone",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Plone",
        "Framework :: Plone :: 4.1",
        "Framework :: Plone :: 4.2",
        ],
      keywords='memcached utility plone',
      author='Jukka Ojaniemi',
      author_email='jukka.ojaniemi@gmail.com',
      url='http://github.com/pingviini/collective.memcached',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Products.CMFPlone',
      ],
      extras_require={
          'test': 'plone.app.testing',
          'pylibmc': 'pylibmc',
          'python-memcached': 'python-memcached'},
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target=plone
      """,
      )
