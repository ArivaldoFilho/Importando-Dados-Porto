portos = {}

def adicionar_porto():
    nome = input("Digite o nome do porto: ")
    localizacao = input("Digite a localização do porto: ")
    portos[nome] = {"Localização": localizacao}
    print("Porto adicionado com sucesso!")

def editar_porto():
    nome = input("Digite o nome do porto que deseja editar: ")
    if nome in portos:
        localizacao = input("Digite a nova localização do porto: ")
        portos[nome] = {"Localização": localizacao}
        print("Porto editado com sucesso!")
    else:
        print("O porto não existe!")

def listar_portos():
    if portos:
        print("Lista de Portos:")
        for nome, info in portos.items():
            print(f"Nome: {nome} | Localização: {info['Localização']}")
    else:
        print("Não há portos cadastrados!")

def deletar_porto():
    nome = input("Digite o nome do porto que deseja deletar: ")
    if nome in portos:
        del portos[nome]
        print("Porto deletado com sucesso!")
    else:
        print("O porto não existe!")

while True:
    print("Opções: 'incluir', 'editar', 'listar', 'deletar' ou 'sair'")
    opcao = input("Digite a operação que deseja realizar: ").lower()

    if opcao == "sair":
        print("Encerrando o programa...")
        break
    elif opcao == "incluir":
        adicionar_porto()
    elif opcao == "editar":
        editar_porto()
    elif opcao == "listar":
        listar_portos()
    elif opcao == "deletar":
        deletar_porto()
    else:
        print("Opção inválida!")