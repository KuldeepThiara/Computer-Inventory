# Name = Kuldeep Thiara
# Class = CS3100

from Computer import Computer
from HTDictAbstract import HTDictAbstract

# Implementing a dictionary using hashtable


class HTDict(HTDictAbstract):

    def __init__(self, size=99):

        self.hash_table = [None]*size
        self.value = [None]*size
        self.size = size

    def get_key(self):
        return self.key

    def set_key(self, key):
        self.key = key

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    # Defining our print format. Now we can call
    # print(Node)

    def __str__(self):
        return str(self.key) + ": " + str(self.value)

    # Function to add key and value to hash table (Key is model name)
    def push(self, key, value):

        # Formating the key value
        key = key.upper()

        # We get the hash value
        hashvalue = self.hashfunction(key)

        # in case Slot is Empty
        if self.hash_table[hashvalue] == None:
            self.hash_table[hashvalue] = key
            self.value[hashvalue] = value

        else:

            # If the key already exists, replace old value
            if self.hash_table[hashvalue] == key:
                self.value[hashvalue] = value

            # Otherwise, find the next available slot - collision case
            else:

                nextslot = self.rehash(hashvalue)

                # Get to the next slot
                while self.hash_table[nextslot] != None and self.hash_table[nextslot] != key:
                    nextslot = self.rehash(nextslot)

                # Set new key, if NONE
                if self.hash_table[nextslot] == None:
                    self.hash_table[nextslot] = key
                    self.value[nextslot] = value

                # Otherwise replace old value
                else:
                    self.value[nextslot] = value

    # Function to add key and value to hash table (Key is date)
    def push2(self, key, value):

        # Formating the key value
        key = key.upper()

        # We get the hash value
        hashvalue = self.hashfunction(key)

        # in case Slot is Empty
        if self.hash_table[hashvalue] == None:
            self.hash_table[hashvalue] = key
            self.value[hashvalue] = value

        # Else get to the next slot
        else:
            while True:

                nextslot = self.rehash(hashvalue)
                if self.hash_table[nextslot] == None:

                    self.hash_table[nextslot] = key
                    self.value[nextslot] = value

                    break
                else:
                    hashvalue += 1

    # Function to search by Model name
    # Return key and value
    def search(self, key):

        # Set up variables for our search
        startslot = self.hashfunction(key)
        value = None
        stop = False
        found = False
        position = startslot

        # Until we discern that its not empty or found (and haven't stopped yet)
        while self.hash_table[position] != None and not found and not stop:

            if self.hash_table[position] == key:
                found = True
                value = self.value[position]

            else:
                position = self.rehash(position)
                if position == startslot:

                    stop = True

        return (key, value)

    # Function to search by Date
    # Returns list of data that contains the values associated with date
    def search2(self, key):
        # Set up variables for our search
        startslot = self.hashfunction(key)
        value = None
        stop = False
        found = False
        position = startslot
        resultList = []
        index = 0

        # Until we discern that its not empty or found (and haven't stopped yet)
        while self.hash_table[position] != None and not found and not stop:

            if self.hash_table[position] == key and index == 0:
                value = self.value[position]
                resultList.append(value)
                index = 1

            else:
                position = self.rehash(position)
                index = 0
                if position == startslot:
                    index = 1
                    stop = True

        return resultList

    # Takes the key as input and returns back the index for that specif key in the hash table
    def hashfunction(self, key):
        tablesize = self.size
        sum = 0
        for pos in range(len(key)):
            sum = sum + ord(key[pos])

        return sum % tablesize

    # For finding next possible positions
    def rehash(self, oldhash):
        tablesize = self.size
        # For finding next possible positions
        return (oldhash+1) % tablesize

    # Searches for index of the passed model name
    def searchIndex(self, key):

        # Gets the list from listOfModels function in this class
        list = self.listOfModels()

        try:
            keyIndex = list.index(key)
            return keyIndex
        except ValueError:
            return None

    # Function to add key to hash table (Key is model)
    def pushForIndex(self, key):
        self.hash_table.append(key)

    # Returns a list of models

    def listOfModels(self):

        tempList = []
        for x in self.hash_table:
            if x != None:
                tempList.append(x)

        return tempList
