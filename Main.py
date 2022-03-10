print("Olá, seja bem vindo!")
while True:
    opcao = input("""
    Escolha uma opção abaixo:
    1 - Achar ΔS (Achar variação do espaço) 
    2 - Achar S ( Achar posição final)
    3 - Achar S0 (Achar posição inicial)
    4 - Achar V (Achar velocidade final)
    5 - Achar V0 (Achar velocidade inicial)
    6 - Achar a (Achar aceleração)
    7 - Achar T (Achar tempo)
    0 - Sair
    """)

    if opcao == "1":
        try:
            print("Insira os valores a seguir (0 caso não tenha)")
            S = float(input("Insira o valor da posição final: "))
            S0 = float(input("Insira o valor da posição inicial: "))
            V0 = float(input("Insira a velocidade inicial: "))
            T0 = float(input("Insira o tempo inicial: "))
            T = float(input("Insira o tempo final: "))
            a = float(input("Insira a aceleração: "))
        except:
            print("Valor inválido!")
        print(S, S0, V0, T0, T, a)
        if (S !=0 and a == 0):
            print(f"O resultado é {S-S0} .")

    elif opcao == "2":
        ""
    elif opcao == "3":
        ""
    elif opcao == "4":
        ""
    elif opcao == "5":
        ""
    elif opcao == "6":
        ""
    elif opcao == "7":
        ""
    elif opcao == "0":
        break
    else:
        print("Opção Inválida")
