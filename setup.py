#!/usr/bin/env python
# -*- coding: latin1 -*-

import distribute_setup
distribute_setup.use_setuptools()

from setuptools import setup

try:
    from distutils.command.build_py import build_py_2to3 as build_py
except ImportError:
    # 2.x
    from distutils.command.build_py import build_py

setup(name="exafmm",
      version="2011.1",
      description="Fast summation in Python",
      long_description="""
      Code-generating FMM etc.
      """,
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Other Audience',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Scientific/Engineering :: Visualization',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
        ],

      author="Rio Yokota, Andreas Kloeckner, Matthew Knepley",
      author_email="yokota@bu.edu",
      license = "MIT",
      packages=["exafmm"],

      # 2to3 invocation
      cmdclass={'build_py': build_py})