# Name = Kuldeep Thiara
# Class = CS3100

# Import the required libraries
from Computer import Computer
from ComputerInventoryHTDictAbstract import ComputerInventoryHTDictAbstract
from HTDict import HTDict
import csv
from datetime import date

# Holds information for all computers in inventory
# Inherititng from the base class


class ComputerInventoryHTDict(ComputerInventoryHTDictAbstract):

    def __init__(self):
        self.__computer_dict = HTDict()  # Dictionay class

    # Given the model name, returns a quantity object that has a matching model number.
    def search_model(self, key):

        return self.__computer_dict.search(key)

    # Given the date, returns a list of model that has a matching date.
    def search_Date(self, key):

        return self.__computer_dict.search2(key)

    # Given a model name, returns a index of that model
    def search_Index(self, key):

        return self.__computer_dict.searchIndex(key)

    # Returns a list of models
    def listOfModels(self):

        return self.__computer_dict.listOfModels()

    # This function reads the all the models of computer and then stores it in LLDictionary
    def read_inventory(self, ComputerInventory_file, keyType):
        # Open the file for reading
        # Loop through each line of the file
        # For each row, create a computer object and add it to the list of computer
        #modeIsKey = self.__computer_dict.push(computer.get_model(),computer.get_quantity())

        with open(ComputerInventory_file, newline='') as csv_file:
            reader = csv.reader(csv_file)
            next(reader, None)  # Skip the header.
            # Unpack the row directly in the head of the for loop.
            for Model, Quantity, Date in reader:

                computer = Computer()
                # Reads the first column and set it to model
                computer.set_model(Model)
                # Reads the second column and set it to quantity
                computer.set_quantity(int(Quantity))
                # Reads the last column and set it to date
                computer.set_date(Date)
                # Now append model as key and quanity as value.

                if keyType == "Model":
                    self.__computer_dict.push(
                        computer.get_model(), computer.get_quantity())
                elif keyType == "Date":
                    self.__computer_dict.push2(computer.get_date(), computer)
                elif keyType == "Index":
                    self.__computer_dict.pushForIndex(computer.get_model())

    # Function to update and add models to csv

    def write_inventory(self, ComputerInventory_file, Model, newQuantity, keyType):
        # Open the file for reading
        # Loop through each line of the file
        # Adds each row to the tempList
        with open(ComputerInventory_file, 'r', newline='') as csv_fileReader:
            reader = csv.reader(csv_fileReader)

            # Temporary list to store date from reader
            tempList = list(reader)

            # Function to update quantity
            if keyType == "Update":

                # Index for the model that needs to be updated
                index = self.__computer_dict.searchIndex(Model)

                # New quantoty
                quantity = newQuantity

                index += 1
                # Current Date
                currentDate = date.today()

                # Date format dd/mm/YY
                formatedDate = currentDate.strftime("%m/%d/%y")

                # Updating the quantity
                tempList[index][1] = quantity
                # Updating the date
                tempList[index][2] = formatedDate

            if keyType == "Add":

                # Quantity is passed on as 0
                quantity = newQuantity

                # Gets the today's date
                currentDate = date.today()

                # Date format dd/mm/YY
                formatedDate = currentDate.strftime("%m/%d/%y")

                # Model is added to a list
                # Which will be added to a temporary list
                addList = []
                addList.append(Model)
                addList.append(quantity)
                addList.append(formatedDate)

                # Model is added to temp list to be writen in csv file
                tempList.append(addList)

            csv_fileReader.close()

        with open(ComputerInventory_file, 'w', newline='') as csv_fileWriter:
            writer = csv.writer(csv_fileWriter)

            # Overwrites the templist to csv file.
            writer.writerows(tempList)
            csv_fileWriter.close()
