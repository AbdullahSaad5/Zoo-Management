def add_animal_record(dictionary):  # User defined Functions
    confirm = "1"  # Defining variable for confirmation loop
    while confirm == "1":  # Confirmation Loop
        while True:  # Infinite loop
            try:  # Using Exception Handling
                animal_ID = input(f"\nEnter Animal ID Number: ")  # Getting Entities ID Number
                if animal_ID in dictionary:  # If ID already exists in record
                    print(
                        "ERROR: ID already Exists. Use another ID number or update record using UPDATE ANIMAL RECORD.")  # Print this in above case
                elif int(animal_ID) <= 0:  # If ID less than or equal to 0
                    print("ERROR: ID Can't be Zero Or Negative!")  # Print this in above case
                else:  # If ID is legit
                    break  # Break the infinite loop
            except ValueError:  # Using value Exception to prevent value error in Line 24 if an alphabetical value is entered.
                print(
                    "ERROR: You should provide an integral value to Animal ID")  # Print this in case of exception error
        animal_type_ = input(f"Enter Animal Type: ")  # Getting entity's information
        animal_name = input(f"Enter Animal Name: ")  # Getting entity's information
        animal_origin = input(f"Enter Animal Origin: ")  # Getting entity's information
        dictionary[animal_ID] = [animal_type_, animal_name, animal_origin]  # Storing value in the dictionary
        confirm = input("Enter 1 To Enter Data Again: ")  # Confirming if user wants to enter data again.


# ______________________________________________________________________________________________________________________
def view_animal_record(dictionary):  # User defined Functions
    print(f"An.ID\t\t\tAn.Type\t\t\tAn.Name\t\t\tAn.Origin")  # Printing tables top headings
    for key in dictionary.keys():  # Indenting over the keys of dictionary
        record = dictionary[key]  # Variable holding the value of the key specified
        # Printing data according to table
        print(key, "\t\t\t", record[0], "\t\t\t", record[1], "\t\t\t", record[2])


# ______________________________________________________________________________________________________________________
def search_animal_record(dictionary):  # User defined Functions
    search = input("Enter ID Number To Search: ")  # Getting input to match against record
    if search in dictionary.keys():  # If input is in record
        print("Record Found")  # Print this in above record
        record = dictionary[search]  # Variable holding the value of key specified
        print(f"ID\t\t\tType\t\t\tName\t\t\tOrigin")  # Printing table top headings
        # Printing data according to table
        print(search, "\t\t\t", record[0], "\t\t\t", record[1], "\t\t\t", record[2])
    else:  # If no such record exists
        print("ERROR: No Such Record Exists")  # Print this in above case


