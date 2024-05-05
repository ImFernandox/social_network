import uuid
from classes_data_base.Connect import Connect

class DataBasePost:

    @staticmethod
    def insert_post(post_data):
        sql = """INSERT INTO post (post_id, content, day_of_publication, month_of_publication,
                                    year_of_publication, hour_of_publication, minute_of_publication, user_id)
                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
        try:
            Connect.cursor.execute(sql, post_data)
            Connect.connection.commit()
            print("Post inserted successfully.")
        except Exception as e:
            Connect.connection.rollback()
            print("[Error]: ", str(e))
    
    @staticmethod
    def generate_unique_post_id(user_id):
        from classes.User import User
        try:
            if User.getProfile(user_id) is not None:
                user = User.getProfile(user_id)
                while True:
                    post_id = user.username + "-post=" + str(uuid.uuid4())
                    sql = "SELECT post_id FROM post WHERE post_id = %s"
                    result = Connect.cursor.execute(sql, (post_id,))
                    if not result:
                        return post_id
            return None
        except Exception as e:
            print("[Error-gupi]: ", str(e))

    @staticmethod
    def edit_post(post_id, new_content):
        try:
            post = Connect.getPost(post_id)
            if post is not None:
                post.content = new_content
                sql = "UPDATE post SET content = %s WHERE post_id = %s"
                Connect.cursor.execute(sql, (new_content, post_id))
                Connect.connection.commit()
                print("[Post Edited Successfully]")
            else:
                print("[Error]: Post not found")
        except Exception as e:
            print("[Error]: ", str(e))

    @staticmethod
    def delete_post(post_id, user_id):
        try:
            sql = "DELETE FROM post WHERE post_id = %s AND user_id = %s"
            Connect.cursor.execute(sql, (post_id, user_id))
            rows_deleted = Connect.cursor.rowcount

            if rows_deleted > 0:
                Connect.connection.commit()
                print("[Post Deleted Successfully]")
            else:
                print("[Error]: Post not found")
        except Exception as e:
            print("[Error]: ", str(e))

    @staticmethod
    def getPost(post_id):
        from classes.Post import Post
        try:
            sql = "SELECT * FROM post WHERE post_id = %s"
            Connect.cursor.execute(sql, (post_id,))
            result = Connect.cursor.fetchone()
            if result:
                return Post(*result)
            else:
                print("[Post not exist]")
                return None
        except Exception as e:
            print("[Error]: ", str(e))
            return None
        
    @staticmethod
    def get_posts_by_user(user_id):
        from classes.Post import Post
        try:
            sql = "SELECT * FROM post WHERE user_id = %s"
            Connect.cursor.execute(sql, (user_id,))
            posts_data = Connect.cursor.fetchall()
            posts = []
            for post_data in posts_data:
                post = Post(*post_data)
                posts.append(post)
            return posts
        except Exception as e:
            print("[Error]: ", str(e))
            return None