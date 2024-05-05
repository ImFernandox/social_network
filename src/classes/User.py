import time
import uuid
from classes_data_base.DataBaseUser import DataBaseUser

class User:

    def __init__(
        self,
        user_id,
        username,
        email,
        password,
        first_name,
        last_name,
        dd_b,
        mm_b,
        yy_b,
        biography,
        dd_r,
        mm_r,
        yy_r,
        posts = None
    ):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.dd_b = dd_b
        self.mm_b = mm_b
        self.yy_b = yy_b
        self.biography = biography
        self.dd_r = dd_r
        self.mm_r = mm_r
        self.yy_r = yy_r
        self.posts = posts

    @classmethod
    def create_post(cls, user_id, content):
        from .Post import Post
        Post.create_post(user_id, content)

    @classmethod
    def create_comment(cls, user_id, post_id, content):
        from .Comment import Comment
        Comment.create_comment(user_id, post_id, content)

    @classmethod
    def send_like(cls, user_id, post_id):
        from .Like import Like
        Like.create_like(user_id, post_id)

    @classmethod
    def unlike(cls, like_id, post_id):
        from .Like import Like
        Like.delete_like(like_id, post_id)

    @classmethod
    def change_password(cls, user_id, old_password, new_password):
        return DataBaseUser.change_password(old_password, new_password, user_id)


    @classmethod
    def update_profile(cls, user_id, username, email, first_name, last_name, dd_b, mm_b, yy_b, biography):
        if username != "":
            DataBaseUser.update_profile_db("username", username, user_id)
        if email != "":
            DataBaseUser.update_profile_db("email", email, user_id)
        if first_name != "":
            DataBaseUser.update_profile_db("first_name", first_name, user_id)
        if last_name != "":
            DataBaseUser.update_profile_db("last_name", last_name, user_id)
        if dd_b != "":
            DataBaseUser.update_profile_db("day_of_birth", dd_b, user_id)
        if mm_b != "":
            DataBaseUser.update_profile_db("month_of_birth", mm_b, user_id)
        if yy_b != "":
            DataBaseUser.update_profile_db("year_of_birth", yy_b, user_id)
        if biography != "":
            DataBaseUser.update_profile_db("biography", biography, user_id)

    @classmethod
    def register(cls, username, email, password, first_name, last_name, dd_b, mm_b, yy_b):
        user_id = str(uuid.uuid4())
        posts = []
        dd_r = time.localtime().tm_mday
        mm_r = time.localtime().tm_mon
        yy_r = time.localtime().tm_year
        new_user = cls(
            user_id,
            username,
            email,
            password,
            first_name,
            last_name,
            dd_b,
            mm_b,
            yy_b,
            "",
            dd_r,
            mm_r,
            yy_r,
            posts,
        )
        user_data = (new_user.user_id, new_user.username, new_user.email, new_user.password, new_user.first_name, new_user.last_name, new_user.dd_b, new_user.mm_b,
        new_user.yy_b, new_user.biography, new_user.dd_r, new_user.mm_r, new_user.yy_r)
        DataBaseUser.insert_user(user_data)
        print("[Registered Succesfully]")
        return new_user

    @classmethod
    def login(cls, username, password):
        DataBaseUser.login(username, password)

    @classmethod
    def getProfile(cls, user_id):
        return DataBaseUser.getProfile(user_id)

    def show_posts(self):
        aux = ""
        if self.posts is not None:
            for post in self.posts:
                aux += str(post) + "\n"
        return aux

    @classmethod
    def generate_unique_user_id(cls):
        try:
            return DataBaseUser.generate_unique_user_id()
        except Exception as e:
            print("[Error]: ", str(e))

    @classmethod
    def username_available(cls, username):
        return DataBaseUser.username_available(username)

    def __str__(self):
        user_info = f"First Name: {self.first_name}\nLast Name: {self.last_name}\nUsername: {self.username}\nE-mail: {self.email}\nPassword: {self.password}\nUser ID: {self.user_id}\nRegister Date: {self.dd_r}-{self.mm_r}-{self.yy_r}\nBirthday: {self.dd_b}-{self.mm_b}-{self.yy_b}\n"
        post_info = "Posts: \n\n" + self.show_posts()
        return user_info + post_info