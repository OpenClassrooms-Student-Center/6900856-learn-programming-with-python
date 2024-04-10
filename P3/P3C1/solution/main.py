from contact.user import User
from contact.textContactSystem import TextContactSystem
from contact.emailContactSystem import EmailContactSystem
from utils.senders import mass_mail

if __name__ == '__main__':
	# Our main program.
	alice = User("Alice", TextContactSystem("01234 567890"))
	bob = User("Bob", EmailContactSystem("bob@bob.com"))

	user_list = [alice, bob]
	mass_mail("Hello {name}, how are you?", user_list)
	mass_mail("Hi {name}. Is your contact information still correct? Our records indicate that your {contact_info}.", user_list)