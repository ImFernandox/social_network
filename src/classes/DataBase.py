import pymysql 


class DataBase:

    def __init__(self):
        self.connection = pymysql.connect(
            host= 'localhost',
            user= 'root',
            password= '1234',
            db= 'social_network'
        )

        self.cursor = self.connection.cursor()
        print("Successfully Connection")

    
    def insert_user(self, user_data):
        sql  = """INSERT INTO user (user_id, username, email, user_password, first_name, last_name, day_of_birth,
                                   month_of_birth, year_of_birth, biography, day_of_registration, 
                                   month_of_registration, year_of_registration)
                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        
        try:
            self.cursor.execute(sql, user_data)
            self.connection.commit()
            print("User inserted successfully.")
        except Exception as e:
            self.connection.rollback()
            print("[Error]: ", str(e))

    def update_profile_db(self, variable, data, user_id):
        sql = f"""UPDATE user
                    SET {variable} = %s
                    WHERE user_id = %s;"""
        try:
            self.cursor.execute(sql, (data, user_id))
            self.connection.commit()
        except Exception as e:
            raise

    def login(self, username, password):
        sql = "SELECT * FROM user WHERE username = %s AND user_password = %s"
        self.cursor.execute(sql, (username, password))
        result = self.cursor.fetchone() 
        if result:
            print("Successfully Login")
            return result
        else:
            print("Incorrect Username or Password")
            return None
        
    def username_available(self , username):
        sql = "SELECT * FROM user WHERE username = %s"
        self.cursor.execute(sql, (username,))
        result = self.cursor.fetchone() 
        if result:
            return -1
        else:
            return 0   
        
    def getProfile(self, user_id):
        try:
            sql = "SELECT * FROM user WHERE user_id = %s"
            self.database.cursor.execute(sql, (user_id,))
            result = self.database.cursor.fetchone()
            
            if result:
                user = self(*result)
                return user
            else:
                print("[User not exist]")
                return None
        except Exception as e:
            print("[Error]: ", str(e))
            return None
    
    def change_password(self, old_password, new_password, user_id):
        try:
            sql = "SELECT user_id FROM user WHERE user_id = %s AND user_password = %s"
            self.database.cursor.execute(sql, (user_id, old_password))
            result = self.database.cursor.fetchone()
            
            if result:
                sql_update = "UPDATE user SET user_password = %s WHERE user_id = %s"
                self.database.cursor.execute(sql_update, (new_password, user_id))
                self.database.connection.commit() 
                self.password = new_password 
                print("Password changed successfully.")
            else:
                print("Incorrect password.")
        except Exception as e:
            print("[Error]: ", str(e))