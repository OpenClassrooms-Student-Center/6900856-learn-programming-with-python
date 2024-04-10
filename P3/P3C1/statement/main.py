## Learn Programming With Python - OpenClassrooms Course
# Part Three, Chapter One, Exercise.
# Version 0.1

# Split the program into modules and packages, adding __init__.py files and import statements where needed.
# Make sure that the program itself can be run by running a main.py in the project’s root directory.

from abc import ABC, abstractmethod

class User:
    def __init__(self, name, contact_method):
        self.name = name
        self.contact_method = contact_method

    def send(self, message):
        # This send method just passes the message onto its contact_method to send.
        self.contact_method.send(message)

class ContactSystem(ABC):
    # ContactSystem is abstract (inherits from Abstract Base Class)
    # A ContactSystem can be used to send a message to a user using a certain method.

    def __init__(self):
        pass

    # All subclasses of ContactSystem have to implement a way of sending the message.
    @abstractmethod
    def send(self, message):
        pass

class TextContactSystem(ContactSystem):
    # A TextContactSystem sends a message to the user using a text.

    def __init__(self, phone_number):
        validate_phone(phone_number)
        self.phone_number = phone_number
        super().__init__()

    def send(self, message):
        send_text_message(self.phone_number, message)

    def __str__(self):
        return "Phone Number is {}".format(self.phone_number)

class EmailContactSystem(ContactSystem):
    # An EmailContactSystem sends a message to the user using an email.

    def __init__(self, email_address):
        validate_email(email_address)
        self.email_address = email_address
        super().__init__()

    def send(self, message):
        send_email(self.email_address, message)

    def __str__(self):
        return "Email Address is {}".format(self.email_address)

def validate_email(email_address):
    # Parameters: email_address (string)
    # Validates the email address. Returns True if it's valid, False otherwise.

    # Right now, we can just assume the email address is fine.
    return True

def validate_phone(phone_number):
    # Parameters: phone_number (string)
    # Validates the phone number. Returns True if it's valid, False otherwise.

    # Right now, we can just assume the phone number is fine.
    return True

def send_text_message(number, message):
    # Parameters: number (string), message (string)
    # Sends a text containing message to number

    # In a real system, this would call some external library or service.
    print("Sending text message \"{}\" to phone number {}".format(message, number))

def send_email(email_address, message):
    # Parameters: email_address (string), message (string)
    # Sends an email containing message to email_address

    # In a real system, this would call some external library or service.
    print("Sending email \"{}\" to email address {}".format(message, email_address))

def mass_mail(message, user_list):
    # Parameters: message (string), user_list (List[User])
    # This function sends message to each user in user_list.

    for user in user_list:
        # mail_merge is a Dictionary that contains information about each user.
        mail_merge = {"name" : user.name, "contact_info" : user.contact_method}

        # We've used format before, but this is a little different.
        # The ** before mail_merge let's us "unpack" a dictionary.
        customised_message = message.format(**mail_merge)
        user.send(customised_message)

# Our main program.
alice = User("Alice", TextContactSystem("01234 567890"))
bob = User("Bob", EmailContactSystem("bob@bob.com"))

user_list = [alice, bob]
mass_mail("Hello {name}, how are you?", user_list)
mass_mail("Hi {name}. Is your contact information still correct? Our records indicate that your {contact_info}.", user_list)

