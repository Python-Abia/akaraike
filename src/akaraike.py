from random import randint
import sys


class PasswordGenerator:

    # string of upper characters
    upper_characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # string of lower characters
    lower_characters = 'abcdefghijklmnopqrstuvwxyz'

    # string of numbers
    numbers = '0123456789'

    #string of special characters
    specials = '@-_+=%^&*#!'

    # charset
    charset = None

    #charset length - the length of the password string to generate
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
        try:
            self.charset_length = int(length)
        except ValueError:
            sys.exit("Enter a whole number")


    def set_charset_types(self, type):
        
        try:

            #convert charset types into a list
            type_list = list(type)

            #placeholder for concatenated charset string
            charset = ""

            #an internal function to  ensure that the user does not enter wrong values
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
        for item in type_list:
            if item != 'lowers' and item != 'uppers' and item != 'numbers' and item != 'specials':
                sys.exit("Unrecognized charset type \'" + item + "\'")

