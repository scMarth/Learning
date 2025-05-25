import pyodbc, os

server = os.environ['LOCAL_SQL_SERVER_NAME']
database = 'FamilyTree'  # Replace with your database name
username = os.environ['FAMILY_TREE_USER']  # Replace with your username
password = os.environ['FAMILY_TREE_PASSWORD']  # Replace with your password

# Create a connection string
conn_str = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

# Establish the connection
conn = pyodbc.connect(conn_str)

# Create a cursor to execute SQL queries
cursor = conn.cursor()

# Example: Execute a query
cursor.execute('SELECT * FROM MEMBERS')

# Fetch the results
results = cursor.fetchall()

# Do something with the results
for result in results:
    print(result)

# Close the cursor and connection
cursor.close()
conn.close()
