import Bussiness_Access_Layer.MySQLBAL as MySQL_Bal
import Bussiness_Access_Layer.SQLServerBAL as SQLServer_Bal
import Bussiness_Entities.Emp_Entities as Bent
import re

print("\033[1m\033[3m"+"Choose the SQL SERVER:\n 1. mySQL Connection\n 2. MS SERVER SQL Connection"+"\033[0m")
choose_server=int(input("\033[1m"+"Enter the server option(1-2):"+"\033[0m"))

obj_mySQL_Bal=MySQL_Bal.CEmpBal()
obj_MSSQL_Bal=SQLServer_Bal.CEmpBal()
if choose_server==1:
    obj_mySQL_Bal.mSQL_Server()
    choice = "yes"
    while choice == "yes":
        print("\033[1m\033[3m"+"\nDatabase Operations:"+"\033[0m")
        print("\033[1m\033[3m"+" 1. Insert \n 2. Update \n 3. Delete \n 4. Retrieval: \n\t4.1. Retrieve all data from the table."
              +"\n\t4.2. Retrieve specific row from the table."+"\033[0m")
        option = float(input("\033[1m"+"Enter the choice (1-4):"+"\033[0m"))
        if option == 1:
            print("\033[1m"+"INSERTION PROCESS STARTS..."+"\033[0m")
            obj_ent = Bent.CEmpEntities()
            emp_id=obj_mySQL_Bal.mAutomatic_emp_id()
            obj_ent.set_emp_id(emp_id)
            while True:
                fname = input("\n\tEnter the first name:")
                if re.match(r"^[A-Za-z]+([ A-Za-z'-]*[A-Za-z]+)*$", fname):
                    obj_ent.set_f_name(fname)
                    break
                else:
                    print(
                        "Invalid first name. Only alphabetic characters, spaces, hyphens, and apostrophes are allowed.")

            while True:
                lname = input("\tEnter the last name:")
                if re.match(r"^[A-Za-z]+([ A-Za-z'-]*[A-Za-z]+)*$", fname):
                    obj_ent.set_l_name(lname)
                    break
                else:
                    print(
                        "Invalid first name. Only alphabetic characters, spaces, hyphens, and apostrophes are allowed.")

            age = int(input("\tEnter the age:"))
            if age>=18 and 75 >= age:
                obj_ent.set_age(age)
            else:
                print("Please enter a valid age (between 18 and 75).")

            while True:
                sex = input("\tEnter the sex (M/F/T):")
                if sex in ["M", "F", "T"]:
                    obj_ent.set_sex(sex)
                    break
                else:
                    print("Please enter a valid sex (M/F/T).")

            email_id=str(fname.lower()+'.'+lname.lower()+"@example.com")
            obj_ent.set_email_id(email_id)

            while True:
                phone_no=input("\tEnter the phone number(XXX-XXX-XXXX):")
                if re.match(r"\d{3}-\d{3}-\d{4}", phone_no):
                    obj_ent.set_phone_no(phone_no)
                    break
                else:
                    print("Please enter the valid phone number.")

            department_id=int(input("\tEnter the Department ID :"))
            obj_ent.set_department_id(department_id)

            designation_id=int(input("\tEnter the Designation ID :"))
            obj_ent.set_designation_id(designation_id)

            manager_id=int(input("\tEnter the Manager ID :"))
            obj_ent.set_manager_id(manager_id)

            salary = float(input("\tEnter the salary:"))
            obj_ent.set_salary(salary)

            while True:
                level=int(input("\tEnter the level of the designation:"))
                if level in [1, 2, 3, 4]:
                    obj_ent.set_level(level)
                    break
                else:
                    print("Please enter the valid level of the designation(1,2,3,4).")

            commission=obj_mySQL_Bal.m_Automatic_commisssion(obj_ent)
            obj_ent.set_commission(commission)
            print("\tAccording to the Salary Commission of the employee :", obj_ent.get_commission())

            print("\033[1m"+"After insertion the table emp:"+"\033[0m")
            obj_mySQL_Bal.mInsert_Data(obj_ent)

        elif option == 2:
            obj_ent=Bent.CEmpEntities()
            print("\033[1m" + "UPDATION PROCESS STARTS..." + "\033[0m")
            while True:
                emp_id = int(input("Enter the Emp_id for updation:"))
                obj_ent.set_emp_id(emp_id)
                print("\tData of Emp_id {} for updation:".format(emp_id))
                obj_mySQL_Bal.mFilter_Data(obj_ent)
                if emp_id>obj_mySQL_Bal.mAutomatic_emp_id():
                    print("\n\tWARNING: Invalid emp_id.")
                else:
                    break
            option1=input("Do you want to update this data(Yes/No)?:").lower()
            if option1=="yes":
                while True:
                    fname = input("\tEnter the first name:")
                    if re.match(r"^[A-Za-z]+([ A-Za-z'-]*[A-Za-z]+)*$", fname):
                        obj_ent.set_f_name(fname)
                        break
                    else:
                        print(
                            "Invalid first name. Only alphabetic characters, spaces, hyphens, and apostrophes are allowed.")

                while True:
                    lname = input("\tEnter the last name:")
                    if re.match(r"^[A-Za-z]+([ A-Za-z'-]*[A-Za-z]+)*$", fname):
                        obj_ent.set_l_name(lname)
                        break
                    else:
                        print(
                            "Invalid first name. Only alphabetic characters, spaces, hyphens, and apostrophes are allowed.")

                age = int(input("\tEnter the age:"))
                if age >= 18 and 75 >= age:
                    obj_ent.set_age(age)
                else:
                    print("Please enter a valid age (between 18 and 75).")

                while True:
                    sex = input("\tEnter the sex (M/F/T):")
                    if sex in ["M", "F", "T"]:
                        obj_ent.set_sex(sex)
                        break
                    else:
                        print("Please enter a valid sex (M/F/T).")

                email_id = fname + '.' + lname + "@example.com"
                obj_ent.set_email_id(email_id)

                while True:
                    phone_no = input("\tEnter the phone number(XXX-XXX-XXXX):")
                    if re.match(r"\d{3}-\d{3}-\d{4}", phone_no):
                        obj_ent.set_phone_no(phone_no)
                        break
                    else:
                        print("Please enter the valid phone number.")

                designation = input("\tEnter the Designation :")
                obj_ent.set_designation(designation)

                salary = float(input("\tEnter the salary:"))
                obj_ent.set_salary(salary)

                while True:
                    level = int(input("\tEnter the level of the designation:"))
                    if level in [1, 2, 3, 4]:
                        obj_ent.set_level(level)
                        break
                    else:
                        print("Please enter the valid level of the designation(1,2,3,4).")

                commission = obj_mySQL_Bal.m_Automatic_commisssion(obj_ent)
                obj_ent.set_commission(commission)
                '''
                dictionary = {"Emp Id": obj_ent.get_emp_id(),
                              "First Name": obj_ent.get_f_name(),
                              "Last Name": obj_ent.get_l_name(),
                              "Age": obj_ent.get_age(),
                              "Sex": obj_ent.get_sex(),
                              "Email_id": obj_ent.get_email_id(),
                              "Phone_no": obj_ent.get_phone_no(),
                              "Salary": obj_ent.get_salary(),
                              "Commission": obj_ent.get_commission()}
                print("Data for updation:", dictionary)
                option = input("\tDo you want to update this data?(Yes/No):").lower()
                if option == "yes":
                    print("\nAfter updation the table emp:")
                    obj_mySQL_Bal.mUpdate_Data(obj_ent)
                '''
                obj_mySQL_Bal.mUpdate_Data(obj_ent)
            elif option1=="no":
                print("Updation of data is not permitted.")
            else:
                print("Enter the valid option(Yes/No).")

        elif option == 3:
            print("\033[1m" + "DELETION PROCESS STARTS..." + "\033[0m")
            obj_ent = Bent.CEmpEntities()
            emp_id = int(input("\n\tEnter the Emp_id for Deletion:"))
            obj_ent.set_emp_id(emp_id)
            print("Data for deletion of emp_id {}:".format(emp_id))
            obj_mySQL_Bal.mFilter_Data(obj_ent)
            option = input(
                "Do you want to delete this data for employee having emp_id {} ?(Yes/No):".format(emp_id)).lower()
            if option=="yes":
                print("Deletion of record from the table:")
                obj_mySQL_Bal.mDelete_Data(obj_ent)
            elif option=="no":
                print("Deletion of data is not permitted.")
            else:
                print("Enter the valid option(Yes/No).")

        elif option == 4:
            print("\033[1m" + "RETRIEVAL PROCESS STARTS..." + "\033[0m")
            option = float(input("\033[1m" +"Enter the option for Retrieval:"+ "\033[0m"))
            if option == 4.1:
                print("\033[1m" + "\nAll the records of the table:" + "\033[0m")
                obj_mySQL_Bal.mRetrieval_Data()
            elif option == 4.2:
                obj_ent = Bent.CEmpEntities()
                print(
                    "\033[1m\033[3m" + "\nEnter the option for retrieval of the data from emp table:\n 1. Emp ID \n 2. Phone Number \n 3. Email Id \n 4. First Name \n 5. Last Name  " + "\033[0m")
                option2 = int(input("Enter the option (1-5):"))
                if option2 == 1:
                    emp_id = int(input("\n\tEnter the emp id :"))
                    obj_ent.set_column_name('Emp_id')
                    obj_ent.set_column_value(emp_id)
                    obj_MSSQL_Bal.m_data_retrieval(obj_ent)
                elif option2 == 2:
                    phone_no = input("\n\tEnter the phone number :")
                    obj_ent.set_column_name('Phone_no')
                    obj_ent.set_column_value(phone_no)
                    obj_MSSQL_Bal.m_data_retrieval(obj_ent)
                elif option2 == 3:
                    email_id = input("\n\tEnter the Email id :")
                    obj_ent.set_column_name('Email_id')
                    obj_ent.set_column_value(email_id)
                    obj_MSSQL_Bal.m_data_retrieval(obj_ent)
                elif option2 == 4:
                    f_name = input("\n\tEnter the first name :")
                    obj_ent.set_column_name("First_name")
                    obj_ent.set_column_value(f_name)
                    obj_MSSQL_Bal.m_data_retrieval(obj_ent)
                elif option2 == 5:
                    l_name = input("\n\tEnter the last name :")
                    obj_ent.set_column_name("Last_name")
                    obj_ent.set_column_value(l_name)
                    obj_MSSQL_Bal.m_data_retrieval(obj_ent)
                else:
                    print("\n\t\033[1mWARNING:\033[1m Please enter the valid option.")
        else:
            print("\033[1m\033[3m"+"\nPlease enter the valid option."+"\033[0m")
        choice = input("\033[1m\033[3m"+"\nDo you want to perform more operations(Yes/No) :"+"\033[0m").lower()

