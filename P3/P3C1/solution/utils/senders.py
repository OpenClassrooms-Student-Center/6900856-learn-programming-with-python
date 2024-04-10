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