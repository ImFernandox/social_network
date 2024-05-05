import time
from .User import User
from .Post import Post
from classes_data_base.DataBaseComment import DataBaseComment

class Comment:

    def __init__(self, comment_id, content, dd, mm, yy, hh, mn, user_id, post_id):
        self.comment_id = comment_id
        self.content = content
        self.dd = dd
        self.mm = mm
        self.yy = yy
        self.hh = hh
        self.mn = mn
        self.user_id = user_id
        self.post_id = post_id

    @classmethod
    def create_comment(cls, user_id, post_id, content):
        try:
            if User.getProfile(user_id) is not None and Post.getPost(post_id) is not None:
                actual_date = time.localtime()
                comment_id = cls.create_unique_comment_id(user_id, post_id)
                dd = actual_date.tm_mday
                mm = actual_date.tm_mon
                yy = actual_date.tm_year
                hh = actual_date.tm_hour
                mn = actual_date.tm_min

                comment_data = (comment_id, content, dd, mm, yy, hh, mn, user_id, post_id)
                DataBaseComment.insert_comment(comment_data)
                print("[Comment Created Successfully]")
        except Exception as e:
            print("[Error]: ", str(e))

    @classmethod
    def create_unique_comment_id(cls, user_id, post_id):
        try:
           return DataBaseComment.create_unique_comment_id(user_id, post_id)
        except Exception as e:
            print("[Error]: ", str(e))

    @classmethod
    def edit_comment(cls, post_id, comment_id, new_content):
        try:
            DataBaseComment.edit_comment(post_id, comment_id, new_content)
        except Exception as e:
            print("[Error]: ", str(e))

    @classmethod
    def delete_comment(cls, comment_id, post_id):
        try:
            DataBaseComment.delete_comment(comment_id, post_id)
        except Exception as e:
            print("[Error]: ", str(e))

    @classmethod
    def get_comment(cls, comment_id, post_id):
        try:
            return DataBaseComment.get_comment(comment_id, post_id)
        except Exception as e:
            print("[Error]: ", str(e))
            return None
        
    def __str__(self):
        return f"Comment ID: {self.comment_id}\nContent: {self.content}\nPosting Date: {self.dd}-{self.mm}-{self.yy}\nTime: {self.hh}-{self.mn}\nUser ID: {self.user_id}\nPost ID: {self.post_id}"