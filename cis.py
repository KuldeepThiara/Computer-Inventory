# Name = Kuldeep Thiara
# Class = CS-3100

# Import the required libraries
from tkinter import *
import tkinter.ttk as ttk
from tkmacosx import Button
from ComputerInventoryHTDict import ComputerInventoryHTDict
import os
import csv


# Class for setting up the pages for the App
class CIS(Tk):
    def __init__(self):
        Tk.__init__(self)
        container = ttk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        self.frames = {}
        # These are the six pages we going to have in this app
        for F in (LoginPage, SelectionPage, SearchPage, UpdatePage, AddModelPage, AllModelPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='NSEW')
        # Login page is the main page to be displayed
        self.show_frame(LoginPage)

    # Show frame function
    def show_frame(self, cont):
        frame = self.frames[cont]
        # tkraise used to switch between pages
        frame.tkraise()


# Class for the login page
class LoginPage(ttk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        ttk.Frame.__init__(self, parent)
        self.Login_widget()

    # Login page function
    def Login_widget(self):

        # Function for the login page to confirm  that the username and password matches
        def login():
            if username_entry.get() == "admin" and password_entry.get() == "admin123":
                command = self.controller.show_frame(SelectionPage)

        # Frame created with the size of 1200X650
        self.frame = Frame(self, width="1200", height="650",
                           background="#ede9e3")

        # Login in frame in the center on the window
        frame_login = LabelFrame(self.frame, bg="#fffff0", padx=25, pady=25)
        frame_login.place(relx=.5, rely=.5, anchor=CENTER)

        # Bold login label inside the frame_login frame
        login_label = Label(frame_login, text="Login",
                            bg="#fffff0", font=("canterall", 32, "bold"))
        login_label.grid(row=0, column=0)

        # Welcome to CIS label inside frame_login frame
        welcome_label = Label(frame_login, text="Welcome to CIS", bg="#fffff0", fg="#999999",
                              font=("canterall", 14))
        welcome_label.grid(row=1, column=0)

        # Blank label for creating space in between the welcome to CIS & Username label
        blank0_label = Label(frame_login, text="      ", bg="#fffff0")
        blank0_label.grid(row=2, column=0)

        # Blank label for creating space in between the welcome to CIS & Username label
        blank1_label = Label(frame_login, text="      ", bg="#fffff0")
        blank1_label.grid(row=3, column=0)

        # Blank label for creating space in between the welcome to CIS & Username label
        blank2_label = Label(frame_login, text="      ", bg="#fffff0")
        blank2_label.grid(row=4, column=0)

        # Username label inside frame_login frame
        username_label = Label(frame_login, text="USERNAME",
                               bg="#fffff0", font=("canterall", 12))
        username_label.grid(row=5, column=0, sticky=W)

        # Username entry field inside frame_login frame
        username_entry = Entry(frame_login, width=20,
                               borderwidth="2", bg="white")
        username_entry.grid(row=6, column=0, sticky=W)

        # Password label inside frame_login frame
        password_label = Label(frame_login, text="PASSWORD",
                               bg="#fffff0", font=("canterall", 12))
        password_label.grid(row=7, column=0, sticky=W)

        # Password entry field inside the frame_login frame
        password_entry = Entry(frame_login, show="*", width=20, bg="white")
        password_entry.grid(row=8, column=0, sticky=W)

        # Black label for creating space between password entry field and the login button
        blank3_label = Label(frame_login, text="      ", bg="#fffff0")
        blank3_label.grid(row=9, column=0)

        # Login button inside the frame_login frame
        Login_Button = Button(frame_login, text="  Login  ",
                              bg="#63ec69", command=lambda: login())

        Login_Button.grid(row=10, column=0)

        # Packing the frame
        self.frame.pack()

        def change_page(self):
            pass


# Class for the selection page
class SelectionPage(ttk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        ttk.Frame.__init__(self, parent)
        self.success_widget()

    # Selection page function
    def success_widget(self):

        # Created self.Selection_Frame Frame to contain other frame inside it
        self.Selection_Frame = Frame(self, bg="#fffff0")

        # Created Topbar_Frame frame to be contained inside Selection_Frame
        # This frame will store the four buttons (Search, Update, Add Models, All Models)
        Topbar_Frame = LabelFrame(
            self.Selection_Frame, bg="#fffff0", width=1200, height=50)

        # Search button to be contained inside Topbar_Frame frame
        # This will take you to the search page
        Search_Button = Button(Topbar_Frame, text='Search', width=300, height=48, bg="#d9d9d9", font=("canterall", 13, "bold"),
                               activeforeground="#fffff0", command=lambda: self.controller.show_frame(SearchPage))
        Search_Button.grid(row=0, column=0)

        # Update button to be contained inside Topbar_Frame frame
        # This will take you to the update page
        Update_Button = Button(Topbar_Frame, text='Update', width=300, height=48, bg="#d9d9d9", font=("canterall", 13, "bold"),
                               activeforeground="#fffff0", command=lambda: self.controller.show_frame(UpdatePage))
        Update_Button.grid(row=0, column=1)

        # Add Models button to be contained inside Topbar_Frame frame
        # This will take you to the Add Models page
        Addmodel_Button = Button(Topbar_Frame, text='Add Models', width=300, height=48, bg="#d9d9d9", font=("canterall", 13, "bold"),
                                 activeforeground="#fffff0", command=lambda: self.controller.show_frame(AddModelPage))
        Addmodel_Button.grid(row=0, column=2)

        # All Models button to be contained inside Topbar_Frame frame
        # This will take you to the All Models page
        Allmodels_Button = Button(Topbar_Frame, text='All Models', width=300, height=48, bg="#d9d9d9", font=("canterall", 13, "bold"),
                                  activeforeground="#fffff0", command=lambda: self.controller.show_frame(AllModelPage))
        Allmodels_Button.grid(row=0, column=3)

        # Organize the Topbar_Frame frame in grid
        Topbar_Frame.grid()
        Topbar_Frame.grid_propagate(0)

        # Selection_Frame frame to be placed right under the Topbar_Frame frame
        Selection_Frame = Frame(self.Selection_Frame,
                                bg="#fffff0", width=1200, height=550)

        # Created "Make a selection!" label inside Selection_Frame frame
        Selection_label = Label(Selection_Frame, text="Make a selection!", font=(
            "canterall", 30, "bold"), fg="#d9d9d9", bg="#fffff0")
        Selection_label.place(relx=.5, rely=.5, anchor=CENTER)

        # Organize the Selection_Frame frame in grid
        Selection_Frame.grid()
        Selection_Frame.grid_propagate(0)

        # Exit_Frame frame to store the exit button in the lower section of the window
        Exit_Frame = Frame(self.Selection_Frame,
                           bg="#fffff0", width=1200, height=50)

        # Exit button to be contained inside the center of Exit_Frame frame
        Exit_Button = Button(Exit_Frame, text="  Exit  ",  bg="Red", width=100, height=30,
                             command=lambda: exit())
        Exit_Button.place(relx=.5, rely=.5, anchor=CENTER)

        # Organize the Exit_Frame frame in grid
        Exit_Frame.grid()
        Exit_Frame.grid_propagate(0)

        # Organizethe self.Selection_Frame in pack
        self.Selection_Frame.pack(fill="both", expand=True)


# Class for search page
class SearchPage(ttk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        ttk.Frame.__init__(self, parent)
        self.Search_widget()

    # Function for Search page
    def Search_widget(self):

        # Created self.Search_Frame Frame to cont. other frame inside it
        self.Search_Frame = Frame(self, bg="#fffff0")

        # Created Topbar_Frame frame to be contained inside Search_Frame
        Topbar_Frame = LabelFrame(
            self.Search_Frame, bg="#fffff0", width=1200, height=50)

        # Search button to be contained inside Topbar_Frame frame
        Search_Button = Button(Topbar_Frame, text='Search', width=300, height=48, bg="#d9d9d9", font=("canterall", 13, "bold"),
                               activeforeground="#fffff0", command=lambda: self.controller.show_frame(SearchPage))
        Search_Button.grid(row=0, column=0)

        # Update button to be contained inside Topbar_Frame frame
        # This will take you to the update page
        Update_Button = Button(Topbar_Frame, text='Update', width=300, height=48, bg="#d9d9d9", font=("canterall", 13, "bold"),
                               activeforeground="#fffff0", command=lambda: self.controller.show_frame(UpdatePage))
        Update_Button.grid(row=0, column=1)

        # Add Models button to be contained inside Topbar_Frame frame
        # This will take you to the Add Models page
        Addmodel_Button = Button(Topbar_Frame, text='Add Models', width=300, height=48, bg="#d9d9d9", font=("canterall", 13, "bold"),
                                 activeforeground="#fffff0", command=lambda: self.controller.show_frame(AddModelPage))
        Addmodel_Button.grid(row=0, column=2)

        # All Models button to be contained inside Topbar_Frame frame
        # This will take to the all Models page
        Allmodels_Button = Button(Topbar_Frame, text='All Models', width=300, height=48, bg="#d9d9d9", font=("canterall", 13, "bold"),
                                  activeforeground="#fffff0", command=lambda: self.controller.show_frame(AllModelPage))
        Allmodels_Button.grid(row=0, column=3)

        # Organize the Topbar_Frame in grid
        Topbar_Frame.grid()
        Topbar_Frame.grid_propagate(0)

        # Selection_Frame frame to be placed right under the Topbar_Frame frame
        Selection_Frame = Frame(
            self.Search_Frame, bg="#fffff0",  height=550, width=1200)

        # Frame to display results
        resultFrame = Frame(Selection_Frame, bg="#fffff0",
                            height=550, width=600)

        columns = ('Model', 'Quantity')

        # Treeview list will display results for the searched query
        resultList = ttk.Treeview(
            resultFrame, columns=columns, show='headings')
        resultList.heading('Model', text='Model')
        resultList.heading('Quantity', text='Quantity')

        resultList.grid(row=0, column=0, sticky='nsew')

        # Result frame will be displayed on the right side
        resultFrame.grid(row=0, column=1)

        # Function to search specific model from csv file and display results
        def searchModel():

            columns = ('Model', 'Quantity')

            # Treeview list will display results for the searched query(Computer Model)
            resultList = ttk.Treeview(
                resultFrame, columns=columns, show='headings')
            resultList.heading('Model', text='Model')
            resultList.heading('Quantity', text='Quantity')

            resultList.grid(row=0, column=0, sticky='nsew')

            # Starting with clear list box
            for item in resultList.get_children():
                resultList.delete(item)

            cInventory = ComputerInventoryHTDict()

            # Reading the Inventory.csv file according to the key which is model
            cInventory.read_inventory("Inventory.csv", "Model")

            # Key is the model name that is searched by the user
            key = Model_entry.get().upper()

            # calling the search_model function with key intput
            # searching for the entered model
            computer = cInventory.search_model(key)

            # Inseting the data that is returned by searched query inside Treeview list.
            if computer == (key, None):
                resultList.insert('', 'end', values=(
                    key, "No data for the entery searched"))
            else:
                resultList.insert('', 'end', values=computer)

        # Function to search all data by specific date from csv file and display results

        def searchDate():

            columnsForDate = ('Model', 'Quantity', 'Date')

            # Treeview list will display results for the searched query(Date)
            resultList2 = ttk.Treeview(
                resultFrame, columns=columnsForDate, show='headings')
            resultList2.heading('Model', text='Model')
            resultList2.heading('Quantity', text='Quantity')
            resultList2.heading('Date', text='Date')

            resultList2.grid(row=0, column=0, sticky='nsew')

            # Starting with clear list box
            for item in resultList2.get_children():
                resultList2.delete(item)

            cInventory = ComputerInventoryHTDict()

            # Reading the Inventory.csv file
            cInventory.read_inventory("Inventory.csv", "Date")

            key = Date_entry.get()

            # calling the search_Date function with key(Date) intput
            # searching for the entered date
            computer = cInventory.search_Date(key)

            # Inseting the data that is returned by searched query inside Treeview list
            if computer == ([]):
                resultList2.insert('', 'end', values=(
                    "No data", "No data", "No data"))
            else:
                for x in computer:
                    resultList2.insert('', 'end', values=x)

        # Frame to display options that the user will have for search
        optionFrame = Frame(Selection_Frame, bg="#fffff0",
                            height=550, width=600, padx=125, pady=125)

        # Created "Model" label to be placed inside Selection_Frame
        Model_label = Label(optionFrame, text="Model",
                            bg="#fffff0", font=("canterall", 14, "bold"))
        Model_label.grid(row=0, column=0, sticky=W)

        # Created a model entry field to be placed right under the model label
        Model_entry = Entry(optionFrame, width=20, borderwidth="2", bg="white")
        Model_entry.grid(row=1, column=0, sticky=W)

        # Created a blank label to create space between the model entry field and search button
        blank0_label = Label(optionFrame, text="    ", bg="#fffff0")
        blank0_label.grid(row=1, column=1)

        # Created a search buttom to perform search for that specific model
        Search_Button = Button(optionFrame, text="Search",
                               bg="#63ec69", width=100, height=30, command=searchModel)
        Search_Button.grid(row=1, column=2, sticky=W)

        # A "Date" label to placed on top date entry field
        Date_label = Label(optionFrame, text="Date",
                           bg="#fffff0", font=("canterall", 14, "bold"))
        Date_label.grid(row=2, column=0, sticky=W)

        # Date entry field to enter the date to check the quanity of all models
        Date_entry = Entry(optionFrame, width=20, borderwidth="2", bg="white")
        Date_entry.grid(row=3, column=0, sticky=W)

        # Blank label to create space between date entry field and search all button
        blank1_label = Label(optionFrame, text="    ", bg="#fffff0")
        blank1_label.grid(row=3, column=1)

        # Search all button to search all the Laptops for that specific date
        Searchall_Button = Button(optionFrame, text="Search All",
                                  bg="#63ec69", width=100, height=30, command=searchDate)
        Searchall_Button.grid(row=3, column=2, sticky=W)

        # option frame will be displayed on the left side
        optionFrame.grid(row=0, column=0)

        # Organize the Selection_Frame frame in grid
        Selection_Frame.grid()
        Selection_Frame.grid_propagate(0)

        # Exit_Frame frame to store the exit button in the lower section of the window
        Exit_Frame = Frame(self.Search_Frame, bg="#fffff0",
                           width=1200, height=50)

        # Exit button to be contained inside the center of Exit_Frame frame
        Exit_Button = Button(Exit_Frame, text="  Exit  ",  bg="Red", width=100, height=30,
                             command=lambda: exit())
        Exit_Button.place(relx=.5, rely=.5, anchor=CENTER)

        # Organize the Exit_Frame frame in grid
        Exit_Frame.grid()
        Exit_Frame.grid_propagate(0)

        # Organizethe self.Selection_Frame in pack
        self.Search_Frame.pack(fill="both", expand=True)


# Class to update the inventory on computers
class UpdatePage(ttk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        ttk.Frame.__init__(self, parent)
        self.Update_widget()

    def Update_widget(self):

        # Created self.Update_Frame Frame to cont. other frame inside it
        self.Update_Frame = Frame(self, bg="#fffff0")

        # Created Topbar_Frame frame to be contained inside Update_Frame
        Topbar_Frame = LabelFrame(
            self.Update_Frame, bg="#fffff0", width=1200, height=50)

        # Search button to be contained inside Topbar_Frame frame
        Search_Button = Button(Topbar_Frame, text='Search', width=300, height=48, bg="#d9d9d9", font=("canterall", 13, "bold"),
                               activeforeground="#fffff0", command=lambda: self.controller.show_frame(SearchPage))
        Search_Button.grid(row=0, column=0)

        # Update button to be contained inside Topbar_Frame frame
        # This will take you to the update page
        Update_Button = Button(Topbar_Frame, text='Update', width=300, height=48, bg="#d9d9d9", font=("canterall", 13, "bold"),
                               activeforeground="#fffff0", command=lambda: self.controller.show_frame(UpdatePage))
        Update_Button.grid(row=0, column=1)

        # Add Models button to be contained inside Topbar_Frame frame
        # This will take you to the Add Models page
        Addmodel_Button = Button(Topbar_Frame, text='Add Models', width=300, height=48, bg="#d9d9d9", font=("canterall", 13, "bold"),
                                 activeforeground="#fffff0", command=lambda: self.controller.show_frame(AddModelPage))
        Addmodel_Button.grid(row=0, column=2)

        # All Models button to be contained inside Topbar_Frame frame
        # This will take to the all Models page
        Allmodels_Button = Button(Topbar_Frame, text='All Models', width=300, height=48, bg="#d9d9d9", font=("canterall", 13, "bold"),
                                  activeforeground="#fffff0", command=lambda: self.controller.show_frame(AllModelPage))
        Allmodels_Button.grid(row=0, column=3)

        # Organize the Topbar_Frame in grid
        Topbar_Frame.grid()
        Topbar_Frame.grid_propagate(0)

        # Selection_Frame frame to be placed right under the Topbar_Frame frame
        Selection_Frame = Frame(
            self.Update_Frame, bg="#fffff0", width=1200, height=550)

        # Frame to display results
        resultFrame = Frame(Selection_Frame, bg="#fffff0",
                            height=550, width=600, padx=125)

        # Result label for quanity saved
        result_label = Label(resultFrame, text=" ",
                             bg="#fffff0", font=("canterall", 14, "bold"))
        result_label.grid(row=0, column=0, sticky=W)

        # Result frame will be displayed on the right side
        resultFrame.grid(row=0, column=1)

        # Frame to display options that the user will have for search
        optionFrame = Frame(Selection_Frame, bg="#fffff0",
                            height=500, width=600, padx=150, pady=150)

        # Created "Select Model" label to be placed inside Selection_Frame
        Selectmodel_label = Label(
            optionFrame, text="Select Model ", bg="#fffff0", font=("canterall", 14, "bold"))
        Selectmodel_label.grid(row=0, column=0, sticky=W)

        # Gets the selected model from the option menu

        def selectedModel(selection):
            model.get()

        cInventory = ComputerInventoryHTDict()

        # Reading the Inventory.csv file according to keyType which is index
        # It returns only the model name from file
        cInventory.read_inventory("Inventory.csv", "Index")

        # calling the listOfModels function which returns a list of models
        computers = cInventory.listOfModels()

        # datatype of menu text
        model = StringVar()
        model.set(computers[0])

        # If the users leaves the quanity blank and then clicks the save button
        # This function will input 0 as the quantity

        def quantity():
            if Quantity_entry.get() == "":
                return 0
            else:
                return Quantity_entry.get()

        # Function to update the quantity for selected model in option menu

        def updateQuantity():
            cInventory.write_inventory(
                "Inventory.csv", model.get(), quantity(), "Update")
            result_label.config(
                text=('Quantity updated for the selected model to ' + str(quantity())))

        # Dropdown menu to select the model to update the quanity
        Selectmodel_dropmenu = OptionMenu(
            optionFrame, model, *computers, command=selectedModel)
        Selectmodel_dropmenu.config(width=17)
        Selectmodel_dropmenu.grid(row=0, column=1, sticky=W)

        # Label for "Quanity" to displayed on right of quanity entry field
        Quantity_label = Label(optionFrame, text="Quanity",
                               bg="#fffff0", font=("canterall", 14, "bold"))
        Quantity_label.grid(row=1, column=0, sticky=W)

        # Quanity entry field to enter the amount of Laptops in stock
        Quantity_entry = Entry(optionFrame, width=20,
                               borderwidth="2", bg="white")
        Quantity_entry.grid(row=1, column=1, sticky=W)

        # Save button to save the quanity of laptops that were entered in entry field
        Save_Button = Button(optionFrame, text="Save",  bg="#3b87d5",
                             width=100, height=30, command=updateQuantity)
        Save_Button.grid(row=2, column=1, sticky=W)

        # option frame will be displayed on the left side
        optionFrame.grid(row=0, column=0)

        Selection_Frame.grid()
        Selection_Frame.grid_propagate(0)

        # Exit_Frame frame to store the exit button in the lower section of the window
        Exit_Frame = Frame(self.Update_Frame, bg="#fffff0",
                           width=1200, height=50)

        # Exit button to close the program
        Exit_Button = Button(Exit_Frame, text="  Exit  ",  bg="Red", width=100, height=30,
                             command=lambda: exit())
        Exit_Button.place(relx=.5, rely=.5, anchor=CENTER)

        # Organize the Exit_Frame in grid
        Exit_Frame.grid()
        Exit_Frame.grid_propagate(0)

        # Organize Search_Frame in pack
        self.Update_Frame.pack(fill="both", expand=True)


# Class for Add Model page
class AddModelPage(ttk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        ttk.Frame.__init__(self, parent)
        self.AddModel_widget()

    def AddModel_widget(self):

        cInventory = ComputerInventoryHTDict()

        # Function to add new model name to the csv file
        def addModel():
            cInventory.write_inventory(
                "Inventory.csv", Model_entry.get(), 0, "Add")
            result_label.config(
                text='Entered Model "' + Model_entry.get() + '" has been added to the list')

        # Created self.AddModel_Frame Frame to cont. other frame inside it
        self.AddModel_Frame = Frame(self, bg="#fffff0")

        # Created Topbar_Frame frame to be contained inside AddModel_Frame
        Topbar_Frame = LabelFrame(
            self.AddModel_Frame, bg="#d9d9d9", width=1200, height=50)

        # Search button to be contained inside Topbar_Frame frame
        Search_Button = Button(Topbar_Frame, text='Search', width=300, height=48, bg="#d9d9d9", font=("canterall", 13, "bold"),
                               activeforeground="#fffff0", command=lambda: self.controller.show_frame(SearchPage))
        Search_Button.grid(row=0, column=0)

        # Update button to be contained inside Topbar_Frame frame
        # This will take you to the update page
        Update_Button = Button(Topbar_Frame, text='Update', width=300, height=48, bg="#d9d9d9", font=("canterall", 13, "bold"),
                               activeforeground="#fffff0", command=lambda: self.controller.show_frame(UpdatePage))
        Update_Button.grid(row=0, column=1)

        # Add Models button to be contained inside Topbar_Frame frame
        # This will take you to the Add Models page
        Addmodel_Button = Button(Topbar_Frame, text='Add Models', width=300, height=48, bg="#d9d9d9", font=("canterall", 13, "bold"),
                                 activeforeground="#fffff0", command=lambda: self.controller.show_frame(AddModelPage))
        Addmodel_Button.grid(row=0, column=2)

        # All Models button to be contained inside Topbar_Frame frame
        # This will take to the all Models page
        Allmodels_Button = Button(Topbar_Frame, text='All Models', width=300, height=48, bg="#d9d9d9", font=("canterall", 13, "bold"),
                                  activeforeground="#fffff0", command=lambda: self.controller.show_frame(AllModelPage))
        Allmodels_Button.grid(row=0, column=3)

        # Organize the Topbar_Frame in grid
        Topbar_Frame.grid()
        Topbar_Frame.grid_propagate(0)

        # AddModel_Frame frame to be placed right under the Topbar_Frame frame
        Selection_Frame = Frame(self.AddModel_Frame,
                                bg="#fffff0", width=1200, height=550)

        # Frame to display results
        resultFrame = Frame(Selection_Frame, bg="#fffff0",
                            height=550, width=600, padx=125)

        # Result label for quanity saved
        result_label = Label(resultFrame, text=" ",
                             bg="#fffff0", font=("canterall", 14, "bold"))
        result_label.grid(row=0, column=0, sticky=W)

        # Result frame will be displayed on the right side
        resultFrame.grid(row=0, column=1)

        # Frame to display options that the user will have for search
        optionFrame = Frame(Selection_Frame, bg="#fffff0",
                            height=550, width=600, padx=150, pady=150)

        # Created "Model Name" label to be placed inside Selection_Frame
        AddModel_label = Label(
            optionFrame, text="Model Name ", bg="#fffff0", font=("canterall", 14, "bold"))
        AddModel_label.grid(row=0, column=0, sticky=W)

        # Created a model entry field to be placed right under the model name label
        Model_entry = Entry(optionFrame, width=20, borderwidth="2", bg="white")
        Model_entry.grid(row=0, column=1, sticky=W)

        # Created a blank label to create space between the model entry field and add button
        blank0_label = Label(optionFrame, text="      ", bg="#fffff0")
        blank0_label.grid(row=1, column=1)

        # Add button to add the laptop model to the list
        Add_Button = Button(optionFrame, text="Add",  bg="#3b87d5",
                            width=180, height=30, command=addModel)
        Add_Button.grid(row=2, column=1, sticky=W)

        # option frame will be displayed on the left side
        optionFrame.grid(row=0, column=0)

        Selection_Frame.grid()
        Selection_Frame.grid_propagate(0)

        # Exit_Frame frame to store the exit button in the lower section of the window
        Exit_Frame = Frame(self.AddModel_Frame,
                           bg="#fffff0", width=1200, height=50)

        # Exit button to close the program
        Exit_Button = Button(Exit_Frame, text="  Exit  ",  bg="Red", width=100, height=30,
                             command=lambda: exit())
        Exit_Button.place(relx=.5, rely=.5, anchor=CENTER)

        # Organize the Exit_Frame in grid
        Exit_Frame.grid()
        Exit_Frame.grid_propagate(0)

        # Organize AddModel_Frame in pack
        self.AddModel_Frame.pack(fill="both", expand=True)


# Class for All model display page
class AllModelPage(ttk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        ttk.Frame.__init__(self, parent)
        self.AddModel_widget()

    # Function for All Model display page
    def AddModel_widget(self):

        # Created self.AllModel_Frame Frame to cont. other frame inside it
        self.AddModel_Frame = Frame(self, bg="#fffff0")

        # Created Topbar_Frame frame to be contained inside AllModel_Frame
        Topbar_Frame = LabelFrame(
            self.AddModel_Frame, bg="#d9d9d9", width=1200, height=50)

        # Search button to be contained inside Topbar_Frame frame
        Search_Button = Button(Topbar_Frame, text='Search', width=300, height=48, bg="#d9d9d9", font=("canterall", 13, "bold"),
                               activeforeground="#fffff0", command=lambda: self.controller.show_frame(SearchPage))
        Search_Button.grid(row=0, column=0)

        # Update button to be contained inside Topbar_Frame frame
        # This will take you to the update page
        Update_Button = Button(Topbar_Frame, text='Update', width=300, height=48, bg="#d9d9d9", font=("canterall", 13, "bold"),
                               activeforeground="#fffff0", command=lambda: self.controller.show_frame(UpdatePage))
        Update_Button.grid(row=0, column=1)

        # Add Models button to be contained inside Topbar_Frame frame
        # This will take you to the Add Models page
        Addmodel_Button = Button(Topbar_Frame, text='Add Models', width=300, height=48, bg="#d9d9d9", font=("canterall", 13, "bold"),
                                 activeforeground="#fffff0", command=lambda: self.controller.show_frame(AddModelPage))
        Addmodel_Button.grid(row=0, column=2)

        # All Models button to be contained inside Topbar_Frame frame
        # This will take to the all Models page
        Allmodels_Button = Button(Topbar_Frame, text='All Models', width=300, height=48, bg="#d9d9d9", font=("canterall", 13, "bold"),
                                  activeforeground="#fffff0", command=lambda: self.controller.show_frame(AllModelPage))
        Allmodels_Button.grid(row=0, column=3)

        # Organize the Topbar_Frame in grid
        Topbar_Frame.grid()
        Topbar_Frame.grid_propagate(0)

        # Selection_Frame frame to be placed right under the Topbar_Frame frame
        Selection_Frame = Frame(self.AddModel_Frame,
                                bg="#fffff0", width=1200, height=550)

        # Created "All Model Listed Below" label to be placed on top of the listbox
        AddModel_label = Label(
            Selection_Frame, text="All Models Listed Below ", bg="#fffff0", font=("canterall", 14))
        AddModel_label.place(relx=.5, rely=.32, anchor=CENTER)

        # Frame to to placed the list box inside
        Listbox_Frame = Frame(
            Selection_Frame, bg="#fffff0", width=200, height=300)

        # Scrollbar to be placed inside the Listbox_Frame frame
        scrollbar = Scrollbar(Listbox_Frame, orient=VERTICAL)

        # create listbox object
        AllModel_listbox = Listbox(Listbox_Frame, width=20,
                                   yscrollcommand=scrollbar.set)

        # configure scrollbar
        scrollbar.config(command=AllModel_listbox.yview)
        scrollbar.pack(side=RIGHT, fill=Y)

        # This is used refresh the list in listbox
        def refresh():

            cInventory = ComputerInventoryHTDict()

            # Reading the Inventory.csv file according to keyType which is Index
            cInventory.read_inventory("Inventory.csv", "Index")

            # calling the listOfModels function which returns a list of models
            computers = cInventory.listOfModels()

            AllModel_listbox.delete(0, END)

            # Adding all model to the listbox
            for row in computers:
                AllModel_listbox.insert(1, row)

        cInventory = ComputerInventoryHTDict()

        # Reading the Inventory.csv file according to keyType which is Index
        cInventory.read_inventory("Inventory.csv", "Index")

        # calling the listOfModels function which returns a list of models
        computers = cInventory.listOfModels()

        # Adding all model to the listbox
        for row in computers:
            AllModel_listbox.insert(1, row)

        # Organize the listbox in a pack
        AllModel_listbox.pack()

        # Refresh button to refresh the data in the list
        Refresh_Button = Button(Selection_Frame, text="Refresh",
                                bg="#3b87d5", width=100, height=30, command=refresh)
        Refresh_Button.place(relx=.5, rely=.25, anchor=CENTER)

        # Place the Listbox_Frame frame in the center of the parent frame
        Listbox_Frame.place(relx=.5, rely=.5, anchor=CENTER)

        # Organize the Selection_Frame in grid
        Selection_Frame.grid()
        Selection_Frame.grid_propagate(0)

        # Exit_Frame frame to store the exit button in the lower section of the window
        Exit_Frame = Frame(self.AddModel_Frame,
                           bg="#fffff0", width=1200, height=50)

        # Exit button to close the program
        Exit_Button = Button(Exit_Frame, text="  Exit  ",  bg="Red", width=100, height=30,
                             command=lambda: exit())
        Exit_Button.place(relx=.5, rely=.5, anchor=CENTER)

        # Organize the Exit_Frame in grid
        Exit_Frame.grid()
        Exit_Frame.grid_propagate(0)

        # Organize Search_Frame in pack
        self.AddModel_Frame.pack(fill="both", expand=True)


# App setup fucntion with its configuration
def appSetup():
    app = CIS()
    app.title('CIS')
    App_Width = 1200
    App_Height = 650
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()
    app.geometry(f'{App_Width}x{App_Height}+{0}+{0}')
    app.resizable(False, False)
    app.mainloop()

# Main method


def main():
    appSetup()


if __name__ == '__main__':
    main()
