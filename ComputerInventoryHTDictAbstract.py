# Name = Kuldeep Thiara
# Class = CS3100

#Import the required libraries
from abc import abstractmethod
from abc import ABC, abstractmethod

class ComputerInventoryHTDictAbstract(ABC):

    @abstractmethod
    def search_model(self, model):    # Given the model name, returns a quantity object that has a matching model number.
        pass

    # Given the date, returns a list of model that has a matching date.
    @abstractmethod
    def search_Date(self, key):
        pass

    # Given a model name, returns a index of that model
    @abstractmethod
    def search_Index(self, key):
        pass

    # Returns a list of models
    @abstractmethod
    def listOfModels(self):
        pass

    @abstractmethod
    # This function reads the all the models of computer and then stores it in LLDictionary
    def read_inventory(self, Inventory):
        pass

    @abstractmethod
    # Function to update and add models to csv
    def write_inventory(self, ComputerInventory_file, Model, newQuantity, keyType):
        pass
