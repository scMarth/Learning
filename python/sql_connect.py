import pyodbc, os

username = os.environ['LOCAL_SQLEXPRESS_USER']
password = os.environ['LOCAL_SQLEXPRESS_PW']
sql_server = os.environ['LOCAL_SQLEXPRESS_SERVER']


# Define connection string
conn_str = (
    r"DRIVER={ODBC Driver 17 for SQL Server};"
    f"SERVER=192.168.1.30\SQLEXPRESS;"
    r"DATABASE=FamilyTree;"
    r"Trusted_Connection=no;"
    rf"UID={username};"
    rf"PWD={password};"
)

try:
    # Connect to the database
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()

    # Execute a query
    cursor.execute("SELECT * FROM Members")

    # Fetch and print results
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Clean up
    cursor.close()
    conn.close()

except Exception as e:
    print("Error connecting to the database:", e)
