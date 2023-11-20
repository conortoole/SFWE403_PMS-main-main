import mysql.connector

def Connect():
    conn = None

    try:
        conn = mysql.connector.connect(
            host = 'mysql-145311-0.cloudclusters.net',
            port = '18166',
            user = 'admin',
            passwd = 'FcCZds4d',
            db = 'PMS'
    )
    except:
        print('Error Connecting to Database')

    finally:
        return conn