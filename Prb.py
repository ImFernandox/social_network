from src.classes.User import User
from src.classes.Comment import Comment
from src.classes.Post import Post

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