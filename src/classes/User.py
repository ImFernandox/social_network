import time
import uuid
from .DataBase import DataBase

class User:
    database = DataBase()

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
        posts,
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

    def create_post(self, content):
        from .Post import Post

        Post.create_post(self.user_id, content)

    def createComment(self, post_id, content):
        from .Comment import Comment

        Comment.create_comment(self.user_id, post_id, content)

    def send_like(self, post_id):
        from .Post import Post
        from .Like import Like

        try:
            if Post.post_list and Post.getPost(post_id) != None:
                Like.create_like(self.user_id, post_id)
        except Exception as e:
            print("[Error]: ", str(e))

    def unlike(self, like_id, post_id):
        from .Post import Post
        from .Like import Like

        try:
            if Post.post_list and Post.getPost(post_id) != None:
                Like.delete_like(like_id, post_id)

        except Exception as e:
            print("[Error]: ", str(e))

    def change_password(self, old_password, new_password):
        try:
            return self.database.change_password(old_password, new_password, self.user_id)
        except Exception as e:
            print(str(e))

    def update_profile(
        self, username, email, first_name, last_name, dd_b, mm_b, yy_b, biography
    ):

        if username != "":
            self.username = username
            self.database.update_profile_db("username", username,self.user_id)
        if email != "":
            self.email = email
            self.database.update_profile_db("email", email, self.user_id)
        if first_name != "":
            self.first_name = first_name
            self.database.update_profile_db("first_name", first_name, self.user_id)
        if last_name != "":
            self.last_name = last_name
            self.database.update_profile_db("last_name", last_name, self.user_id)
        if dd_b != "":
            self.dd_b = dd_b
            self.database.update_profile_db("day_of_birth", dd_b, self.user_id)
        if mm_b != "":
            self.mm_b = mm_b
            self.database.update_profile_db("month_of_birth", mm_b, self.user_id)
        if yy_b != "":
            self.yy_b = yy_b
            self.database.update_profile_db("year_of_birth", yy_b, self.user_id)
        if biography != "":
            self.biographself = biography
            self.database.update_profile_db("biography", biography, self.user_id)
            print("a")

    def show_posts(self):
        aux = ""
        if self.posts != None:
            for post in self.posts:
                aux += str(post) + "\n"
        return aux

    @classmethod
    def generate_unique_user_id(cls):
        try:
            while True:
                user_id = str(uuid.uuid4())
                sql = "SELECT user_id FROM user WHERE user_id = %s"
                cls.database.cursor.execute(sql, (user_id,))
                result = cls.database.cursor.fetchone()
                if not result:
                    return user_id
        except Exception as e:
            print("[Error]: ", str(e))
            return None

    @classmethod
    def register(
        cls, username, email, password, first_name, last_name, dd_b, mm_b, yy_b
    ):
        try:
            if cls.username_available(username) != -1:
                actual_date = time.localtime()
                user_id = cls.generate_unique_user_id()
                posts = []
                dd_r = actual_date.tm_mday
                mm_r = actual_date.tm_mon
                yy_r = actual_date.tm_year
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
                cls.database.insert_user(user_data)
                print("[Registered Succesfully]")
                return new_user
            else:
                print("[Error]: Username is not available")
                return None
        except Exception as e:
            print("[Error]: ", str(e))

    @classmethod
    def login(cls, username, password):
        try:
            cls.database.login(username, password)
        except Exception as e:
            print("[Error]: ", str(e))

    @classmethod
    def getProfile(cls, user_id):
        try:
            return cls.database.getProfile(user_id)
        except Exception as e:
            print("[Error]: ", str(e))
            return None

    @classmethod
    def username_available(cls, username):
        try:
            return cls.database.username_available(username)
        except Exception as e:
            print(str(e))

    def __str__(self):

        user_info = f"First Name: {self.first_name}\nLast Name: {self.last_name}\nUsername: {self.username}\nE-mail: {self.email}\nPassword: {self.password}\nUser ID: {self.user_id}\nRegister Date: {self.dd_r}-{self.mm_r}-{self.yy_r}\nBirthday: {self.dd_b}-{self.mm_b}-{self.yy_b}\n"
        post_info = "Posts: \n\n" + self.show_posts()
        return user_info + post_info
