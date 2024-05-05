import uuid
from classes_data_base.Connect import Connect

class DataBaseLike:

    @staticmethod
    def insert_like(like_id, day_of_send, month_of_send, year_of_send, hour_of_send, minute_of_send, user_id,
                    post_id):
        try:
            sql = """INSERT INTO user_like (like_id, day_of_send, month_of_send, year_of_send,
                     hour_of_send, minute_of_send, user_id, post_id)
                     VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
            Connect.cursor.execute(sql, (
            like_id, day_of_send, month_of_send, year_of_send, hour_of_send, minute_of_send, user_id, post_id))
            Connect.connection.commit()
            print("Like inserted successfully.")
        except Exception as e:
            Connect.connection.rollback()
            print("[Error]: ", str(e))

    @staticmethod
    def create_unique_like_id(user_id, post_id):
        from classes.Post import Post
        from classes.User import User

        try:
            if User.getProfile(user_id) is not None and Post.getPost(post_id) is not None:
                while True:
                    user = User.getProfile(user_id)
                    post = Post.getPost(post_id)
                    like_id = (
                        user.username
                        + "-like="
                        + str(uuid.uuid4())
                        + "-"
                        + post.post_id
                    )

                    sql = "SELECT like_id FROM user_like WHERE like_id = %s"
                    result = Connect.cursor.execute(sql, (like_id,))
                    if result == 0:
                        return like_id
            return None
        except Exception as e:
            print("[Error]: ", str(e))

    @staticmethod
    def delete_like(like_id, post_id):
        try:
            if Connect.get_like(like_id, post_id) is not None:
                sql = "DELETE FROM user_like WHERE like_id = %s AND post_id = %s"
                Connect.cursor.execute(sql, (like_id, post_id))
                Connect.connection.commit()
                print("Like deleted successfully.")
        except Exception as e:
            print("[Error]: ", str(e))

    @staticmethod
    def get_like(like_id, post_id):
        from classes.Like import Like
        try:
            sql = "SELECT * FROM user_like WHERE like_id = %s AND post_id = %s"
            Connect.cursor.execute(sql, (like_id, post_id))
            like_data = Connect.cursor.fetchone()

            if like_data:
                like = Like(*like_data)
                return like
            else:
                print("[Like not exist]")
                return None
        except Exception as e:
            print("[Error]: ", str(e))

    @staticmethod
    def get_likes_by_post(post_id):
        from classes.Like import Like

        try:
            sql = "SELECT * FROM user_like WHERE post_id = %s"
            Connect.cursor.execute(sql, (post_id,))
            likes_data = Connect.cursor.fetchall()

            likes = []
            for like_data in likes_data:
                like = Like(*like_data)
                likes.append(like)
            return likes
        except Exception as e:
            print("[Error]: ", str(e))