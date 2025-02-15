import pymysql
import pyodbc
import Bussiness_Entities.Emp_Entities as Bent

class CEmpDB:
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

    def m_Connect_MSSQL(self):
        global constr, cursor
        server_name='LAPTOP-8T8MA06J\SQLEXPRESS'
        database_name='TestDB'
        constr = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=' + server_name + ';'
            'DATABASE=' + database_name + ';'
            'Trusted_Connection=yes;'
        )
        cursor = constr.cursor()

    def m_Insert_Data(self, obj_ent=Bent.CEmpEntities()):
        query='''
                EXECUTE sp_insert_data ?,?,?,?,?,? 
                '''
        val=(obj_ent.get_emp_id(), obj_ent.get_f_name(), obj_ent.get_l_name(), obj_ent.get_age(), obj_ent.get_sex(), obj_ent.get_salary())
        cursor.execute(query, val)
        constr.commit()
        # constr.close()

    def m_update_table(self, obj_ent=Bent.CEmpEntities()):
        cursor.execute('''
               EXECUTE sp_update_data ?,?,?,?,?,?
                ''', (obj_ent.get_emp_id(), obj_ent.get_f_name(), obj_ent.get_l_name(), obj_ent.get_age(), obj_ent.get_sex(), obj_ent.get_salary()))
        print("Data updation is successfull.")
        constr.commit()
        #constr.close()

    def m_delete_table(self, obj_ent=Bent.CEmpEntities()):
        cursor.execute('''A
                        EXECUTE sp_retrievefilterdata ?;
                        ''', (obj_ent.get_emp_id()))
        for data in cursor.fetchall():
            print(data)
        cursor.execute('''
                EXECUTE sp_delete_data ?;
                ''', (obj_ent.get_emp_id()))
        constr.commit()
        #constr.close()

    def m_retrieval_table(self):
        cursor.execute('''
                EXECUTE sp_retrieve_alldata;
                ''')
        for data in cursor.fetchall():
            print(data)
        #constr.close()

    def m_filter_table(self, obj_ent=Bent.CEmpEntities()):
        cursor.execute('''
                EXECUTE sp_retrievefilterdata(?);
                ''', (obj_ent.get_emp_id()))
        for data in cursor.fetchall():
            print(data)
        #constr.close()
