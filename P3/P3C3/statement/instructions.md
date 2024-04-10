# Instructions

Given the following User class and its constructor, create two custom exceptions with a shared parent class. They should indicate a username that’s too short or an insufficient password.

Once you have your custom exceptions, modify the constructor below to check that usernames are at least three characters long and that passwords contain at least one letter and one digit. Raise the appropriate exception when there’s a problem.

Then, try creating a user with different usernames and passwords to test that it works.

```
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
```

