# this script creates the tables for the bronze layer
import psycopg2
password = input("input database password: ")

# connect to the database
conn = psycopg2.connect(database = "datawarehouse",  # change database name to the database we are working on
                        user = "postgres", 
                        host= 'localhost',
                        password = password,
                        port = 5432)

cur = conn.cursor()
conn.autocommit = True

# create schemas
cur.execute(
    '''
    CREATE SCHEMA bronze;
    '''
)
cur.execute(
    '''
    CREATE SCHEMA silver;
    '''
)
cur.execute(
    '''
    CREATE SCHEMA gold;
    '''
)

cur.execute(
    '''
    CREATE TABLE bronze.crm_cust_info(
        cst_id              INT,
        cst_key             VARCHAR(50),
        cst_firstname       VARCHAR(50),
        cst_lastname        VARCHAR(50),
        cst_marital_status  VARCHAR(10),
        cst_gndr            VARCHAR(10),
        cst_create_date     DATE
    );
    '''
)

cur.execute(
    '''
    CREATE TABLE bronze.crm_prd_info(
        prd_id INT,
        prd_key VARCHAR(50),
        prd_nm VARCHAR(50),
        prd_cost INT,
        prd_line VARCHAR(10),
        prd_start_dt DATE,
        prd_end_dt DATE
    );
    ''')

cur.execute(
    '''
    CREATE TABLE bronze.crm_sales_details(
        sls_ord_num VARCHAR(50),
        sls_prd_key VARCHAR(50),
        sls_cust_id INT,
        sls_order_dt INT,
        sls_ship_dt INT,
        sls_due_dt INT,
        sls_sales INT,
        sls_quantity INT,
        sls_price INT
    );
    '''
)

cur.execute(
    '''
    CREATE TABLE bronze.erp_cust_az12(
        cid VARCHAR(50),
        bdate DATE,
        gen VARCHAR(10)
    );
    '''
)

cur.execute(
    '''
    CREATE TABLE bronze.erp_loc_a101(
        cid VARCHAR(50),
        cntry VARCHAR(50)
    );
    '''
)

cur.execute(
    '''
    CREATE TABLE bronze.erp_px_cat_g1v2(
    id VARCHAR(50),
    cat VARCHAR(50),
    subcat VARCHAR(50),
    maintenance VARCHAR(50)
    );
    '''
)