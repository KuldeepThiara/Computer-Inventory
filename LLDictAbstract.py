# Name = Kuldeep Thiara
# Class = CS3100


from abc import abstractmethod
from abc import ABC, abstractmethod


# Implementing a dictionary using a linked list
class LLDictAbstract(ABC):

    # Adds items to the dictionary
    @abstractmethod
    def push(self, key, value):
        pass

    # Searches the dictionary and returns if the the key exists
    @abstractmethod
    def search(self, key):
        pass

    # Searches the dictionary and returns key and value
    @abstractmethod
    def search2(self, key):
        pass
