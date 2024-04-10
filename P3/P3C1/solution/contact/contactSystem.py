from abc import ABC, abstractmethod

class ContactSystem(ABC):
    # ContactSystem is abstract (inherits from Abstract Base Class)
    # A ContactSystem can be used to send a message to a user using a certain method.

    def __init__(self):
        pass

    # All subclasses of ContactSystem have to implement a way of sending the message.
    @abstractmethod
    def send(self, message):
        pass