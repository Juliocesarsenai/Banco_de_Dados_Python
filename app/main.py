from services.usuario_service import UsuarioService
from repositories.usuario_repositories import UsuarioRepository
from config.database import Session
import os
def main():

    
    session=Session()
    repository=UsuarioRepository(session)
    service=UsuarioService(repository)

    #Solicitando dados para o usuario
    print("\nAdicionando Usuario")
    nome=input("Digite seu nome: ")
    email=input("Digite seu email: ")
    senha=input("Digite sua senha: ")

    
    service.criar_usuario(nome=nome,email=email,senha=senha)

    #Listar todos os usuários cadastrados
    print("\nListando todos os usuarios cadastrados.")
    lista_usuarios=service.listar_todos_usuarios()

    for usuario in lista_usuarios:
        print(f"{usuario.nome} - {usuario.email} - {usuario.senha}")

if __name__ == "__main__":
    os.system("cls||clear")
    main()