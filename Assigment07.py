# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description:  Create a script that demonstrates how pickling and
#               structured error handling work.
# ChangeLog (Who,When,What):
# ALarkin,5.31.2022,Assignment 07
# ---------------------------------------------------------------------------- #

# -- Data -- #
# Declare variables and constants
datFile = "PersonalData.dat"    # An object that represents a file
dicRow = {}     # A row of data separated into elements of a dictionary
lstTable = []   # A list that acts as a 'table' of rows
strChoice = ""  # Capture the user option selection

# -- Processing -- #

# Step 1 - When the program starts, load data from PersonalData.dat
try:
    import os.path
    isfile_bln = (os.path.isfile(datFile))
    if (isfile_bln == True):
        import pickle
        # Read data with pickle.load method from datFile
        objFile = open(datFile, "rb")
        objFileData = pickle.load(objFile)
        objFile.close()
        print()  # adding a new line for looks
        print("****************************")
        print("Unpickle Data Completed") #unpickle
        print("****************************")
        print()
        for row in objFileData:
            print(row["Name"] + ' | ' + row["Address"] + ' | ' + row["Phone"] + ' | ' + row["Email"]
                  + ' | ' + row["DOB"] + ' | ' + row["SSN"])
            lstTable = (objFileData)
except FileNotFoundError as e:
    print("Error File Not Found:", e, sep='\n')
    # print("Built-In Python error info: ")
    # print(e, e.__doc__, type(e), sep='\n')
except Exception as e:
    print()
    print("Error Reading Data From File:", e, sep='\n')
    # print("Built-In Python error info: ")
    # print(e, e.__doc__, type(e), sep='\n')

# -- Input/Output -- #

# Step 2 - Display a menu of choices to the user.
while (True):
     print("""
     ****************************
     Option Menu: Personal Data
     ****************************
     1) Show current data
     2) Add data
     3) Remove data
     4) Save data 
     5) Exit Program
     ****************************
     """)

     strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
     print()  # adding a new line for looks

     # Step 3 - Show current data.
     if (strChoice.strip() == "1"):
         try:
            print() # adding a new line for looks
            print("****************************")
            print("Current Personal Data")
            print("****************************")
            for row in lstTable:
                print(row["Name"] + ' | ' + row["Address"] + ' | ' + row["Phone"] + ' | ' + row["Email"]
                  + ' | ' + row["DOB"] + ' | ' + row["SSN"])
         except Exception as e:
            print() # adding a new line for looks
            print("Error Showing Current Data:", e, sep='\n')
            # print("Built-In Python error info: ")
            # print(e, e.__doc__, type(e), sep='\n')
         continue

     # Step 4 - Add data.
     elif (strChoice.strip() == "2"):
         try:
            print("Enter personal data: ")
            strName = str(input("Name: ").strip().lower().title())
            strAddress = str(input("Address: ").strip().lower().title())
            strPhone = str(input("Phone Number: ").strip().replace(" ", "").replace("-", ""))
            if strPhone.isnumeric() != True or len(strPhone) != 10:
                raise Exception("Phone number contains characters or length not equal to 10: " + strPhone)
            strEmail = str(input("Email: ").strip().lower())
            if strEmail.find("@") == -1 or strEmail.find(".") == -1:
                raise Exception("Email improperly formatted: " + strEmail)
            strDOB = str(input("Date of Birth [yyyymmdd]: ").strip().replace(" ", "").replace("-", ""))
            if strDOB.isnumeric() != True or len(strDOB) != 8:
                raise Exception("DOB contains characters or length not equal to 8: " + strDOB)
            strSSN = str(input("Social Security Number: ").strip().replace(" ", "").replace("-", ""))
            if strSSN.isnumeric() != True or len(strSSN) != 9:
                raise Exception("SSN contains characters or length not equal to 9: " + strSSN)
            dicRow = {"Name": strName, "Address": strAddress, "Phone": strPhone, "Email": strEmail, "DOB": strDOB,
                    "SSN": strSSN}
            lstTable.append(dicRow)
         except Exception as e:
            print() # adding a new line for looks
            print("Error Adding Data:", e, sep='\n')
            # print("Built-In Python error info: ")
            # print(e, e.__doc__, type(e), sep='\n')
         continue

     # Step 5 - Remove data.
     elif (strChoice.strip() == "3"):
         try:
             strRemove = str(input("Enter a name to remove from personal details: ").strip().lower().title())
             remove_bln = False  # verify that the data was found
             for row in lstTable:
                 if (row["Name"] == strRemove):
                     lstTable.remove(row)
                     remove_bln = True
             # Update user on the status
             if remove_bln == True:
                 print()  # Add an extra line for looks
                 print("\n" + strRemove + " removed from personal details. ")
             else:
                 print()  # Add an extra line for looks
                 print(strRemove + " is not in personal details. ")
         except Exception as e:
            print() # adding a new line for looks
            print("Error Removing Data:", e, sep='\n')
            # print("Built-In Python error info: ")
            # print(e, e.__doc__, type(e), sep='\n')
         continue

     # Step 6 - Save Data.
     elif (strChoice.strip() == "4"):
         try:
             strOverwrite = str(input("Overwrite: " + datFile + "?" + " [y/n] ").strip().lower())
             if (strOverwrite == 'y'):
                 import pickle
                 objFile = open(datFile, "wb")
                 pickle.dump(lstTable, objFile)
                 objFile.close()
                 print()  # adding a new line for looks
                 print("*************")
                 print("Data Saved")
                 print("*************")
             else:
                 break
         except Exception as e:
             print()  # adding a new line for looks
             print("Error Saving Data:", e, sep='\n')
             # print("Built-In Python error info: ")
             # print(e, e.__doc__, type(e), sep='\n')
         continue

     # Step 7 – Exit the menu / program.
     elif (strChoice.strip() == "5"):
         break

input("\nPress the enter key to exit")