# ______________________________________________________________________________________________________________________
def update_animal_record(dictionary):  # User defined Functions
    update = input("Enter ID Number To Search: ")  # Getting input to match against record
    if update in dictionary.keys():  # If input is in record
        print("Record Found")  # Print this in above case
        record = dictionary[update]  # Variable holding the value of key specified
        # Getting user choice to update according to wish
        choice = input("""UPDATE ANIMAL RECORD
1) Animal ID
2) Animal Type
3) Animal Name
4) Animal Origin
5) All Of The Above
   Option: \t""")

        if choice == "1":  # If user chooses 1st option
            while True:  # Infinite Loop
                try:  # Using Exception Handling to prevent error at line 82 if alphabetical value is entered
                    animal_ID = input(f"Enter Animal New ID Number: ")  # Getting new ID for the entity
                    if int(animal_ID) <= 0:  # If ID is less than or equal to 0
                        print("ERROR: ID Can't be Zero Or Negative!")  # Print this in above case
                    elif animal_ID in dictionary:
                        print("ID already exists in the record. Try Again!")
                    else:  # If ID is legit
                        break  # Break the infinite loop
                except ValueError:  # Using value Exception to prevent value error in Line 24 if an alphabetical value is entered.
                    print(
                        "ERROR: You should provide an integral value to Animal ID")  # Print this in case of exception error
            dictionary[animal_ID] = dictionary[update]  # Copying the existing key data to new key entered
            dictionary.pop(update)  # Removing the old record from the dictionary
        elif choice == "2":  # If user chooses 2nd option
            record[0] = input("Enter a New Animal Type: ")  # Getting new data of the entity
        elif choice == "3":  # If user chooses 2nd option
            record[1] = input("Enter a New Animal Name: ")  # Getting new data of the entity
        elif choice == "4":  # If user chooses 2nd option
            record[2] = input("Enter a New Animal Origin: ")  # Getting new data of the entity
        elif choice == "5":  # If user chooses 2nd option
            while True:
                try:  # Using Exception Handling to prevent error at line 82 if alphabetical value is entered
                    animal_ID = input(f"Enter Animal New ID Number: ")  # Getting new ID for the entity
                    if int(animal_ID) <= 0:  # If ID is less than or equal to 0
                        print("ERROR: ID Can't be Zero Or Negative!")  # Print this in above case
                    elif animal_ID in dictionary:
                        print("ID already exists in the record. Try Again!")
                    else:  # If ID is legit
                        break  # Break the infinite loop
                except ValueError:  # Using value Exception to prevent value error in Line 24 if an alphabetical value is entered.
                    print(
                        "ERROR: You should provide an integral value to Animal ID")  # Print this in case of exception error
            animal_type_ = input("Enter a New Animal Type: ")  # Getting new data of the entity
            animal_name = input("Enter a New Animal Name: ")  # Getting new data of the entity
            animal_origin = input("Enter a New Animal Origin: ")  # Getting new data of the entity
            dictionary[animal_ID] = dictionary[update]  # Copying the existing key data to new key entered
            dictionary.pop(update)  # Removing the old record from the dictionary
            dictionary[animal_ID] = [animal_type_, animal_name,
                                     animal_origin]  # Assigning new values to new key and updating it in dictionary
        else:  # If none of the above choices entered
            print("ERROR: Invalid Command Entered")  # Print this in above case
    else:  # If ID is not in the record
        print("ERROR: No Such Record Exists")  # Print this in above case


# ______________________________________________________________________________________________________________________
def delete_ind_anm_record(dictionary):  # User defined Functions
    delete = input("Enter the ID Number to Delete: ")  # Getting input to delete the ID
    if delete in dictionary.keys():  # If ID is in the record
        print("Record Found")  # Print this in above case
        delConfirm = input("Enter YES to Confirm delete: ")  # Confirming the deletion process
        if delConfirm.upper() == "YES":  # If user confirms
            dictionary.pop(delete)  # Print the key to delete the whole individual record
            print("Data Deleted")  # Confirming that data is deleted

        else:  # If user doesn't confirm deletion
            print("ERROR: Deletion Process Halted.")  # Print this in above case
    else:  # If ID is not in the record
        print("ERROR: No Such Record Found!")  # Print this in above case


# ______________________________________________________________________________________________________________________
def delete_all_anm_record(dictionary):  # User defined Functions
    delConfirm = input("Enter YES to Confirm delete: ")  # Confirming the deletion process
    if delConfirm.upper() == "YES":  # If user confirms
        dictionary.clear()  # Deleting all the data
        print("All Data Deleted")  # Confirming that data is deleted
    else:  # If user doesn't confirm deletion
        print("ERROR: Deletion Process Halted.")  # Print this in above case


# ______________________________________________________________________________________________________________________
def animal_menu(dictionary):  # User defined Functions
    dataEntered = False  # Boolean Variable Finding Out If Data Is Entered
    while True:  # Infinite Loop
        # Main Menu presenting choices within programs
        check = input("""\nAnimal Management System
1) ADD Animal Record
2) VIEW Animal Record
3) SEARCH Animal Record
4) UPDATE Animal Record
5) DELETE Animal Record
6) EXIT to Main Menu
   Choice: \t""")

        if check == "1":  # If user chooses 1st option
            add_animal_record(dictionary)
            dataEntered = True  # Boolean Variable changed to True to confirm data entry.

        elif check == "2":  # If user chooses 2nd option
            if not dataEntered:  # If the given dictionary is still empty
                print("ERROR: No Record Exists.")  # Print this in above case
            else:  # If data is already entered
                view_animal_record(dictionary)

        elif check == "3":  # If user chooses 3rd option
            if not dataEntered:  # If the given dictionary is still empty
                print("ERROR: No Record Exists.")  # Print this in above case
            else:  # If the data is already entered
                search_animal_record(dictionary)
        elif check == "4":  # If user chooses 4th option
            if not dataEntered:  # If given dictionary is empty
                print("ERROR: No Record Exists.")  # Print this in above case
            else:  # If the data is already entered
                update_animal_record(dictionary)

        elif check == "5":  # If user chooses 5th option
            if not dataEntered:  # If given dictionary is still empty
                print("ERROR: No Record Exists.")  # Print this in above case
            else:  # If data is already entered
                # Getting user choice over deletion process
                del_check = input("""DELETE ANIMAL RECORD
1) Delete Individual Record
2) Delete All Record
   Option: \t""")

                if del_check == "1":  # If user chooses 1st option
                    delete_ind_anm_record(dictionary)
                    if dictionary == {}:  # If the dictionary becomes empty
                        dataEntered = False  # Changing the boolean variable to False

                elif del_check == "2":
                    delete_all_anm_record(dictionary)
                    dataEntered = False  # Changing the boolean variable to False
                else:  # If users enters invalid command
                    print("ERROR: Invalid Command Entered!")  # Print this in above case

        elif check == "6":  # If user chooses 6th option
            break  # Breaking infinite loop

        else:  # If none of the above options entered
            print("ERROR: Invalid Command Entered")  # Print this in above case

    print("Animal Management System is Closing.")  # Print this in the end of the program


