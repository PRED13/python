import pyodbc

# Configuración de conexión
server = 'PRED'  # Cambia si tu servidor tiene otro nombre
database = 'UFCManagement'
username = 'sa'
password = '123456'

def get_connection():
    try:
        conn = pyodbc.connect(
            f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
        )
        return conn
    except Exception as e:
        print("Error al conectar:", e)
        return None

def execute_query(query, params=()):
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
        cursor.close()
        conn.close()

def fetch_query(query, params=()):
    conn = get_connection()
    result = []
    if conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        result = cursor.fetchall()
        cursor.close()
        conn.close()
    return result
