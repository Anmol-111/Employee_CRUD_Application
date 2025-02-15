import pymysql
import Bussiness_Entities.Emp_Entities as Bent

class CMySQLDB:
    """Employee Database connectivity Class."""
    def m_Connect_mySQL(self):
        global constr, cursor
        constr = pymysql.connect(
            host='localhost',
            user='root',
            password='root',
            database='testdb'
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
        data=cursor.fetchone()
        return data[0]

    def m_data_retrieval_col(self, obj_ent=Bent.CEmpEntities()):
        cursor.callproc("sp_data_retrieval", (obj_ent.get_column_name(), obj_ent.get_column_value()))
        for data in cursor.fetchall():
            print(data)