# Appify
Appify is a python package aimed at making simple cli and UI by simply providing an entry function

## Status
[![Build Status](https://travis-ci.org/sylvaus/appify.svg?branch=master)](https://travis-ci.org/sylvaus/appify)

* Common part is implemented and tested 
* Clifier is implemented but not tested 
* Uilifier is not implemented

## Example
```python
from appify.cli.cli import Clifier

def print_main(name):
    """
    :param name: name to print
    :type name: str
    """
    print(name)
    
clifier = Clifier(print_main)
clifier.run()   
```