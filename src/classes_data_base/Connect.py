import pymysql

class Connect:
    connection = None
    cursor = None

    @staticmethod
    def connect():
        try:
            Connect.connection = pymysql.connect(
                host='localhost',
                user='root',
                password='1234',
                db='social_network'
            )
            Connect.cursor = Connect.connection.cursor()
            print("Successfully connected to the database")
        except Exception as e:
            print("[Error]: ", str(e))

