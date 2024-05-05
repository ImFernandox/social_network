import time
from .User import User
from classes_data_base.DataBasePost import DataBasePost

class Post:

    def __init__(self, post_id, content, dd, mm, yy, hh, mn, user_id):
        self.post_id = post_id
        self.content = content
        self.dd = dd
        self.mm = mm
        self.yy = yy
        self.hh = hh
        self.mn = mn
        self.user_id = user_id

    @classmethod
    def create_post(cls, user_id, content):
        try:
            actual_date = time.localtime()
            user = User.getProfile(user_id)
            dd = actual_date.tm_mday
            mm = actual_date.tm_mon
            yy = actual_date.tm_year
            hh = actual_date.tm_hour
            mn = actual_date.tm_min
            
            if user is not None:
                post_id = cls.generate_unique_post_id(user_id)
                post_data = (post_id, content, dd, mm, yy, hh, mn, user_id)
                DataBasePost.insert_post(post_data)
                post = cls(post_id,content,dd,mm,yy,hh,mn,user_id)
                print("[Post Created Successfully]")
                return post
            else:
                print("[Error]: User does not exist")
                return None
        except Exception as e:
            print("[Error]: ", str(e))


    @classmethod
    def generate_unique_post_id(cls, user_id):
        try:
           return DataBasePost.generate_unique_post_id(user_id)
        except Exception as e:
            print("[Error-gupi]: ", str(e))

    @classmethod
    def edit_post(cls, post_id, new_content):
        try:
           DataBasePost.edit_post(post_id,new_content)
        except Exception as e:
            print("[Error]: ", str(e))

    @classmethod
    def delete_post(cls, post_id, user_id):
        try:
            DataBasePost.delete_post(post_id, user_id)
        except Exception as e:
            print("[Error]: ", str(e))

    @classmethod
    def getPost(cls, post_id):
        try:
            return DataBasePost.getPost(post_id)
        except Exception as e:
            print("[Error]: ", str(e))
            return None

    def __str__(self):
        return f"Post ID: {self.post_id}\nContent: {self.content}\nPosting Date: {self.dd}-{self.mm}-{self.yy}\nUser ID: {self.user_id}\nLikes: {DataBasePost.get_likes_by_post(self.post_id)}\nComments: {len(DataBasePost.get_comments_by_post(self.post_id))}"