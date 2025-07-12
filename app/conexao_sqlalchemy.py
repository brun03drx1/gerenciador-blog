from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# - Importante:
""" 
 Antes de executar o projeto, edite os valores abaixo com as suas credenciais do 
 Banco PostgreSQL local (ou servidor, se estiver usando um).
"""

# Substitua pelos seus dados:
user = "seu_usuario_postgres"         # ex: postgres
password = "sua_senha_postgres"
host = "localhost"                    # padrão PostgresSQL
port = 5432                           # padrão PostgresSQL
database = "seu_database_exemplo"     # ex: db_blog

DATABASE_URL = f"postgresql://{user}:{password}@{host}:{port}/{database}"

engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()