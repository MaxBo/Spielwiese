# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 20:33:08 2016

@author: MaxBohnet
"""

from setuptools import setup, find_packages
from cythoninstallhelpers.get_version import get_version


package_name = 'sphinx_creation_example'
version = get_version(package_name, __file__)
ext_modnames = []


setup(
    name=package_name,
    version=version,
    description="project to test sphinx documentation creation",

    packages=find_packages('src', exclude=['ez_setup']),
    #namespace_packages=['wiver'],

    package_dir={'': 'src'},
    package_data={'': ['*.pxd']},
    include_package_data=True,
    zip_safe=False,
    data_files=[
        ],

    extras_require=dict(
        extra=[],
        docs=[
            'z3c.recipe.sphinxdoc',
            'sphinxcontrib-requirements'
        ],
        test=[]
    ),

)
