import pymssql
import Bussiness_Entities.Emp_Entities as Bent

class CSQLServerDB:
    """Employee Database connectivity Class."""
    def m_Connect_MSSQL(self):
        global constr, cursor
        constr=pymssql.connect(
                server='LAPTOP-8T8MA06J\SQLEXPRESS',
                user='root',
                password='Admin@1234',
                database='TestDB',
                as_dict = True
                )
        cursor = constr.cursor()

    def m_Insert_Data(self, obj_ent=Bent.CEmpEntities()):
        cursor.callproc("sp_insert_data", (obj_ent.get_emp_id(), obj_ent.get_f_name(),
                                           obj_ent.get_l_name(), obj_ent.get_age(),
                                           obj_ent.get_sex(), obj_ent.get_email_id(),
                                           obj_ent.get_phone_no(), obj_ent.get_department_id(),
                                           obj_ent.get_designation_id(), obj_ent.get_manager_id(),
                                           obj_ent.get_level(), obj_ent.get_salary(),
                                           obj_ent.get_commission()))
        constr.commit()
        cursor.execute("SELECT * FROM emp;")
        for data in cursor.fetchall():
            print(data)


    def m_update_table(self, obj_ent=Bent.CEmpEntities()):
        cursor.callproc("sp_update_data", (obj_ent.get_emp_id(), obj_ent.get_f_name(),
                                           obj_ent.get_l_name(), obj_ent.get_age(),
                                           obj_ent.get_sex(), obj_ent.get_email_id(),
                                           obj_ent.get_phone_no(), obj_ent.get_department_id(),
                                           obj_ent.get_designation_id(), obj_ent.get_manager_id(),
                                           obj_ent.get_level(), obj_ent.get_salary(),
                                           obj_ent.get_commission()))
        constr.commit()
        cursor.execute("SELECT * FROM emp;")
        for data in cursor.fetchall():
            print(data)

    def m_delete_table(self, obj_ent=Bent.CEmpEntities()):
        cursor.callproc("sp_retrievefilterdata", (obj_ent.get_emp_id(),))
        for data in cursor.fetchall():
            print(data)
        cursor.callproc("sp_delete_data", (obj_ent.get_emp_id(),))
        constr.commit()

    def m_retrieval_table(self):
        cursor.callproc("sp_retrieve_alldata")
        for data in cursor.fetchall():
            print(data)

    def m_filter_table(self, obj_ent=Bent.CEmpEntities()):
        cursor.callproc("sp_retrievefilterdata", (obj_ent.get_emp_id(),))
        for data in cursor.fetchall():
            print(data)

    def m_automatically_emp_id(self):
        cursor.callproc("sp_automatic_emp_id")
        data = cursor.fetchone()
        if data and data[0] is not None:
            return data[0]
        else:
            return 0

    def m_data_retrieval_col(self, obj_ent=Bent.CEmpEntities()):
        cursor.callproc("sp_data_retrieval", (obj_ent.get_column_name(),
                                              obj_ent.get_column_value()))
        for data in cursor.fetchall():
            print(data)

'''
import pyodbc
import Bussiness_Entities.Emp_Entities as Bent

class CSQLServerDB:
    """Employee Database connectivity Class."""
    def m_Connect_MSSQL(self):
        global constr, cursor
        constr = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'  
            'SERVER=LAPTOP-8T8MA06J\\SQLEXPRESS;'     
            'DATABASE=TestDB;'                        
            'Trusted_Connection=yes;'
                )
        cursor = constr.cursor()

    def m_Insert_Data(self, obj_ent=Bent.CEmpEntities()):
        cursor.execute("EXECUTE sp_insert_data ?,?,?,?,?,?,?,?,?,?,? ", (obj_ent.get_emp_id(), obj_ent.get_f_name(), obj_ent.get_l_name(), obj_ent.get_age(), obj_ent.get_sex(), obj_ent.get_email_id(), obj_ent.get_phone_no(), obj_ent.get_designation(), obj_ent.get_level(), obj_ent.get_salary(), obj_ent.get_commission()))
        constr.commit()
        cursor.execute("EXECUTE sp_retrieve_alldata")
        for data in cursor.fetchall():
            print(data)


    def m_update_table(self, obj_ent=Bent.CEmpEntities()):
        cursor.execute("EXECUTE sp_update_data ?,?,?,?,?,?,?,?,?,?,? ", (obj_ent.get_emp_id(), obj_ent.get_f_name(), obj_ent.get_l_name(), obj_ent.get_age(), obj_ent.get_sex(), obj_ent.get_email_id(), obj_ent.get_phone_no(), obj_ent.get_designation(), obj_ent.get_level(), obj_ent.get_salary(), obj_ent.get_commission()))
        constr.commit()
        cursor.execute("EXECUTE sp_retrieve_alldata")
        for data in cursor.fetchall():
            print(data)

    def m_delete_table(self, obj_ent=Bent.CEmpEntities()):
        cursor.execute("EXECUTE sp_retrievefilterdata ? ", (obj_ent.get_emp_id(),))
        for data in cursor.fetchall():
            print(data)
        cursor.execute("EXECUTE sp_delete_data ? ", (obj_ent.get_emp_id()))
        constr.commit()

    def m_retrieval_table(self):
        cursor.execute("EXECUTE sp_retrieve_alldata")
        for data in cursor.fetchall():
            print(data)

    def m_filter_table(self, obj_ent=Bent.CEmpEntities()):
        cursor.execute("EXECUTE sp_retrievefilterdata ? ", (obj_ent.get_emp_id()))
        for data in cursor.fetchall():
            print(data)

    def m_automatically_emp_id(self):
        cursor.execute("EXECUTE sp_automatic_emp_id")
        data = cursor.fetchone()
        return data[0]

    def m_data_retrieval_col(self, obj_ent=Bent.CEmpEntities()):
        cursor.execute("EXEC sp_data_retrieval ?,?,?,?,?", (obj_ent.get_emp_id(),obj_ent.get_phone_no(),obj_ent.get_email_id(),obj_ent.get_f_name(),obj_ent.get_l_name()))
        for data in cursor.fetchall():
            print(data)

'''