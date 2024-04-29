from src.classes.User import User
from src.classes.Comment import Comment
from src.classes.Post import Post
from src.classes.DataBase import DataBase

database = DataBase()

User.login("whosnano","pepepecaspicapapas")

while True:
    try:
        user_name = input("Please type [username]: ")
        if User.username_available(user_name) != -1:
            new_user = User.register(user_name, "fernando1234@gmail.com", "pepepecaspicapapas", "Fernando", "Zetina", 22,7,2003)
            break
        else:
            print("[Error]: The entered username already exists, please try again.")
    except Exception as e:
        print("[Error]: ", str(e))
