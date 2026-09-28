# Pesquisa de Satisfação

excelente = 0
ruim = 0

print("=" * 45)
print("      PESQUISA DE ATENDIMENTO - TUDOWEB")
print("=" * 45)

for i in range(1, 11):
    print(f"\n--- Entrevistado {i}/50 ---")

    nome = input("Nome: ")

    while True:
        try:
            idade = int(input("Idade: "))
            if idade > 0:
                break
            print("Digite uma idade válida.")
        except ValueError:
            print("Digite a idade usando apenas números.")

    while True:
        print("\nOpinião sobre o atendimento:")
        print("1 - EXCELENTE")
        print("2 - BOM")
        print("3 - RUIM")

        try:
            opiniao = int(input("Digite a opção (1, 2 ou 3): "))
            if opiniao in [1, 2, 3]:
                break
            print("Opção inválida. Digite 1, 2 ou 3.")
        except ValueError:
            print("Digite apenas o número da opção.")

    if opiniao == 1:
        excelente += 1
    elif opiniao == 3:
        ruim += 1

print("\n" + "=" * 45)
print("           RESULTADO DA PESQUISA")
print("=" * 45)
print(f"Quantidade de respostas EXCELENTE: {excelente}")
print(f"Quantidade de respostas RUIM: {ruim}")
print("=" * 45)
