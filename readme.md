# Appify
Appify is a python package aimed at making simple cli and UI by simply providing an entry function

## Status
[![Build Status](https://travis-ci.org/sylvaus/appify.svg?branch=master)](https://travis-ci.org/sylvaus/appify)
[![codecov](https://codecov.io/gh/sylvaus/appify/branch/master/graph/badge.svg)](https://codecov.io/gh/sylvaus/appify)

* Common part is implemented and tested 
* Clifier is implemented but not tested 
* Guilifier is implemented but not tested 

## Example
```python
from appify.cli import Clifier

def print_main(name):
    """
    :param name: name to print
    :type name: str
    """
    print(name)
    
clifier = Clifier(print_main)
clifier.run()   
```