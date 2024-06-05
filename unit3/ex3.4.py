import re
import string


class UsernameContainsIllegalCharacter(Exception):
    """
    a class for raising exceptions when trying to entar a username with illegal characters
    """
    def __init__(self, username, char, index):
        self._username = username
        self._char = char
        self._index = index
        super().__init__()

    def __str__(self):
        return f'The username contains an illegal character "{self._char}" at index {self._index} '
    
class UsernameTooShort(Exception):
    """
    class for raising exceptions when trying to entar a username that is too short
    """
    def __init__(self, username):
        self._username = username
        super().__init__()

    def __str__(self):
        return 'The username is too short'
    
class UsernameTooLong(Exception):
    """
    class for raising exceptions when trying to entar a that is too long
    """
    def __init__(self, username):
        self._username = username
        super().__init__()
    
    def __str__(self):
        
        return 'The username is too long'
    
class PasswordMissingCharacter(Exception):
    """
    a class for raising exceptions when trying to entar a password that is missing 
    a required character to make a strong password
    """
    def __init__(self, password, missing_char):
        self._password =  password
        self._missing_char = missing_char
        super().__init__()
    
    def __str__(self):
        return f'The password is missing a character ({self._missing_char})'
    
class PasswordTooShort(Exception):
    """
    class for raising exceptions when trying to entar a password that is too short
    """
    def __init__(self, password):
        self._password =  password
        super().__init__()
    
    def __str__(self):
        return 'The password is too short'

class PasswordTooLong(Exception):
    """
    class for raising exceptions when trying to entar a password that is too long
    """
    def __init__(self, password):
        self._password =  password
        super().__init__()

    def __str__(self):
        return 'The password is too long'

# funtion that gets a username and password as variables and prints 
    # OK if the username and password are valid
    # otherwise it raises an error message
def check_input(username, password):
    try:
        #check for errors in the lengths of the variables
        if(len(username)>16):
           raise UsernameTooLong(username)
        elif (len(username)<3):
           raise UsernameTooShort(username) 
        elif(len(password)<8):
           raise PasswordTooShort(password)
        elif(len(password)>40):
           raise PasswordTooLong(password)
        
        # check to see if all characters are alphanumeric characters or an underscore
        regex = re.compile(r'[a-zA-Z0-9_]')
        for i, char in enumerate(username):
            if not regex.match(char):
              raise UsernameContainsIllegalCharacter(username,char, i)

        # Check if password containg all the required characters
        if not any(c.islower() for c in password):
            raise PasswordMissingCharacter(password, "Lowercase")
        elif not any(c.isupper() for c in password):
            raise PasswordMissingCharacter(password, "Uppercase")
        elif not any(c.isdigit() for c in password):
            raise PasswordMissingCharacter(password, "Digit")
        elif not any(c in r'!"#$%&\'()*+,-./:;<=>?@[\\\]^_`{|}~' for c in password):
            raise PasswordMissingCharacter(password, "Special")
        
        
        print("OK")
    except Exception as e:
        print(e)

def main():
    check_input("1", "2")
    check_input("0123456789ABCDEFG", "2")
    check_input("A_a1.", "12345678")
    check_input("A_1", "2")
    check_input("A_1", "ThisIsAQuiteLongPasswordAndHonestlyUnnecessary")
    check_input("A_1", "abcdefghijklmnop")
    check_input("A_1", "ABCDEFGHIJLKMNOP")
    check_input("A_1", "ABCDEFGhijklmnop")
    check_input("A_1", "4BCD3F6h1jk1mn0p")
    check_input("A_1", "4BCD3F6.1jk1mn0p")

if __name__ == "__main__":
    main()