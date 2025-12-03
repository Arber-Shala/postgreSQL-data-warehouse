# this script creates the database
import psycopg2
password = input("input database password: ")

# connect to the database
conn = psycopg2.connect(database = "postgres", 
                        user = "postgres", 
                        host= 'localhost',
                        password = password,
                        port = 5432)

cur = conn.cursor()
conn.autocommit = True


# cur.execute(
#     '''
#     IF EXISTS (SELECT 1 FROM sys.databases WHERE name = 'DataWarehouse')
#     BEGIN
#         ALTER DATABASE DataWarehouse SET SINGLE_USER WITH ROLLBACK IMMEDIATE;
#         DROP DATABASE DataWarehouse;
#     '''
# )

# create the database
cur.execute(
    '''
    CREATE DATABASE DataWarehouse
    '''
)