# ______________________________________________________________________________________________________________________
def add_employee_record(dictionary):  # User defined Functions
    confirm = "1"  # Defining variable for confirmation loop
    while confirm == "1":  # Confirmation Loop
        while True:  # Infinite loop
            try:  # Using Exception Handling
                employee_ID = input(f"\nEnter Employee ID Number: ")  # Getting Entities ID Number
                if employee_ID in dictionary:  # If ID already exists in record
                    print(
                        "ERROR: ID already Exists. Use another ID number or update record using UPDATE Employee RECORD.")  # Print this in above case
                elif int(employee_ID) <= 0:  # If ID less than or equal to 0
                    print("ERROR: ID Can't be Zero Or Negative!")  # Print this in above case
                else:  # If ID is legit
                    break  # Break the infinite loop
            except ValueError:  # Using value Exception to prevent value error in Line 24 if an alphabetical value is entered.
                print(
                    "ERROR: You should provide an integral value to Employee ID")  # Print this in case of exception error
        employee_name = input(f"Enter Employee Name: ")  # Getting entity's information
        employee_age = input(f"Enter Employee Age: ")  # Getting entity's information
        employee_salary = input(f"Enter Employee Salary: Rs. ")  # Getting entity's information
        employee_service = input(f"Enter Employee Service: ")  # Getting entity's information
        employee_working_hours = input(f"Enter Employee Working Hours: ")  # Getting entity's information
        dictionary[employee_ID] = [employee_name, employee_age, employee_salary, employee_service,
                                   employee_working_hours]  # Storing value in the dictionary
        confirm = input("Enter 1 To Enter Data Again: ")  # Confirming if user wants to enter data again.


# ______________________________________________________________________________________________________________________
def view_employee_record(dictionary):  # User defined Functions
    print(f"ID\t\t\tName\t\t\tAge\t\t\tSalary(Rupees)\t\t\tService\t\t\tW.Hours")  # Printing tables top headings
    for key in dictionary.keys():  # Indenting over the keys of dictionary
        record = dictionary[key]  # Variable holding the value of the key specified
        # Printing data according to table
        print(key, "\t\t\t", record[0], "\t\t\t", record[1], "\t\t\t", record[2], "\t\t\t", record[3], "\t\t\t",
              record[4])


# ______________________________________________________________________________________________________________________
def search_employee_record(dictionary):  # User defined Functions
    search = input("Enter ID Number To Search: ")  # Getting input to match against record
    if search in dictionary.keys():  # If input is in record
        print("Record Found")  # Print this in above record
        record = dictionary[search]  # Variable holding the value of key specified
        print(f"ID\t\t\tName\t\t\tAge\t\t\tSalary\t\t\tService\t\t\tW.Hours")  # Printing tables top headings
        # Printing data according to table
        print(search, "\t\t\t", record[0], "\t\t\t", record[1], "\t\t\t", record[2], "\t\t\t", record[3], "\t\t\t",
              record[4])

    else:  # If no such record exists
        print("ERROR: No Such Record Exists")  # Print this in above case


