

print("Olá usuário")
print("Seja bem-vindo")
nome = input("Qual o seu nome? ")

print("Seja bem-vindo,", nome)

senha_correta = "1234"
senha = input("Qual sua senha? ")

if senha == senha_correta:
    print("Senha correta")
else:
    print("Senha incorreta, tente novamente")
    senha = input("Digite novamente sua senha: ")

    if senha != senha_correta:
        print("Deseja clicar na opção 'Esqueci a senha'?")
        opcao = input("1 - Sim | 2 - Não: ")

        if opcao == "1":
            email = input("Digite seu email: ")
            print("Email enviado com sucesso!")
            nova_senha = input("Crie uma nova senha: ")
            confirmar = input("Confirmar nova senha? (1 - Sim | 2 - Não): ")

            if confirmar == "1":
                senha_correta = nova_senha
                print("Nova senha confirmada com sucesso!")
            else:
                print("Senha não confirmada.")
        else:
            print("Tente novamente mais tarde.")
    else:
        print("Senha correta na segunda tentativa!")
