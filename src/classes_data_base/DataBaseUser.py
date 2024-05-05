import uuid
from classes_data_base.Connect import Connect

class DataBaseUser:

    @staticmethod
    def insert_user(user_data):
        sql = """INSERT INTO user (user_id, username, email, user_password, first_name, last_name, day_of_birth,
                                   month_of_birth, year_of_birth, biography, day_of_registration, 
                                   month_of_registration, year_of_registration)
                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        try:
            Connect.cursor.execute(sql, user_data)
            Connect.connection.commit()
            print("User inserted successfully.")
        except Exception as e:
            Connect.connection.rollback()
            print("[Error]: ", str(e))
    
    @classmethod
    def generate_unique_user_id(cls):
        while True:
            user_id = str(uuid.uuid4())
            sql = "SELECT user_id FROM user WHERE user_id = %s"
            result = Connect.cursor.execute(sql, (user_id,))
            if not result:
                return user_id
            
    @staticmethod
    def update_profile_db(variable, data, user_id):
        sql = f"""UPDATE user
                    SET {variable} = %s
                    WHERE user_id = %s;"""
        try:
            Connect.cursor.execute(sql, (data, user_id))
            Connect.connection.commit()
        except Exception as e:
            raise

    @staticmethod
    def login(username, password):
        sql = "SELECT * FROM user WHERE username = %s AND user_password = %s"
        Connect.cursor.execute(sql, (username, password))
        result = Connect.cursor.fetchone()
        if result:
            print("Successfully Login")
            return result
        else:
            print("Incorrect Username or Password")
            return None

    @staticmethod
    def username_available(username):
        sql = "SELECT * FROM user WHERE username = %s"
        Connect.cursor.execute(sql, (username,))
        result = Connect.cursor.fetchone()
        if result:
            return -1
        else:
            return 0

    @staticmethod
    def getProfile(user_id):
        from classes.User import User
        try:
            sql = "SELECT * FROM user WHERE user_id = %s"
            Connect.cursor.execute(sql, (user_id,))
            result = Connect.cursor.fetchone()

            if result:
                user = User(*result)
                return user
            else:
                print("[User not exist]")
        except Exception as e:
            print("[Error]: ", str(e))
            return None

    @staticmethod
    def change_password(old_password, new_password, user_id):
        try:
            sql = "SELECT user_id FROM user WHERE user_id = %s AND user_password = %s"
            Connect.cursor.execute(sql, (user_id, old_password))
            result = Connect.cursor.fetchone()

            if result:
                sql_update = "UPDATE user SET user_password = %s WHERE user_id = %s"
                Connect.cursor.execute(sql_update, (new_password, user_id))
                Connect.connection.commit()
                print("Password changed successfully.")
            else:
                print("Incorrect password.")
        except Exception as e:
            print("[Error]: ", str(e))