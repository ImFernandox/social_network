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


    def select_all_users(self):
        from .User import User
        sql = 'SELECT*FROM user'

        try:
            self.cursor.execute(sql)
            users = self.cursor.fetchall()

            for user in users:
                user_id, username, email, password, first_name, last_name, dd_b, mm_b, yy_b, biography, dd_r, mm_r, yy_r = user
                user_obj = User(user_id, username, email, password, first_name, last_name, dd_b, mm_b, yy_b, biography, dd_r, mm_r, yy_r, None)
                User.user_list.append(user_obj)
        except Exception as e:
            raise
    
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
