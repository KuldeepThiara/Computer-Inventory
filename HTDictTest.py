# Name = Kuldeep Thiara
# Class = CS3100

#Import the required libraries
from Computer import Computer
from ComputerInventoryHTDict import ComputerInventoryHTDict
from HTDict import HTDict

# Test class to test computer and ComputerInventory class
class Test:

    def __init__(self):
        pass

    # function to test the computer class
    def test_Computer(self):

        # Setting dummy value for model, quantity, and date
        computer = Computer()
        computer.set_model("T15")
        computer.set_quantity(15)
        computer.set_date("01/01/2000")

        # Testing those dummy value that are set above
        assert computer.get_model() == "T15"
        assert computer.get_quantity() == 15
        assert computer.get_date() == "01/01/2000"

        print("Everything passed for Computer Class")

    # Function to test ComputerInventory class
    def test_Computer_Inventory(self):


        cInventory = ComputerInventoryHTDict()

        #Reading the Inventory.csv file according to keyType
        cInventory.read_inventory("Inventory.csv", "Model")

        # The model name to check
        model = "T15"

        # searching for the given model
        computer = cInventory.search_model(model)

        # Testing if the data mataches
        assert computer == ('T15', 26)

        comInventory = ComputerInventoryHTDict()

        #Reading the Inventory.csv file according to keyType
        comInventory.read_inventory("Inventory.csv", "Index")

        # Searching for the index of model
        computer = comInventory.search_Index("T15")

        # Testing if the data mataches
        assert computer == 10

        # If everything passes this statement will be printed.
        print("Everything passed for Computer Inventory Class")


# main function
def main():
    test = Test()
    test.test_Computer()
    test.test_Computer_Inventory()


if __name__ == '__main__':
    main()
