import psycopg2


hostname =  'localhost'
database = 'demo'
username = 'postgres'
pwd = 'vks881576' 
port_id = 5432
conn = None,
cur = None

sql_file = 'output.sql'


try:
    conn = psycopg2.connect(
                host = hostname,
                dbname = database,
                user = username,
                password = pwd,
                port = port_id,
    

    )

    cur = conn.cursor()

    script =    '''CREATE TABLE Coffee_Sales (
    date DATE,
    datetime TIMESTAMP,
    cash_type VARCHAR(50),  -- Adjust the size based on your data requirements
    card VARCHAR(50),       -- Adjust the size based on your data requirements
    money NUMERIC(10, 2),   -- Adjust precision and scale as per your data
    coffee_name VARCHAR(100)  -- Adjust the size based on your data requirements
    );

    '''

    # script01 = '''-- Insert values into the employee table
    # INSERT INTO employee (id, name, salary, dept_id) VALUES
    # (1, 'John Doe', 50000, 'HR'),
    # (2, 'Jane Smith', 60000, 'Finance'),
    # (3, 'Robert Brown', 55000, 'IT'),
    # (4, 'Emily Davis', 62000, 'Marketing'),
    # (5, 'Michael Wilson', 58000, 'Sales');
    # '''
    cur.execute(script)

    ## Read SQL statment from file
    # with open(sql_file, 'r') as file:
    #     sql_commands = file.read().split(';')

    # ## Execute each command 
    # for command in sql_commands:
    #     if command.strip() != "":
    #         cur.execute(command)


    
    ## Commit the transaction 
    conn.commit()
    print("SQL commands executed sucessfully")

    


except Exception as error:
    print(error)

finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()

    







