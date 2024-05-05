import time
import uuid
from .User import User
from .Post import Post
from classes_data_base.DataBaseLike import DataBaseLike


class Like:

    def __init__(self, like_id, dd, mm, yy, hh, mn, user_id, post_id):
        self.like_id = like_id
        self.dd = dd
        self.mm = mm
        self.yy = yy
        self.hh = hh
        self.mn = mn
        self.user_id = user_id
        self.post_id = post_id

    @classmethod
    def create_unique_like_id(cls, user_id, post_id):
        try:
            return DataBaseLike.create_unique_like_id(user_id, post_id)
        except Exception as e:
            print("[Error]: ", str(e))

    @classmethod
    def create_like(cls, user_id, post_id):
        try:
            if User.getProfile(user_id) is not None and Post.getPost(post_id) is not None:
                actual_date = time.localtime()
                dd = actual_date.tm_mday
                mm = actual_date.tm_mon
                yy = actual_date.tm_year
                hh = actual_date.tm_hour
                mn = actual_date.tm_min
                like_id = cls.create_unique_like_id(user_id, post_id)
                DataBaseLike.insert_like(like_id, dd, mm, yy, hh, mn, user_id, post_id)
                print("Like created successfully.")
        except Exception as e:
            print("[Error]: ", str(e))

    @classmethod
    def delete_like(cls, like_id, post_id):
        try:
            DataBaseLike.delete_like(like_id, post_id)
        except Exception as e:
            print("[Error]: ", str(e))

    @classmethod
    def get_like(cls, like_id, post_id):
        try:
            return DataBaseLike.get_like(like_id, post_id)
        except Exception as e:
            print("[Error]: ", str(e))
            return None

    def __str__(self):
        return f"Like ID: {self.like_id}\nDate: {self.dd}-{self.mm}-{self.yy}\nTime: {self.hh}-{self.mn}\nUser ID: {self.user_id}\nPost ID: {self.post_id}"