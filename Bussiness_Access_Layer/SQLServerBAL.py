import Bussiness_Entities.Emp_Entities as Bent
import Data_Access_Layer.SQLServerDB as MS_DB

class CEmpBal:
    """Business Access Layer"""
    def mMSSQL_Server(self):
        obj_db = MS_DB.CSQLServerDB()
        obj_db.m_Connect_MSSQL()

    def mInsert_Data(self, obj_ent=Bent.CEmpEntities()):
        obj_db = MS_DB.CSQLServerDB()
        obj_db.m_Insert_Data(obj_ent)

    def mUpdate_Data(self, obj_ent=Bent.CEmpEntities()):
        obj_db = MS_DB.CSQLServerDB()
        obj_db.m_update_table(obj_ent)

    def mDelete_Data(self, obj_ent=Bent.CEmpEntities()):
        obj_db = MS_DB.CSQLServerDB()
        obj_db.m_delete_table(obj_ent)

    def mRetrieval_Data(self):
        obj_db = MS_DB.CSQLServerDB()
        obj_db.m_retrieval_table()

    def mFilter_Data(self, obj_ent=Bent.CEmpEntities()):
        obj_db = MS_DB.CSQLServerDB()
        obj_db.m_filter_table(obj_ent)

    def mAutomatic_emp_id(self):
        obj_db = MS_DB.CSQLServerDB()
        result=int(obj_db.m_automatically_emp_id())+1
        if result is not None:
            next_emp_id = result + 1
        else:
            next_emp_id = 1
        return next_emp_id

    def m_Automatic_commisssion(self, obj_ent=Bent.CEmpEntities()):
        comm=float(obj_ent.get_salary())
        level=int(obj_ent.get_level())
        if level==1:
            return comm*0.20
        elif level==2:
            return comm*0.15
        elif level==3:
            return comm*0.10
        else:
            return comm*0.05

    def m_data_retrieval(self, obj_ent=Bent.CEmpEntities()):
        obj_db=MS_DB.CSQLServerDB()
        obj_db.m_data_retrieval_col(obj_ent)