# Name = Kuldeep Thiara
# Class = CS3100

from abc import abstractmethod
from abc import ABC, abstractmethod
from LLDictAbstract import LLDictAbstract

#Implementing a dictionary using a linked list
class HTDictAbstract(LLDictAbstract):


    # Function to add model(key) and its value(quantity)
    @abstractmethod
    def push2(self, key, value, value2):
        pass

    # add model for index search
    @abstractmethod
    def pushForIndex(self,model):
        pass

    # list of models
    @abstractmethod
    def listOfModels(self):
        pass

    # Searches for index of the passes model name
    @abstractmethod
    def searchIndex(self, key):
        pass
