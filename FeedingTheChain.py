
usuarios_registrados = {
    "FeedingTheChain": "123a"
}


def fazer_login():
    nome_usuario = input("Nome de usuário: ")
    senha = input("Senha: ")
    if nome_usuario in usuarios_registrados and senha == usuarios_registrados[nome_usuario]:
        return True
    else:
        return False


def exibir_menu():
    print("\nMenu:")
    print("1. Caminhão 1")
    print("2. Caminhão 2")
    print("3. Caminhão 3")
    print("4. Caminhão 4")
    print("5. Caminhão 5")


def obter_informacoes_caminhao(caminhao):
    caminhoes = {
        "Caminhão 1": {
            "Rota": "São Paulo",
            "Alimentos": ["Frutas", "Verduras"]
        },
        "Caminhão 2": {
            "Rota": "Rio Grande do Sul",
            "Alimentos": ["Carnes", "Laticínios"]
        },
        "Caminhão 3": {
            "Rota": "Minas Gerais",
            "Alimentos": ["Grãos", "Legumes"]
        },
        "Caminhão 4": {
            "Rota": "Paraná",
            "Alimentos": ["Bebidas", "Snacks"]
        },
        "Caminhão 5": {
            "Rota": "Santa Catarina",
            "Alimentos": ["Pães", "Bolos"]
        }
    }
    return caminhoes[caminhao]


def main():
    
    if fazer_login():
        print("Login realizado com sucesso!")
        while True:
            
            exibir_menu()
            opcao = input("Escolha uma opção (1-5) ou digite 'sair' para encerrar: ")

            
            if opcao.lower() == "sair":
                break

            
            if opcao.isnumeric() and 1 <= int(opcao) <= 5:
                caminhao = f"Caminhão {opcao}"
                informacoes = obter_informacoes_caminhao(caminhao)
                print(f"\nInformações do {caminhao}:")
                print(f"Rota: {informacoes['Rota']}")
                print(f"Alimentos: {', '.join(informacoes['Alimentos'])}")
            else:
                print("Opção inválida.")
    else:
        print("Login inválido.")


main()