elif choose_server==2:
    obj_MSSQL_Bal.mMSSQL_Server()
    choice = "yes"
    while choice == "yes":
        print("\033[1m\033[3m" + "\nDatabase Operations:" + "\033[0m")
        print(
            "\033[1m\033[3m" + " 1. Insert \n 2. Update \n 3. Delete \n 4. Retrieval: \n\t4.1. Retrieve all data from "
                               "the table."
                               "\n\t4.2. Retrieve specific row from the table." + "\033[0m")
        option = float(input("\033[1m" + "\nEnter the choice (1-4):" + "\033[0m"))
        if option == 1:
            print("\033[1m" + "INSERTION PROCESS STARTS..." + "\033[0m")
            obj_ent = Bent.CEmpEntities()
            emp_id=obj_MSSQL_Bal.mAutomatic_emp_id()
            obj_ent.set_emp_id(emp_id)
            while True:
                fname = input("\n\tEnter the first name:")
                if re.match(r"^[A-Za-z]+([ A-Za-z'-]*[A-Za-z]+)*$", fname):
                    obj_ent.set_f_name(fname)
                    break
                else:
                    print(
                        "Invalid first name. Only alphabetic characters, spaces, hyphens, and apostrophes are allowed.")

            while True:
                lname = input("\tEnter the last name:")
                if re.match(r"^[A-Za-z]+([ A-Za-z'-]*[A-Za-z]+)*$", fname):
                    obj_ent.set_l_name(lname)
                    break
                else:
                    print(
                        "Invalid first name. Only alphabetic characters, spaces, hyphens, and apostrophes are allowed.")

            age = int(input("\tEnter the age:"))
            if age >= 18 and 75 >= age:
                obj_ent.set_age(age)
            else:
                print("Please enter a valid age (between 18 and 75).")

            while True:
                sex = input("\tEnter the sex (M/F/T):")
                if sex in ["M", "F", "T"]:
                    obj_ent.set_sex(sex)
                    break
                else:
                    print("Please enter a valid sex (M/F/T).")

            email_id = str(fname.lower() + '.' + lname.lower() + "@example.com")
            obj_ent.set_email_id(email_id)

            while True:
                phone_no = input("\tEnter the phone number(XXX-XXX-XXXX):")
                if re.match(r"\d{3}-\d{3}-\d{4}", phone_no):
                    obj_ent.set_phone_no(phone_no)
                    break
                else:
                    print("Please enter the valid phone number.")

            department_id = int(input("\tEnter the Department ID :"))
            obj_ent.set_department_id(department_id)

            designation_id = int(input("\tEnter the Designation ID :"))
            obj_ent.set_designation_id(designation_id)

            manager_id = int(input("\tEnter the Manager ID :"))
            obj_ent.set_manager_id(manager_id)

            salary = float(input("\tEnter the salary:"))
            obj_ent.set_salary(salary)

            while True:
                level = int(input("\tEnter the level of the designation:"))
                if level in [1, 2, 3, 4]:
                    obj_ent.set_level(level)
                    break
                else:
                    print("Please enter the valid level of the designation(1,2,3,4).")

            commission = obj_MSSQL_Bal.m_Automatic_commisssion(obj_ent)
            obj_ent.set_commission(commission)
            print("\tAccording to the Salary Commission of the employee :", obj_ent.get_commission())

            print("\033[1m" + "After insertion the table emp:" + "\033[0m")
            obj_MSSQL_Bal.mInsert_Data(obj_ent)

        elif option == 2:
            obj_ent = Bent.CEmpEntities()
            print("\033[1m" + "UPDATION PROCESS STARTS..." + "\033[0m")
            while True:
                emp_id = int(input("Enter the Emp_id for updation:"))
                obj_ent.set_emp_id(emp_id)
                print("\tData of Emp_id {} for updation:".format(emp_id))
                obj_MSSQL_Bal.mFilter_Data(obj_ent)
                if emp_id > obj_MSSQL_Bal.mAutomatic_emp_id():
                    print("\n\tWARNING: Invalid emp_id.")
                else:
                    break
            option1 = input("Do you want to update this data(Yes/No)?:").lower()
            if option1 == "yes":
                while True:
                    fname = input("\tEnter the first name:")
                    if re.match(r"^[A-Za-z]+([ A-Za-z'-]*[A-Za-z]+)*$", fname):
                        obj_ent.set_f_name(fname)
                        break
                    else:
                        print(
                            "Invalid first name. Only alphabetic characters, spaces, hyphens, and apostrophes are allowed.")

                while True:
                    lname = input("\tEnter the last name:")
                    if re.match(r"^[A-Za-z]+([ A-Za-z'-]*[A-Za-z]+)*$", fname):
                        obj_ent.set_l_name(lname)
                        break
                    else:
                        print(
                            "Invalid first name. Only alphabetic characters, spaces, hyphens, and apostrophes are allowed.")

                age = int(input("\tEnter the age:"))
                if age >= 18 and 75 >= age:
                    obj_ent.set_age(age)
                else:
                    print("Please enter a valid age (between 18 and 75).")

                while True:
                    sex = input("\tEnter the sex (M/F/T):")
                    if sex in ["M", "F", "T"]:
                        obj_ent.set_sex(sex)
                        break
                    else:
                        print("Please enter a valid sex (M/F/T).")

                email_id = fname + '.' + lname + "@example.com"
                obj_ent.set_email_id(email_id)

                while True:
                    phone_no = input("\tEnter the phone number(XXX-XXX-XXXX):")
                    if re.match(r"\d{3}-\d{3}-\d{4}", phone_no):
                        obj_ent.set_phone_no(phone_no)
                        break
                    else:
                        print("Please enter the valid phone number.")

                designation = input("\tEnter the Designation :")
                obj_ent.set_designation(designation)

                salary = float(input("\tEnter the salary:"))
                obj_ent.set_salary(salary)

                while True:
                    level = int(input("\tEnter the level of the designation:"))
                    if level in [1, 2, 3, 4]:
                        obj_ent.set_level(level)
                        break
                    else:
                        print("Please enter the valid level of the designation(1,2,3,4).")

                commission = obj_MSSQL_Bal.m_Automatic_commisssion(obj_ent)
                obj_ent.set_commission(commission)
                '''
                dictionary = {"Emp Id": obj_ent.get_emp_id(),
                              "First Name": obj_ent.get_f_name(),
                              "Last Name": obj_ent.get_l_name(),
                              "Age": obj_ent.get_age(),
                              "Sex": obj_ent.get_sex(),
                              "Email_id": obj_ent.get_email_id(),
                              "Phone_no": obj_ent.get_phone_no(),
                              "Salary": obj_ent.get_salary(),
                              "Commission": obj_ent.get_commission()}
                print("Data for updation:", dictionary)
                option = input("\tDo you want to update this data?(Yes/No):").lower()
                if option == "yes":
                    print("\nAfter updation the table emp:")
                    obj_mySQL_Bal.mUpdate_Data(obj_ent)
                '''
                obj_MSSQL_Bal.mUpdate_Data(obj_ent)
            elif option1 == "no":
                print("Updation of data is not permitted.")
            else:
                print("Enter the valid option(Yes/No).")

        elif option == 3:
            print("\033[1m" + "DELETION PROCESS STARTS..." + "\033[0m")
            obj_ent = Bent.CEmpEntities()
            emp_id = int(input("\n\tEnter the Emp_id for Deletion:"))
            obj_ent.set_emp_id(emp_id)
            print("Data for deletion of emp_id {}:".format(emp_id))
            obj_MSSQL_Bal.mFilter_Data(obj_ent)
            option = input(
                "Do you want to delete this data for employee having emp_id {} ?(Yes/No):".format(emp_id)).lower()
            if option == "yes":
                print("Deletion of record from the table:")
                obj_MSSQL_Bal.mDelete_Data(obj_ent)
            elif option == "no":
                print("Deletion of data is not permitted.")
            else:
                print("Enter the valid option(Yes/No).")

        elif option == 4:
            print("\033[1m" + "RETRIEVAL PROCESS STARTS..." + "\033[0m")
            option = float(input("\033[1m" +"Enter the option for Retrieval:"+ "\033[0m"))
            if option == 4.1:
                print("\033[1m" + "\nAll the records of the table:" + "\033[0m")
                obj_MSSQL_Bal.mRetrieval_Data()
            elif option == 4.2:
                '''
                obj_ent = Bent.CEmpEntities()
                emp_id = input("\n\tEnter the Emp_id for Retrieval:")
                obj_ent.set_emp_id(emp_id)
                print("\033[1m\033[3m" + "\n The record of the employee having emp_id {}:" + "\033[0m".format(emp_id))
                obj_MSSQL_Bal.mFilter_Data(obj_ent)
                '''
                obj_ent = Bent.CEmpEntities()
                print("\033[1m\033[3m" + "\nEnter the option for retrieval of the data from emp table:\n 1. Emp ID \n 2. Phone Number \n 3. Email Id \n 4. First Name \n 5. Last Name  " + "\033[0m")
                option2 = int(input("Enter the option (1-5):"))
                if option2 == 1:
                    emp_id = int(input("\n\tEnter the emp id :"))
                    obj_ent.set_column_name('Emp_id')
                    obj_ent.set_column_value(emp_id)
                    obj_MSSQL_Bal.m_data_retrieval(obj_ent)
                elif option2 == 2:
                    phone_no=input("\n\tEnter the phone number :")
                    obj_ent.set_column_name('Phone_no')
                    obj_ent.set_column_value(phone_no)
                    obj_MSSQL_Bal.m_data_retrieval(obj_ent)
                elif option2 == 3:
                    email_id=input("\n\tEnter the Email id :")
                    obj_ent.set_column_name('Email_id')
                    obj_ent.set_column_value(email_id)
                    obj_MSSQL_Bal.m_data_retrieval(obj_ent)
                elif option2 == 4:
                    f_name=input("\n\tEnter the first name :")
                    obj_ent.set_column_name("First_name")
                    obj_ent.set_column_value(f_name)
                    obj_MSSQL_Bal.m_data_retrieval(obj_ent)
                elif option2 == 5:
                    l_name = input("\n\tEnter the last name :")
                    obj_ent.set_column_name("Last_name")
                    obj_ent.set_column_value(l_name)
                    obj_MSSQL_Bal.m_data_retrieval(obj_ent)
                else:
                    print("\n\t\033[1mWARNING:\033[1m Please enter the valid option.")
        else:
            print("\033[1m\033[3m" + "\nPlease enter the valid option." + "\033[0m")
        choice = input("\033[1m\033[3m" + "\nDo you want to perform more operations(Yes/No) :" + "\033[0m").lower()
else:
    print("\033[1m\033[3m" +"\nEnter the valid option for SQL Server."+ "\033[0m")