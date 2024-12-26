from abc import ABC, abstractmethod

class SubscriberRepFileStrategy(ABC):
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, data):
        pass


    @abstractmethod
    def display(self):
        pass
