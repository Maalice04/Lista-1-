def sistema():
    print("Início")

    # Passo 1: Verificar se está cadastrado
    cadastrado = input("Você está cadastrado? (sim/não): ").strip().lower()
    if cadastrado != "sim":
        print("Cadastro inválido")
        return  # Encerra o programa

    # Se sim, pede nome e idade
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")

    # Passo 2: Ver dados
    ver_dados = input("Deseja ver os dados? (sim/não): ").strip().lower()
    if ver_dados != "sim":
        print("Cadastro")
    else:
        print(f"Nome: {nome}, Idade: {idade}")

    # Passo 3: Deseja sair do sistema?
    sair = input("Deseja sair do sistema? (sim/não): ").strip().lower()
    if sair == "sim":
        print("Saída")
        print("Fim")
    else:
        print("Retornando ao início...\n")
        sistema()  # Reinicia o sistema

# Iniciar o programa
sistema()