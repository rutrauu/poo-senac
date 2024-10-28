from sqlalchemy import create_engine, Column, Integer, String



from sqlalchemy.orm import sessionmaker,declarative_base

# Configurações do banco de dados
DATABASE_URL ="mysql+mysqlconnector://root:@localhost/usuarios"

# Criação do engine e da sessão
engine = create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine)

session = Session()

Base = declarative_base()


# Definição do modelo
class Usuario(Base):
    __tablename__ = 'usuario'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    senha=Column(String(50), nullable=False)
    e_mail=Column(String(50), nullable=False)
    age = Column(Integer, nullable=False)



# Função para inserir um novo usuário
def insert_Usuario(name, senha, e_mail, age):
    new_Usuario = Usuario(name=name,  senha=senha, e_mail=e_mail, age=age)
    session.add(new_Usuario)
    session.commit()
    print(f'Usuário {name} adicionado com sucesso!')


# Função para atualizar um usuário
def update_Usuario(name):
    usuario = session.query(Usuario).filter_by(name=name).first()
    if usuario:
        new_senha = input('Senha:')
        new_e_mail = input('E-mail:')
        new_age = int(input("Nova idade: "))

        usuario.age = new_age
        usuario.senha=new_senha
        usuario.e_mail=new_e_mail
        session.commit()
        print(f'Usuário {name} atualizado para a idade {new_age}.')
    else:
        print(f'Usuário {name} não encontrado.')

def update_Usuario_id(id):
    usuario = session.query(Usuario).filter_by(id=id).first()
    if usuario:
        new_name = input('Nome:')
        new_senha = input('Senha:')
        new_e_mail = input('E-mail:')
        new_age = int(input("Nova idade: "))
        usuario.name = new_name
        usuario.age = new_age
        usuario.senha=new_senha
        usuario.e_mail=new_e_mail
        session.commit()
        print(f'Usuário {id}  {new_name} atualizado para a idade {new_age}.')
    else:
        print(f'Usuário {id}   não encontrado.')




# Função para deletar um usuário
def delete_Usuario(name):
    usuario = session.query(Usuario).filter_by(name=name).first()
    if usuario:
        session.delete(usuario)
        session.commit()
        print(f'Usuário {name} deletado com sucesso.')
    else:
        print(f'Usuário {name} não encontrado.')

def delete_Usuario_id(id):
    usuario = session.query(Usuario).filter_by(id=id).first()
    user_name= usuario.name
    if usuario:
        session.delete(usuario)
        session.commit()
        print(f'Usuário {id} {user_name} deletado com sucesso.')
    else:
        print(f'Usuário {id} não encontrado.')

# Função para listar todos os usuários
def list_Usuarios():
    session = Session()
    all_Usuarios = session.query(Usuario).all()
    if all_Usuarios:
        for usuario in all_Usuarios:
            print(f'ID: {usuario.id}, Nome: {usuario.name}, senha: {usuario.senha}, e-mail: {usuario.e_mail}, Idade: {usuario.age} ')
    else:
        print('Nenhum usuário encontrado.')


# Função principal para interagir com o usuário
def main():
    while True:
        print("\nEscolha uma opção:")
        print("1. Adicionar usuário")
        print("2. Atualizar usuário")
        print("3. Deletar usuário")
        print("4. Listar usuários")
        print("5. Atualizar usuario por ID")
        print("6. Deletar usuário por ID")
        print("7. Sair")

        choice = input("Opção: ")

        if choice == '1':
            name = input("Nome do usuário: ")
            senha=input('Senha:')
            e_mail=input('E-mail:')
            age = int(input("Idade do usuário: "))
            insert_Usuario(name, senha, e_mail, age )
        elif choice == '2':
            list_Usuarios()
            name = input("Nome do usuário a ser atualizado: ")
            update_Usuario(name)
        elif choice == '3':
            list_Usuarios()
            name = input("Nome do usuário a ser deletado: ")
            delete_Usuario(name)
        elif choice == '4':
            list_Usuarios()
            input('[Enter] Continua!')
        elif choice == '5':
            list_Usuarios()
            id= int(input('ID do usuario para atualizar:'))
            update_Usuario_id(id)
        elif choice == '6':
            list_Usuarios()
            id = int(input("ID do usuário a ser deletado: "))
            delete_Usuario_id(id)
        elif choice == '7':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


# Execução do programa
if __name__ == "__main__":
    Base.metadata.create_all(engine)  # Cria a tabela se não existir
    main()
    session.close()