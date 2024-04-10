from contact.contactSystem import ContactSystem
from utils.validators import validate_phone
from utils.senders import send_text_message


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