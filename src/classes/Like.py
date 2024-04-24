import time
import uuid
from .User import User
from .Post import Post

class Like: 
    list_id = []
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
            if User.user_exist(user_id) and Post.getPost(post_id) != None:
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
                    if not cls.list_id or like_id not in post.likes:
                        cls.list_id.append(like_id)
                        return like_id
            return None
        except Exception as e:
            print("[Error]: ", str(e))

    @classmethod
    def create_like(cls,user_id,post_id):
        try:
            if User.user_exist(user_id) and Post.getPost(post_id) != None:
                actual_date = time.localtime()
                like_id = Like.create_unique_like_id(user_id, post_id)
                post = Post.getPost(post_id)

                dd = actual_date.tm_mday
                mm = actual_date.tm_mon
                yy = actual_date.tm_year
                hh = actual_date.tm_hour
                mn = actual_date.tm_min

                new_like = Like(like_id,dd,mm,yy,hh,mn,user_id,post_id)
                post.likes.append(new_like)
        except Exception as e:
            print("[Error]: ", str(e))

    @classmethod
    def delete_like(cls, like_id, post_id):
        try:
            post = Post.getPost(post_id)
            if post.likes and cls.getLike(like_id, post_id) != None:
                like = cls.getLike(like_id, post_id)
                post.likes.remove(like)
                cls.list_id.remove(like.like_id)
        except Exception as e:
            print("[Error]: ", str(e))

    @classmethod
    def getLike(cls,like_id, post_id):
        try:
            post = Post.getPost(post_id)
            if post.likes:
                for like in post.likes:
                    if like.like_id == like_id:
                        return like 
                return None
            else:
                print("[Like not exist]")
                return None
        except Exception as e:
            print("[Error]: ", str(e))
            return None

    def __str__(self):
        return f"Like ID: {self.like_id}\nDate: {self.dd}-{self.mm}-{self.yy}\nTime: {self.hh}-{self.mn}\nUser ID: {self.user_id}\nPost ID: {self.post_id}"
    #elf, like_id, dd, mm, yy, hh, mn, user_id, post_id):