# ______________________________________________________________________________________________________________________
def update_employee_record(dictionary):  # User defined Functions
    update = input("Enter ID Number To Search: ")  # Getting input to match against record
    if update in dictionary.keys():  # If input is in record
        print("Record Found")  # Print this in above case
        record = dictionary[update]  # Variable holding the value of key specified
        # Getting user choice to update according to wish
        choice = input("""UPDATE Employee RECORD
1) Employee ID
2) Employee Name
3) Employee Age
4) Employee Salary
5) Employee Service
6) Employee Working Hours
7) All Of The Above
   Option: \t""")

        if choice == "1":  # If user chooses 1st option
            while True:  # Infinite Loop
                try:  # Using Exception Handling to prevent error at line 82 if alphabetical value is entered
                    employee_ID = input(f"Enter Employee New ID Number: ")  # Getting new ID for the entity
                    if int(employee_ID) <= 0:  # If ID is less than or equal to 0
                        print("ERROR: ID Can't be Zero Or Negative!")  # Print this in above case
                    elif employee_ID in dictionary:
                        print("ID already exists in the record. Try Again!")
                    else:  # If ID is legit
                        break  # Break the infinite loop
                except ValueError:  # Using value Exception to prevent value error in Line 24 if an alphabetical value is entered.
                    print(
                        "ERROR: You should provide an integral value to Employee ID")  # Print this in case of exception error
            dictionary[employee_ID] = dictionary[update]  # Copying the existing key data to new key entered
            dictionary.pop(update)  # Removing the old record from the dictionary
        elif choice == "2":  # If user chooses 2nd option
            record[0] = input("Enter a New Employee Name: ")  # Getting new data of the entity
        elif choice == "3":  # If user chooses 3rd option
            record[1] = input("Enter a New Employee Age: ")  # Getting new data of the entity
        elif choice == "4":  # If user chooses 4th option
            record[2] = input("Enter a New Employee Salary: Rs. ")  # Getting new data of the entity
        elif choice == "5":  # If user chooses 5th option
            record[3] = input("Enter a New Employee Service: ")  # Getting new data of the entity
        elif choice == "6":
            record[4] = input("Enter a New Employee Working Hours: ")  # Getting new data of the entity
        elif choice == "7":
            while True:
                try:  # Using Exception Handling to prevent error at line 82 if alphabetical value is entered
                    employee_ID = input(f"Enter Employee New ID Number: ")  # Getting new ID for the entity
                    if int(employee_ID) <= 0:  # If ID is less than or equal to 0
                        print("ERROR: ID Can't be Zero Or Negative!")  # Print this in above case
                    elif employee_ID in dictionary:
                        print("ID already exists in the record. Try Again!")
                    else:  # If ID is legit
                        break  # Break the infinite loop
                except ValueError:  # Using value Exception to prevent value error in Line 24 if an alphabetical value is entered.
                    print(
                        "ERROR: You should provide an integral value to Employee ID")  # Print this in case of exception error
            employee_name = input("Enter a New Employee Name: ")  # Getting new data of the entity
            employee_age = input("Enter a New Employee Age: ")  # Getting new data of the entity
            employee_salary = input("Enter a New Employee Salary: Rs. ")  # Getting new data of the entity
            employee_service = input("Enter a New Employee Service: ")
            employee_working_hours = input("Enter a New Employee Working Hours: ")
            dictionary[employee_ID] = dictionary[update]  # Copying the existing key data to new key entered
            dictionary.pop(update)  # Removing the old record from the dictionary
            dictionary[employee_ID] = [employee_name, employee_age, employee_salary, employee_service,
                                       employee_working_hours]  # Assigning new values to new key and updating it in dictionary
        else:  # If none of the above choices entered
            print("ERROR: Invalid Command Entered")  # Print this in above case
    else:  # If ID is not in the record
        print("ERROR: No Such Record Exists")  # Print this in above case


# ______________________________________________________________________________________________________________________
def delete_ind_emp_record(dictionary):  # User defined Functions
    delete = input("Enter the ID Number to Delete: ")  # Getting input to delete the ID
    if delete in dictionary.keys():  # If ID is in the record
        print("Record Found")  # Print this in above case
        delConfirm = input("Enter YES to Confirm delete: ")  # Confirming the deletion process
        if delConfirm.upper() == "YES":  # If user confirms
            dictionary.pop(delete)  # Print the key to delete the whole individual record
            print("Data Deleted")  # Confirming that data is deleted

        else:  # If user doesn't confirm deletion
            print("ERROR: Deletion Process Halted.")  # Print this in above case
    else:  # If ID is not in the record
        print("ERROR: No Such Record Found!")  # Print this in above case


