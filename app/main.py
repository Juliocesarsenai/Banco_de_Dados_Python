from services.usuario_service import UsuarioService
from repositories.usuario_repositories import UsuarioRepository
from config.database import Session
import os


def main():

    
    session=Session()
    repository=UsuarioRepository(session)
    service=UsuarioService(repository)


    while True:
        print("=======MENU========")
        print("1.Adicionar Usuário")
        print("2.Pesquisar Usuário")
        print("3.Atualizar Usuário")
        print("4.Excluir Usuário")
        print("5.Exibir todos os  Usuários")
        print("0.Sair")
        opcao=input("Selecione a opção que deseja: ")

        match opcao:
            case "1":
                print("\nAdicionando Usuario")
                nome=input("Digite seu nome: ")
                email=input("Digite seu email: ")
                senha=input("Digite sua senha: ")
                service.criar_usuario(nome=nome,email=email,senha=senha)

            case "2":
                print("Procurando Usuário")
                service.repository.pesquisar_usuario__por__email(email=str)
          
 
    

    #Listar todos os usuários cadastrados
        #print("\nListando todos os usuarios cadastrados.")
        #lista_usuarios=service.listar_todos_usuarios()

        #for usuario in lista_usuarios:
            #print(f"{usuario.nome} - {usuario.email} - {usuario.senha}")

if __name__ == "__main__":
    os.system("cls||clear")
    main()