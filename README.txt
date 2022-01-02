
Welcome to CIS (Computer inventory system)


In the beginning when the application is launched it will take you to login page, where it will ask you to enter your username and password. 

After you login, it will take you to the selection page, where you will have options displayed on the top of the page as tabs. Options = (Search, Update, Add Models, and All models)

Search option -> Gives you the option to search model and search all models by date. 
		Search model -> requires you to enter model name and will display quantity for that 				  
				model
		Search all -> requires you to enter a date and will display all model with 	quantity 		     						 			 				
				associated with that date. 

Update Option -> Gives you the option to update the quantity for the model selected from the dropdown  				
		menu. Once you select the model and enter the quantity and then press save. It will 
		display that the quantity for that model has been updated. 

Add Models Option -> Gives you the option to add model to list of model in the system. You first 
		    enter the model name and then press add. Then it will display that the entered 		
		    model has been added to the list in the system. 

All Models Option -> Displays all the models stored in the system in a scrollable list. 


The testing of this system has been explained in unit test file. 

____________________________________________________Login Info_______________________________________

	
				Username = admin 
				Password = admin123

------------------------------------------- tkmacosx Install instruction ----------------------------
	
			-> In terminal type the below command and then press enter
			-> pip install tkmacosx
			-> This will install tkmacosx 


*******************************( Purpose of each file ) *********************************************


cis.py -> Contains the code for GUI setup along with functions to read from CSV file. 

Computer.py -> Contains the code for the word class

ComputerInventoryHTDict.py -> Contains the function to search the model(key), search by date, search for index of model, list of 	  									      					  		                                                  models and add the key and computer object to HTDict 

HTDict.py -> Hash Table dictionary class

LLDictAbstract.py -> Linked list dictionary abstract class

HTDictAbstract.py -> Hash Table dictionary abstract class

HTDictTest.py -> Contains the code to test the computer and ComputerInventoryHTDict class

ComputerInventoryHTDictAbstract.py -> Computer Inventory abstract class

Inventory.csv -> This is CSV file where the program reads that data from. 

Meeting log -> Is the log for meeting the I attending for the group meeting.

Analysis Report - Provide my opinion about the new implementation in comparison of the old one  

HTDictTest Run Screen-Shot -> Displays results of running HTDictTest.py in Terminal 

GUI Screen Shot -> Displays results of running model search function in GUI 

GUI 2 Screen Shot -> Displays results of running search all by date function in GUI 