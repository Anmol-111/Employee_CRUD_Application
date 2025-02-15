import pymysql
import sys
sys.path.append(
    "C:\\Users\\Anmol\\Desktop\\EmpCRUDapplication\\Bussiness_Entities")
sys.path.append(
    "C:\\Users\\Anmol\\Desktop\\EmpCRUDapplication\\Bussiness_Access_Layer")
import Table_Create_Entities as Tent

class CTableDB:
    """Table Data Access Layer."""

    def m_Connect_SQL(self):
        global constr, cursor
        constr = pymysql.connect(
            host='localhost',
            user='root',
            password='root',
            database='testdb'
        )
        cursor = constr.cursor()

    def m_table_creation(self, obj_ent=Tent.C_Create_Table()):
        column = ''
        '''sql_create_table="CREATE TABLE"+str(obj_ent.get_table_name)+"("
        for detail in obj_ent.get_table_details():
            column_name,data_type=detail.split(":")
            column+=column_name+ " " + data_type + ","
        sql_create_table += column[:-1] + ")"'''
        data = cursor.execute('''
                            CREATE TABLE IF NOT EXISTS %s(%s %s, %s %s, %s %s, %s %s);
                            ''', (obj_ent.get_table_name(),
                                      obj_ent.get_col1_name(), obj_ent.get_col1_data_type(),
                                      obj_ent.get_col2_name(), obj_ent.get_col2_data_type(),
                                      obj_ent.get_col3_name(), obj_ent.get_col3_data_type(),
                                      obj_ent.get_col4_name(), obj_ent.get_col4_data_type(),
                                      obj_ent.get_col5_name(), obj_ent.get_col5_data_type()))
        constr.close()
