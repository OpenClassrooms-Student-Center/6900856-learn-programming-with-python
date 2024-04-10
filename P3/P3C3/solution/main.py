class InvalidUsernameException(Exception):
    pass

class InvalidPasswordException(Exception):
    pass

def validate_username(username):
    return len(username) > 5

def validate_password(password):
    return len(password) > 12
        

class User:
    def __init__(self, username, password):
        if (not validate_username(username)):
            raise InvalidUsernameException(f"Invalid username : {username}, Too short")
        if (not validate_password(password)):
            raise InvalidPasswordException(f"Invalid password : {password}, Not insufficient")

        self.username = username
        self.password = password

if __name__ == '__main__':
    user1 = User("user", "Password12345") # Comment this line to check the next exception.
    user2 = User("username", "Password")