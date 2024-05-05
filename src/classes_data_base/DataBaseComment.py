import uuid
from classes_data_base.Connect import Connect

class DataBaseComment:    

    @staticmethod
    def insert_comment(comment_data):
        try:
            sql = """INSERT INTO comment (comment_id, content, day_of_publication, month_of_publication,
                     year_of_publication, hour_of_publication, minute_of_publication, user_id, post_id)
                     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            Connect.cursor.execute(sql, comment_data)
            Connect.connection.commit()
            print("Comment inserted successfully.")
        except Exception as e:
            Connect.connection.rollback()
            print("[Error]: ", str(e))

    @staticmethod
    def create_unique_comment_id(user_id, post_id):
        from classes.Post import Post
        from classes.User import User

        try:
            if User.getProfile(user_id) and Post.getPost(post_id) is not None:
                while True:
                    user = User.getProfile(user_id)
                    post = Post.getPost(post_id)
                    comment_id = (
                        user.username
                        + "-comment="
                        + str(uuid.uuid4())
                        + "-"
                        + post.post_id
                    )
                    sql = "SELECT comment_id FROM comment WHERE comment_id = %s"
                    result = Connect.cursor.execute(sql, (comment_id,))
                    if result == 0:
                        return comment_id
            return None
        except Exception as e:
            print("[Error]: ", str(e))

    @staticmethod
    def edit_comment(post_id, comment_id, new_content):
        try:
            comment = DataBaseComment.get_comment(comment_id, post_id)
            if comment is not None:
                sql = "UPDATE comment SET content = %s WHERE comment_id = %s AND post_id = %s"
                Connect.cursor.execute(sql, (new_content, comment_id, post_id))
                Connect.connection.commit()
                print("[Comment Edited Successfully]")
            else:
                print("[Error]: Comment not found")
        except Exception as e:
            print("[Error]: ", str(e))

    @staticmethod
    def delete_comment(comment_id, post_id):
        try:
            comment = DataBaseComment.get_comment(comment_id, post_id)
            if comment is not None:
                sql = "DELETE FROM comment WHERE comment_id = %s AND post_id = %s"
                Connect.cursor.execute(sql, (comment_id, post_id))
                Connect.connection.commit()
                print("[Comment Deleted Successfully]")
            else:
                print("[Error]: Comment not found")
        except Exception as e:
            print("[Error]: ", str(e))

    @staticmethod
    def get_comment(comment_id, post_id):
        from classes.Comment import Comment
        try:
            sql = "SELECT * FROM comment WHERE comment_id = %s AND post_id = %s"
            Connect.cursor.execute(sql, (comment_id, post_id))
            comment_data = Connect.cursor.fetchone()

            if comment_data:
                comment = Comment(*comment_data)
                return comment
            else:
                print("[Comment not exist]")
                return None
        except Exception as e:
            print("[Error]: ", str(e))
            return None

    @staticmethod
    def get_comments_by_post(post_id):
        from classes.Comment import Comment
        try:
            sql = "SELECT * FROM comment WHERE post_id = %s"
            Connect.cursor.execute(sql, (post_id,))
            comments_data = Connect.cursor.fetchall()

            comments = []
            for comment_data in comments_data:
                comment = Comment(*comment_data)
                comments.append(comment)
            return comments
        except Exception as e:
            print("[Error]: ", str(e))