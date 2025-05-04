usuario = "admin"
senha = "1234"
tentativas_incorretas = 0
alteracoes_de_credenciais = 0

#boas vindas
boas_vindas = ""
idade = ""
descricao = ""

def alterar_usuario_senha():
    global usuario, senha, alteracoes_de_credenciais, tentativas_incorretas

    usuario = input("Novo usuário: ")
    senha = input("Nova senha: ")
    tentativas_incorretas = 0
    alteracoes_de_credenciais +=1
    print("Usuário e senha atualizados com sucesso!\n")

def login():
    global tentativas_incorretas
    while True:
        usuario_input = input("Digite seu usuário: ")
        senha_input = input("Digite sua senha: ")

        if usuario_input == usuario and senha_input == senha:
            print("Credencias corretas!")
            break
        else:
            tentativas_incorretas +=1
            print("Credenciais incorretas tente novamente")

def menu():
    while True:
        try:
            print("=== MENU ===")
            print("a) - Consultar tentativas incorretas")
            print("b) - Alterar usuário e senha")
            print("c) - Adicionar Boas vindas")
            print("d) - Cadastrar idade e descrição")
            print("e) - Exibir perfil completo")
            print("f) - Encerrar sistema")

            opcao = input("Digite a opção").lower()

            if opcao == "a":
                print(f"Tentativas Incorretas: {tentativas_incorretas}")
            
            elif opcao == "b":
                alterar_usuario_senha() # chamando a função
            
            elif opcao == "c":
                global boas_vindas
                boas_vindas = input("Adicione mensagem de boas vindas")
                print("Mensagem salva")
            
            elif opcao == "d":
                global idade, descricao
                idade = input("Digite sua idade: ")
                descricao = input("Digite uma descrição sobre você: ")
                print("Informações salvas!")

            elif opcao == "e":
                print("=== Perfil do Usuário ===")
                print(f"Nome de boas-vindas: {boas_vindas}")
                print(f"Idade: {idade}")
                print(f"Descrição: {descricao}")
                print(f"Alterações de Credenciais Realizadas: {alteracoes_de_credenciais}")

            elif opcao == "f":
                print("Encerrando sistema")
                break
            else:
                print("Opção inválida, tente novamente. \n")
        
        except KeyboardInterrupt:
            print("Interrupção detecada. Encerrando o sistema com segurança")
            break

login()
menu()