from random import randint
import sys


class PasswordGenerator:

    # String of upper characters
    upper_characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # String of lower characters
    lower_characters = 'abcdefghijklmnopqrstuvwxyz'

    # String of numbers
    numbers = '0123456789'

    # String of special characters
    specials = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

    # Charset
    charset = None

    # Charset length - the length of the password string to generate
    charset_length = 0


    def generate_password(self):
        """
        Performs the computation that genarates a
        password

        """

        password = ""
        while True:
            for x in range(self.charset_length):
                x = randint(0, (self.charset.__len__() - 1))
                password += self.charset[x]
            return password


    def set_charset_length(self, length):
        """
        Defines the lenght of the Password
        """
        try:
            self.charset_length = int(length)
        except ValueError:
            sys.exit("Enter a whole number")


    def set_charset_types(self, type):
        """ Sets the type of character set to be used by password geenrator"""
        try:
            # Convert charset types into a list
            type_list = list(type)

            # Placeholder for concatenated charset string
            charset = ""

            # Internal function to ensure that the user enters the right values
            self.clean_list(type_list)

            if len(type_list) > 4:
                sys.exit("Too many charset types specified")

            if 'lowers' in type_list:
                charset += self.lower_characters
            if 'uppers' in type_list:
                charset += self.upper_characters
            if 'numbers' in type_list:
                charset += self.numbers
            if 'specials' in type_list:
                charset += self.specials

            self.charset = charset

        except ValueError:
            sys.exit("Charset types should be a list of values")


    def clean_list(self, type_list):
        """
        A function to  ensure that the user enter the right values
        """
        for item in type_list:
            if item != 'lowers' and item != 'uppers' and item != 'numbers' and item != 'specials':
                sys.exit("Unrecognized charset type \'" + item + "\'")
