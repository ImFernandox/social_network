import time
import uuid


class User:
    id_list = []
    user_list = []

    def __init__(
        self,
        user_id,
        username,
        email,
        password,
        name,
        lastname,
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
        self.name = name
        self.lastname = lastname
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
        if self.password == old_password:
            self.password = new_password
        else:
            print("[Error]: Incorrect password.")

    def update_profile(
        self, username, email, password, name, lastname, dd_b, mm_b, yy_b
    ):

        if username != "":
            self.username = username
        if email != "":
            self.email = email
        if password != "":
            self.password = password
        if name != "":
            self.name = name
        if lastname != "":
            self.lastname = lastname
        if dd_b != "":
            self.dd_b = dd_b
        if mm_b != "":
            self.mm_b = mm_b
        if yy_b != "":
            self.yy_b = yy_b

    def show_posts(self):
        aux = ""
        for post in self.posts:
            aux += str(post)+"\n"
        return aux
    
    @classmethod
    def generate_unique_user_id(cls):
        try:
            while True:
                user_id = str(uuid.uuid4())
                if not cls.id_list or user_id not in cls.id_list:
                    cls.id_list.append(user_id)
                    return user_id
        except Exception as e:
            print("[Error]: ", str(e))

    @classmethod
    def register(cls, username, email, password, name, lastname, dd_b, mm_b, yy_b):
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
                    name,
                    lastname,
                    dd_b,
                    mm_b,
                    yy_b,
                    "",
                    dd_r,
                    mm_r,
                    yy_r,
                    posts
                )
                cls.user_list.append(new_user)
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
            for user in cls.user_list:
                if user.username == username:
                    if user.password == password:
                        return True
            return False
        except Exception as e:
            print("[Error]: ", str(e))

    @classmethod
    def getProfile(cls, user_id):
        try:
            if cls.user_list:
                for user in cls.user_list:
                    if user.user_id == user_id:
                        return user
                return None
            else:
                print("[User not exist]")
                return None
        except Exception as e:
            print("[Error]: ", str(e))
            return None

    @classmethod
    def user_exist(cls, user_id):
        try:
            if cls.user_list:
                for user in cls.user_list:
                    if user.user_id == user_id:
                        return True
                return False
            else:
                print("[User not exist]")
                return False
        except Exception as e:
            print("[Error]: ", str(e))
            return False

    @classmethod
    def username_available(cls, username):
        if cls.user_list:
            for user in cls.user_list:
                if user.username == username:
                    return -1
            return 0
        else:
            return 0

    def __str__(self):
        
        user_info = f"Name: {self.name}\nLastname: {self.lastname}\nUsername: {self.username}\nE-mail: {self.email}\nPassword: {self.password}\nUser ID: {self.user_id}\nRegister Date: {self.dd_r}-{self.mm_r}-{self.yy_r}\nBirthday: {self.dd_b}-{self.mm_b}-{self.yy_b}\n"
        post_info = "Posts: \n\n" + self.show_posts()
        return user_info + post_info