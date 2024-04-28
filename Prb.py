from src.classes.User import User
from src.classes.Comment import Comment
from src.classes.Post import Post
from src.classes.DataBase import DataBase

usuario = User.register("fernando_zetina","fernando@gmail.com","123456", "Fernando", "Zetina",22,7,2003)
print(str(User.user_list[0]))
print("\n")
usuario.create_post("Hola este es mi primer post")
print(str(Post.post_list[0]))
print("\n")
usuario.send_like(Post.post_list[0].post_id)
print(str(Post.post_list[0]))

usuario.createComment(Post.post_list[0].post_id, "Hola estoy comentando una publicacion jejej")
print("\n")
print(str(Post.post_list[0].comments[0]))
comment = Comment.getComment(Post.post_list[0].comments[0].comment_id, Post.post_list[0].post_id)
print("\n")
Comment.edit_comment(Post.post_list[0].post_id,comment.comment_id,"Acabo de editar mi comentario")
print(str(comment))
print("\n")
print(str(Post.post_list[0].likes[0]))
print("\n")
print(str(usuario))

database = DataBase()
database.select_all_users()
print(str(User.user_list[0]))
while True:
    try:
        user_name = input("Please type [username]: ")
        if User.username_available(user_name) != -1:
            new_user = User.register(user_name, "fernando1234@gmail.com", "pepepecaspicapapas2", "Fernando", "Zetina", 22,7,2003)
            user_data = (new_user.user_id, new_user.username, new_user.email, new_user.password, new_user.first_name, new_user.last_name, new_user.dd_b, new_user.mm_b,
                    new_user.yy_b, new_user.biography, new_user.dd_r, new_user.mm_r, new_user.yy_r)
            database.insert_user(user_data)
            break
        else:
            print("[Error]: The entered username already exists, please try again.")
    except Exception as e:
        print("[Error]: ", str(e))