class User:
    def __init__(self, name, contact_method):
        self.name = name
        self.contact_method = contact_method

    def send(self, message):
        # This send method just passes the message onto its contact_method to send.
        self.contact_method.send(message)