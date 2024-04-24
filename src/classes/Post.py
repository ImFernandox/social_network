import uuid
import time
from .User import User


class Post:
    list_id = []
    post_list = []

    def __init__(self, post_id, content, dd, mm, yy, hh, mn, user_id, likes, comments):
        self.post_id = post_id
        self.content = content
        self.dd = dd
        self.mm = mm
        self.yy = yy
        self.hh = hh
        self.mn = mn
        self.user_id = user_id
        self.likes = likes 
        self.comments = comments 

    @classmethod
    def create_post(cls,user_id, content):
        actual_date = time.localtime()
        comments = []
        likes = []
        dd = actual_date.tm_mday
        mm = actual_date.tm_mon
        yy = actual_date.tm_year
        hh = actual_date.tm_hour
        mn = actual_date.tm_min
        if User.user_exist(user_id):
            post_id = cls.generate_unique_post_id(user_id)
            new_post = cls(post_id, content, dd, mm, yy, hh, mn, user_id, likes, comments)
            cls.post_list.append(new_post)


    @classmethod
    def generate_unique_post_id(cls, user_id):
        try:
            if User.user_exist(user_id):
                user = User.getProfile(user_id)
                while True:
                    post_id = user.username + "-post=" + str(uuid.uuid4())
                    if not Post.list_id or post_id not in Post.list_id:
                        Post.list_id.append(post_id)
                        return post_id
            return None
        except Exception as e:
            print("[Error-gupi]: ", str(e))

    @classmethod
    def edit_post(cls, post_id, new_content):
        try:
            if cls.getPost(post_id) != None:
                post = cls.getPost(post_id)
                post.content = new_content
        except Exception as e:
            print("[Error]: ", str(e))

    @classmethod
    def delete_post(cls, post_id):
        try:
            if cls.post_list and cls.getPost(post_id) != None:
                post = cls.getPost(post_id)
                cls.post_list.remove(post)
                cls.list_id.remove(post.post_id)
        except Exception as e:
            print("[Error]: ", str(e))

    @classmethod
    def getPost(cls, post_id):
        try:
            if cls.post_list:
                for post in cls.post_list:
                    if post.post_id == post_id:
                        return post
                return None
            else:
                print("[Post not exist]")
                return None
        except Exception as e:
            print("[Error]: ", str(e))
            return None

    def __str__(self):
        return f"Post ID: {self.post_id}\nContent: {self.content}\nPosting Date: {self.dd}-{self.mm}-{self.yy}\nUser ID: {self.user_id}\nLikes: {len(self.likes)}\nComments: {len(self.comments)}"