# ______________________________________________________________________________________________________________________
def delete_all_emp_record(dictionary):  # User defined Functions
    delConfirm = input("Enter YES to Confirm delete: ")  # Confirming the deletion process
    if delConfirm.upper() == "YES":  # If user confirms
        dictionary.clear()  # Deleting all the data
        print("All Data Deleted")  # Confirming that data is deleted
    else:  # If user doesn't confirm deletion
        print("ERROR: Deletion Process Halted.")  # Print this in above case


# ______________________________________________________________________________________________________________________
def employee_menu(dictionary):  # User defined Functions
    dataEntered = False  # Boolean Variable Finding Out If Data Is Entered
    while True:  # Infinite Loop
        # Main Menu presenting choices within programs
        check = input("""\nEmployee Management System
1) ADD Employee Record
2) VIEW Employee Record
3) SEARCH Employee Record
4) UPDATE Employee Record
5) DELETE Employee Record
6) EXIT to Main Menu
Option: \t""")

        if check == "1":  # If user chooses 1st option
            add_employee_record(dictionary)
            dataEntered = True  # Boolean Variable changed to True to confirm data entry.

        elif check == "2":  # If user chooses 2nd option
            if not dataEntered:  # If the given dictionary is still empty
                print("ERROR: No Record Exists.")  # Print this in above case
            else:  # If data is already entered
                view_employee_record(dictionary)

        elif check == "3":  # If user chooses 3rd option
            if not dataEntered:  # If the given dictionary is still empty
                print("ERROR: No Record Exists.")  # Print this in above case
            else:  # If the data is already entered
                search_employee_record(dictionary)
        elif check == "4":  # If user chooses 4th option
            if not dataEntered:  # If given dictionary is empty
                print("ERROR: No Record Exists.")  # Print this in above case
            else:  # If the data is already entered
                update_employee_record(dictionary)

        elif check == "5":  # If user chooses 5th option
            if not dataEntered:  # If given dictionary is still empty
                print("ERROR: No Record Exists.")  # Print this in above case
            else:  # If data is already entered
                # Getting user choice over deletion process
                del_check = input("""DELETE Employee RECORD
1) Delete Individual Record
2) Delete All Record
Option: \t""")

                if del_check == "1":  # If user chooses 1st option
                    delete_ind_emp_record(dictionary)
                    if dictionary == {}:  # If the dictionary becomes empty
                        dataEntered = False  # Changing the boolean variable to False

                elif del_check == "2":
                    delete_all_emp_record(dictionary)
                    dataEntered = False  # Changing the boolean variable to False
                else:  # If users enters invalid command
                    print("ERROR: Invalid Command Entered!")  # Print this in above case

        elif check == "6":  # If user chooses 6th option
            break  # Breaking infinite loop

        else:  # If none of the above options entered
            print("ERROR: Invalid Command Entered")  # Print this in above case

    print("Employee Management System is Closing.")  # Print this in the end of the program


# ______________________________________________________________________________________________________________________
def add_service_record(dictionary):  # User defined Functions
    while True:  # Infinite Loop
        try:  # Using exception handling to prevent invalid ID input
            service_ID = input("\nEnter Service ID Number: ")  # Getting service ID number
            if service_ID in dictionary:  # If ID already exists.
                print("ID already exists. Try Again!")  # Print this in above case
            elif int(service_ID) <= 0:  # If ID is less than or equal to zero
                print("ID can't be zero or negative!")  # Print this in above case
            else:  # If ID is legit
                break  # Breaking Infinite Loop
        except ValueError:  # Using exception to prevent error at Line 419 if alphabetic value is entered
            print("ERROR: You should provide an integral value to Animal ID")  # Printing if error found
    employee_ID = input("Enter Employee ID No. allotted the service:  ")  # Getting employee ID number
    if employee_ID not in employee_record:  # If ID doesn't exist in the record
        print("ERROR: ID Not Found! Please Try Again!")  # Print Error
    else:  # If data matches the record
        animal_ID = input("Enter Employee ID No. allotted the service: ")  # Getting animal ID number
        if animal_ID not in animal_record:  # If ID doesn't exist in the record
            print("ERROR: ID Not Found! Please Try Again!")  # Print Error
        else:  # If data matches the record
            service_duration = input("Enter the Hours of Service Duration: ")  # Getting info of service attributes
            service_hours = input("Enter the Service Hours: ")  # Getting info of service attributes
            service_location = input(
                "Enter the Location service is being performed: ")  # Getting info of service attributes
            dictionary[service_ID] = [employee_ID, animal_ID, service_duration, service_hours,
                                      service_location]  # Adding data to service record


