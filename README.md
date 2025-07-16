# 🚀 Gerenciador de Blog CLI

> Um app de terminal em Python para gerenciar usuários e posts em PostgreSQL usando Python & SQLAlchemy.

[![Python 3.7+](https://img.shields.io/badge/python-3.7%2B-blue)]()
[![License: MIT](https://img.shields.io/badge/license-MIT-green)]()

---

## 📁 Estrutura do Projeto

gerenciador-blog/
├── app/
│   ├── __init__.py
│   ├── Blog.py            
│   ├── conexao_sqlalchemy.py  # Configuração de conexão (placeholders)
│   ├── Post.py            
│   └── User.py           
├── App.py                 
├── requirements.txt      
└── README.md              

---

## ⚡️ Funcionalidades

- ➕ Criar / listar usuários  
- 📝 Criar / listar posts  
- 🔄 Relacionamento usuário ↔ posts  
- 🖥️ Interface interativa no terminal

---

## ⚙️ Quick Start  
Siga estes passos para rodar o projeto localmente:

1. Clone o repositório:  
```bash
git clone https://github.com/seu-usuario/gerenciador-blog.git
```

2.	Entre na pasta do projeto:
```bash
cd Projeto II - Gerenciamento de Blog
```

3.	(Opcional) Crie e ative um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

4.	Instale as dependências:
```bash
pip install -r requirements.txt
```

5.	Configure a conexão com o banco:

	•	Abra a/conexao_sqlalchemy.py
	•	Substitua os placeholders:
     user = "seu_usuario"      # ex: postgres
     password = "sua_senha"    # sua senha
     host = "localhost"        # padrão
     port = 5432               # padrão
     database = "nome_do_db"   # ex: blog

6.	Execute a aplicação:
```bash
python App.py
```

7.	Use o menu
  Selecione as opções:
  1. Adicionar usuário  
  2. Adicionar post  
  3. Listar usuários e posts  
  4. Sair

---

## 📄 Licença

MIT © Bruno Eduardo 
