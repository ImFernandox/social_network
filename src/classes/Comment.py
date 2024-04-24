import time
import uuid
from .User import User
from .Post import Post


class Comment:
    list_id = []

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
    def create_unique_comment_id(cls, user_id, post_id):
        try:
            if User.user_exist(user_id) and Post.getPost(post_id) != None:
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
                    if not cls.list_id or comment_id not in post.comments:
                        cls.list_id.append(comment_id)
                        return comment_id
            return None
        except Exception as e:
            print("[Error]: ", str(e))

    @classmethod
    def create_comment(cls, user_id, post_id, content):
        if User.user_exist(user_id) and Post.getPost(post_id) != None:
            actual_date = time.localtime()
            comment_id = Comment.create_unique_comment_id(user_id, post_id)
            post = Post.getPost(post_id)
            
            dd = actual_date.tm_mday
            mm = actual_date.tm_mon
            yy = actual_date.tm_year
            hh = actual_date.tm_hour
            mn = actual_date.tm_min

            new_comment = Comment(
                comment_id, content, dd, mm, yy, hh, mn, user_id, post_id
            )  
            post.comments.append(new_comment)


    @classmethod
    def edit_comment(cls,post_id,comment_id, new_content):
        try:
            if cls.getComment(comment_id,post_id) != None and Post.getPost(post_id) != None:
                comment = cls.getComment(comment_id,post_id)

                comment.content = new_content
        except Exception as e:
            print("[Error]: ", str(e))

    @classmethod
    def delete_comment(cls,comment_id, post_id):
        try:
            post = Post.getPost(post_id)
            if post.comments and cls.getComment(comment_id, post_id) != None:
                comment = cls.getComment(comment_id, post_id)
                post.comments.remove(comment)
                cls.list_id.remove(comment.comment_id)
        except Exception as e:
            print("[Error]: ", str(e))

    @classmethod
    def getComment(cls,comment_id, post_id):
        try:
            post = Post.getPost(post_id)
            if post.comments:
                for comment in post.comments:
                    if comment.comment_id == comment_id:
                        return comment
                return None
            else:
                print("[Comment not exist]")
                return None
        except Exception as e:
            print("[Error]: ", str(e))
            return None

    def __str__(self):
        return F"Comment ID: {self.comment_id}\nContent: {self.content}\nPosting Date: {self.dd}-{self.mm}-{self.yy}\nTime: {self.hh}-{self.mn}\nUser ID: {self.user_id}\nPost ID: {self.post_id}"
    