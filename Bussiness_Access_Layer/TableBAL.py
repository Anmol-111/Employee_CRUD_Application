import sys
sys.path.append("C:\\Users\\Anmol\\Desktop\\EmpCRUDapplication\\Bussiness_Entities")
sys.path.append("C:\\Users\\Anmol\\Desktop\\EmpCRUDapplication\\Data_Access_Layer")
import Table_Create_Entities as Bent
import TableDB as Tdb

class CTableBal:
    """Bussiness Access Layer For Table Creation."""
    def m_Data_BAL(self, obj_ent= Bent.C_Create_Table()):
        obj_db=Tdb.CTableDB()
        obj_db.m_Connect_SQL()
        obj_db.m_table_creation(obj_ent)