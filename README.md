# Password Generator
A password generator module made by the awesome folks at Python Abia

This is a simple Open-Source Python library that helps you generate passwords quickly and neatly. 
It can be integrated into any form of application where there is the need to generate passwords or Secret keys

### Features
- Set length for key
- Choose types of characters or mixture of characters to use

## Usage

``` Python
from akaraike import PasswordGenerator

#Create an object of the PAsswordGenerator class
pg = PasswordGenerator()

#set length of characters
pg.set_charset_length(length = 5)

'''
Set types of characters as a list

Acceptable values are

- lowers for lowercase alphabets
- uppers for UPPERCASE alphabets
- numbers for 0123456789
- specials for @$;:,._

'''
pg.set_charset_types(type= ['numbers', 'specials'])

#print the password generator
print(pg.generate_password())

```

# Contributing to Akaraike

To install akaraike, along with the tools you need to develop and run tests, run the following in your virtualenv:

```bash
$ pip install -e .[dev]

```