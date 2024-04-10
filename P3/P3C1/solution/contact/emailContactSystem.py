from contact.contactSystem import ContactSystem
from utils.validators import validate_email
from utils.senders import send_email

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