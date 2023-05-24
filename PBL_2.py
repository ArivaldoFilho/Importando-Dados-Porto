portos = {
    "Suape": {"estado": "PE", "autoridade portuária": "Administração do Porto de Suape", "tipo": "marítimo"},
    "Imbituba": {"estado": "SC", "autoridade portuária": "SCPAR", "tipo": "marítimo"},
    "Laguna": {"estado": "SC", "autoridade portuária": "SCPAR", "tipo": "marítimo"},
    "São Francisco do Sul": {"estado": "SC", "autoridade portuária": "SCPAR", "tipo": "marítimo"},
    "Cabedelo": {"estado": "PB", "autoridade portuária": "Docas-PB", "tipo": "marítimo"},
    "Recife": {"estado": "PE", "autoridade portuária": "Porto de Recife S.A.", "tipo": "marítimo"},
    "São Sebastião": {"estado": "SP", "autoridade portuária": "Companhia das Docas de São Sebastião", "tipo": "marítimo"},
    "Antonina": {"estado": "PR", "autoridade portuária": "Administração dos Portos de Paranaguá e Antonina", "tipo": "marítimo"},
    "Pelotas": {"estado": "SC", "autoridade portuária": "Porto RS", "tipo": "marítimo"},
    "Porto Alegre": {"estado": "RS", "autoridade portuária": "Porto RS", "tipo": "marítimo"},
    "Rio Grande": {"estado": "RS", "autoridade portuária": "Porto RS", "tipo": "marítimo"},
    "Porto Velho": {"estado": "RO", "autoridade portuária": "Sociedade de Portos e Hidrovias do Estado de RO", "tipo": "fluvial"},
    "Itajaí": {"estado": "SC", "autoridade portuária": "SPI", "tipo": "marítimo"},
    "Macapá": {"estado": "AP", "autoridade portuária": "Companhia das Docas de Santana", "tipo": "marítimo"},
    "Forno": {"estado": "RJ", "autoridade portuária": "Companhia Municipal de Administração Portuária", "tipo": "marítimo"},
    "Santos": {"estado": "SP", "autoridade portuária": "Companhia Docas do Estado de São Paulo", "tipo": "marítimo"},
    "Paranaguá": {"estado": "PR", "autoridade portuária": "Administração dos Portos de Paranaguá e Antonina", "tipo": "marítimo"},
    "Itaqui": {"estado": "MA", "autoridade portuária": "Empresa Maranhense de Administração Portuária", "tipo": "marítimo"},
    "Manaus": {"estado": "AM", "autoridade portuária": "Superintendência da Zona Franca de Manaus", "tipo": "fluvial"}
}

def buscar_informacoes_porto():
    nome_porto = input("Digite o nome do porto: ").title()
    if nome_porto in portos:
        porto = portos[nome_porto]
        print(f"Estado: {porto['estado']}")
        print(f"Autoridade Portuária: {porto['autoridade portuária']}")
        print(f"Tipo: {porto['tipo']}")
    else:
        print("Porto não encontrado.")

def buscar_portos_por_regiao():
    regioes = {
        "N": ["Porto de Porto Velho", "Porto de Macapá", "Porto de Manaus"],
        "NE": ["Porto de Suape", "Porto de Itaqui", "Porto de Cabedelo", "Porto de Recife"],
        "S": ["Porto de Imbituba", "Porto de Paranaguá", "Porto de Rio Grande", "Porto de Laguna", "Porto de São Francisco do Sul", "Porto de Antonina", "Porto de Pelotas", "Porto de Porto Alegre", "Porto de Itajaí"],
        "SE": ["Porto de São Sebastião", "Porto do Forno"]
    }
    entrada = input("Digite o nome da região desejada: ")
    if entrada.upper() in regioes:
        print("Portos na região {}:".format(entrada.upper()))
        for porto in regioes[entrada.upper()]:
            print(porto)
    else:
        print("Região não encontrada.")

def buscar_tipo_porto():
    nome_porto = input("Digite o nome do porto: ").title()
    if nome_porto in portos:
        tipo_porto = portos[nome_porto]['tipo']
        print(f"O tipo do porto {nome_porto} é: {tipo_porto}")
    else:
        print("Porto não encontrado.")

while True:
    print("MENU")
    print("1 - Buscar informações de um porto")
    print("2 - Buscar portos por região")
    print("3 - Buscar tipo de um porto")
    print("4 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        buscar_informacoes_porto()
    elif opcao == "2":
        buscar_portos_por_regiao()
    elif opcao == "3":
        buscar_tipo_porto()
    elif opcao == "4":
        break
    else:
        print("Opção inválida. Tente novamente.")