# ______________________________________________________________________________________________________________________
def view_services_record(dictionary):  # User Defined Functions
    # Printing table top headings
    print(
        "Service ID \t\t\t Employee ID \t\t\t Animal ID \t\t\t Service Duration \t\t\t Service Hours \t\t\t Service Location")
    for key in dictionary.keys():  # Indenting over the keys of the dictionary
        record = dictionary[key]  # Getting the value of the key
        # Printing the values according to the table
        print(key, "\t\t\t", record[0], "\t\t\t", record[1], "\t\t\t", record[2], "\t\t\t", record[3], "\t\t\t",
              record[4])


# ______________________________________________________________________________________________________________________
def search_services_record(dictionary):  # User Defined Functions
    search = input(
        "Enter ID Number To Search: ")  # Getting input to match against record  # Getting input to match against record
    if search in dictionary.keys():  # If input is in record  # If found
        print("Record Found")  # Print this in above record  # Print this in above case
        record = dictionary[search]  # Variable holding the value of key specified  # Getting value of the record
        # Printing table top headings
        print(
            "Service ID \t\t\t Employee ID \t\t\t Animal ID \t\t\t Service Duration \t\t\t Service Hours \t\t\t Service Location")
        # Printing data according to table
        print(search, "\t\t\t", record[0], "\t\t\t", record[1], "\t\t\t", record[2], "\t\t\t", record[3], "\t\t\t",
              record[4])
    else:  # If no such record exists
        print("ERROR: No Such Record Exists")  # Print this in above case


# ______________________________________________________________________________________________________________________
def services_menu(dictionary):  # User Defined Functions
    dataEntered = False  # Defining variable to declare the state of data Entry
    while True:  # Infinite Loop
        # Getting user choice for execution
        check = input("""\nServices Management System
1. ADD Services
2. VIEW Services
3. SEARCH Services
4. EXIT to Main Menu
Option: \t""")

        if check == "1":  # If user chooses 1st Option
            add_service_record(dictionary)  # Calling user defined functions
            dataEntered = True  # Declaring that data is entered

        elif check == "2":  # If user chooses 2nd Option
            if not dataEntered:  # If data is not entered
                print("No Record Found!")  # Print this in above case
            else:  # If data is entered
                view_services_record(dictionary)  # Calling user defined function

        elif check == "3":  # If user chooses 3rd Option
            if not dataEntered:  # If data is not entered
                print("No Record Found!")  # Print this in above case
            else:  # If data is entered already
                search_services_record(dictionary)  # Calling user defined function

        elif check == "4":  # If user chooses 4th option
            break  # Breaking infinite loop

        else:  # If user inputs wrong option
            print("Invalid Command")  # Print this error


# ______________________________________________________________________________________________________________________
def main_menu():  # Defining main_menu option calling all the rest of the functions
    while True:  # Infinite Loop
        # Getting user choice
        main_check = input("""\nWelcome To ZOO MANAGEMENT SYSTEM
1. Animal Management System
2. Employee Management System
3. Services Management System
4. EXIT Program
Option:\t""")

        if main_check == "1":  # If user chooses 1st option
            animal_menu(animal_record)  # Calling user defined function

        elif main_check == "2":  # If user chooses 2nd option
            employee_menu(employee_record)  # Calling user defined function

        elif main_check == "3":  # If user chooses 2nd option
            services_menu(services_record)  # Calling user defined function

        elif main_check == "4":  # If user chooses 2nd option
            break  # Breaking infinite loop

        else:  # If user inputs invalid command
            print("Invalid Command Entered")  # Print this error


# ______________________________________________________________________________________________________________________
animal_record = {}  # Empty dictionary for animal record
employee_record = {}  # Empty dictionary for employee record
services_record = {}  # Empty dictionary for services record

main_menu()  # Calling the main function to invoke all the rest

print("Thanks For Using Zoo Management System")
