import sys
sys.path.append(
    "C:\\Users\\Anmol\\Desktop\\EmpCRUDapplication\\Bussiness_Entities")
sys.path.append(
    "C:\\Users\\Anmol\\Desktop\\EmpCRUDapplication\\Bussiness_Access_Layer")
import Table_Create_Entities as Tent
import TableBAL as Bal
obj_tent = Tent.C_Create_Table()

table_name = input("Enter the table name:")
obj_tent.set_table_name(table_name)

col1 = input("Enter the column-1:")
obj_tent.set_col1_name(col1)

col2 = input("Enter the column-2:")
obj_tent.set_col2_name(col2)

col3 = input("Enter the column-3:")
obj_tent.set_col3_name(col3)

col4 = input("Enter the column-4:")
obj_tent.set_col4_name(col4)

col4 = input("Enter the column-5:")
obj_tent.set_col4_name(col4)

col1_dt = input("Enter the data type of column-1:")
obj_tent.set_col1_data_type(col1_dt)

col2_dt = input("Enter the data type of column-2:")
obj_tent.set_col2_data_type(col2_dt)

col3_dt = input("Enter the data type of column-3:")
obj_tent.set_col3_data_type(col3_dt)

col4_dt = input("Enter the data type of column-4:")
obj_tent.set_col4_data_type(col4_dt)

col5_dt = input("Enter the data type of column-5:")
obj_tent.set_col5_data_type(col5_dt)

obj_bal = Bal.CTableBal()
obj_bal.m_Data_BAL(obj_tent)
