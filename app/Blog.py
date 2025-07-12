from conexao_sqlalchemy import Base, engine, session
from User import User 
from Post import Post

Base.metadata.create_all(engine)

# Função para exibir o menu de opções
def show_menu():
    print("Menu de Opções: \n")
    print("1. Cadastrar Usuário \n")
    print("2. Adicionar Post \n")
    print("3. Listar Usuários e Posts \n")
    print("4. Sair \n")
    
# Função para cadastrar usuário
def add_user():
    print("Cadastrar Usuário: \n")
    name = input("Digite o nome do usuário: \n")
    email = input("Digite o email do usuário: \n")
    user = User(name, email)
    session.add(user)
    session.commit()
    print(f"Usuário {name} cadastrado com sucesso! \n")
    
# Função para adicionar novo post
def add_post():
    print("Adicionar Novo Post: \n")
    title = input("Digite o título do post: \n")
    content = input("Digite o conteúdo do post: \n")
    author_id = input("Digite o id do autor do post: \n")
    user = session.query(User).filter_by(id=author_id).first()
    if user:
        post =Post(title=title, content=content, author=user)
        session.add(post)
        session.commit()
        print("Post adicionado com sucesso! \n")
    
    else:
        print("Usuário não encontrado! \n")
        
# Função para consultar usuários e posts
def query_users_posts():
    users = session.query(User).join(User.posts).order_by(User.name).all()
    for user in users:
        print(f"User: {user.name}, Email: {user.email}")
        for post in user.posts:
            print(f"Post: {post.title}, Conteúdo: {post.content}")