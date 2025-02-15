import pymssql


global constr, cursor
try:
    constr = pymssql.connect(
            server='LAPTOP-8T8MA06J\\SQLEXPRESS',  # Ensure the server and instance name is correct
            user='server',                         # Your SQL Server username
            password='',                      # Your SQL Server password
            database='TestDB'                     # Your database name
    )
    cursor = constr.cursor()
    cursor.execute("SELECT * from EMP")
    print("Connection successful!")
except pymssql.OperationalError as e:
    print(f"Connection failed: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
