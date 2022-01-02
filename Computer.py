# Name = Kuldeep Thiara
# Class = CS3100


class Computer: # Computer class to hold info about a single computer

    def __init__(self): # constructor
        self.__model = ""       # Computer Model
        self.__quantity = 0     # Quantity of the specific model
        self.__date = ""        # Date of stored data

    # Model getter method
    def get_model(self):
        return self.__model

    # Model Setter method
    def set_model(self, model):
        self.__model = model

    # Quantity getter method
    def get_quantity(self):
        return self.__quantity

    # Quantity setter method
    def set_quantity(self, quantity):
        self.__quantity = quantity

    # Date getter method
    def get_date(self):
        return self.__date

    # Date setter method
    def set_date(self, date):
        self.__date = date

    # adding a magic method to be able to print the computer information
    def __str__(self):
        #line =  "Model: " + self.__model + " Quantity: " + str(self.__quantity) + " Date: " + self.__date
        line =  " " + self.__model + " " + str(self.__quantity) + " " + self.__date
        return line
