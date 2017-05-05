'''
Created on 30 Sep 2016

@author: jdrumgoole
'''
from setuptools import setup
import os

pyfiles = [ f for f in os.listdir( "." ) if f.endswith( ".py" ) ]

    
setup(
    name = "mongodb_utils",
    version = "0.9.2",
    
    author = "Joe Drumgoole",
    author_email = "joe@joedrumgoole.com",
    description = "MongoDB Utils - A package of utilities for use with MongoDB",
    long_description = '''
A simple class for initiating MongoDB connections and an aggregation convenience
class agg.py that helps in building aggregation pipelines".
''',
    license = "AGPL",
    keywords = "MongoDB API Aggregation",
    url = "https://github.com/jdrumgoole/mongodb_utils",
    
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',


        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: GNU Affero General Public License v3',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2.7' ],
   
    install_requires = [ "pymongo", "nose" ],
       
    packages = [ "mongodb_utils"],
    


    test_suite='nose.collector',
    tests_require=['nose'],
)
