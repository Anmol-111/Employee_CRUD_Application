import Bussiness_Entities.Emp_Entities as Bent
import Data_Access_Layer.EmpDB as Edb

class CEmpBal:
    """Bussiness Access Layer"""

    def mSQL_Server(self):
        obj_db=Edb.CEmpDB()
        obj_db.m_Connect_mySQL()

    def mMSSQL_Server(self):
        obj_db=Edb.CEmpDB()
        obj_db.m_Connect_MSSQL()

    def mInsert_Data(self, obj_ent=Bent.CEmpEntities()):
        obj_db = Edb.CEmpDB()
        dictionary={"Emp Id": obj_ent.get_emp_id(),
                    "First Name": obj_ent.get_f_name(),
                    "Last Name": obj_ent.get_l_name(),
                    "Age": obj_ent.get_age(),
                    "Sex": obj_ent.get_sex(),
                    "Salary": obj_ent.get_salary()}
        print("Data for Insertion:", dictionary)
        option=input("Do you want to insert this data?(Yes/No):").upper()
        if option=="YES":
            print("After insertion the table emp:")
            obj_db.m_Insert_Data(obj_ent)
        elif option=="NO":
            print("Insertion of data is not permitted.")
        else:
            print("Please enter the valid option(Yes/No)")
    
    def mUpdate_Data(self, obj_ent=Bent.CEmpEntities()):
        obj_db = Edb.CEmpDB()
        dictionary={"Emp Id": obj_ent.get_emp_id(),
                    "First Name": obj_ent.get_f_name(),
                    "Last Name": obj_ent.get_l_name(),
                    "Age": obj_ent.get_age(),
                    "Sex": obj_ent.get_sex(),
                    "Salary": obj_ent.get_salary()}
        print("Data for updation:", dictionary)
        option=input("Do you want to update this data?(Yes/No):").lower()
        if option=="yes":
            print("After updation the table emp:")
            obj_db.m_update_table(obj_ent)
        elif option =="no":
            print("Updation of data is not permitted.")
        else:
            print("Enter the valid option(Yes/No).")
    
    def mDelete_Data(self, obj_ent=Bent.CEmpEntities()):
        obj_db = Edb.CEmpDB()
        option = input("Do you want to update this data for employee Id ?(Yes/No):").lower()
        if option == "yes":
            print("Table after Deletion of record:")
            obj_db.m_delete_table(obj_ent)
        elif option == "no":
            print("Deletion of data is not permitted.")
        else:
            print("Enter the valid option(Yes/No).")
        
    def mRetrieval_Data(self):
        obj_db=Edb.CEmpDB()
        print("Data of emp table:")
        obj_db.m_retrieval_table()
        
    def mFilter_Data(self, obj_ent=Bent.CEmpEntities()):
        obj_db=Edb.CEmpDB()
        print("After filteration data:")
        obj_db.m_filter_table(obj_ent)