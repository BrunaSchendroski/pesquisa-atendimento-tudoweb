# Pesquisa de Atendimento ao Cliente - TudoWeb

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge\&logo=python\&logoColor=white)](https://www.python.org/)
[![GitHub](https://img.shields.io/badge/GitHub-Repositório-181717?style=for-the-badge\&logo=github\&logoColor=white)](https://github.com/)
[![Status](https://img.shields.io/badge/Status-Concluído-2ea44f?style=for-the-badge)](#)

## Sobre o projeto

Projeto desenvolvido em **Python** para a empresa fictícia **TudoWeb**, com o objetivo de realizar uma pesquisa de opinião com clientes para verificar o grau de satisfação em relação ao atendimento prestado.

O programa realiza a coleta de dados de **50 entrevistados** e, ao final, apresenta a quantidade de respostas **EXCELENTE** e **RUIM**.

## Tecnologias utilizadas

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square\&logo=python\&logoColor=white)](https://www.python.org/)

[![VS Code](https://img.shields.io/badge/VS%20Code-Editor-007ACC?style=flat-square\&logo=visual-studio-code\&logoColor=white)](https://code.visualstudio.com/)

* Python 3
* Estrutura de repetição `for`
* Estruturas de decisão `if` e `elif`
* Variáveis
* Contadores
* Entrada e saída de dados
* Validação de dados

## Funcionamento

O programa solicita, para cada entrevistado:

* Nome
* Idade
* Opinião sobre o atendimento

As opções de opinião são:

| Opção | Opinião   |
| :---: | --------- |
|  `1`  | EXCELENTE |
|  `2`  | BOM       |
|  `3`  | RUIM      |

A pesquisa é realizada com **50 entrevistados**.

Ao finalizar, o programa exibe:

* Quantidade de respostas **EXCELENTE**
* Quantidade de respostas **RUIM**

## Estrutura de repetição

Foi utilizada a estrutura `for` para repetir o processo de coleta dos dados 50 vezes:

```python
for i in range(1, 51):
    print(f"\n--- Entrevistado {i}/50 ---")
```

## Estrutura de decisão

As opiniões são verificadas utilizando estruturas condicionais:

```python
if opiniao == 1:
    excelente += 1
elif opiniao == 3:
    ruim += 1
```

Quando a resposta é `1`, o contador de respostas **EXCELENTE** é incrementado.

Quando a resposta é `3`, o contador de respostas **RUIM** é incrementado.

## Código principal

```python
excelente = 0
ruim = 0

print("=" * 45)
print("      PESQUISA DE ATENDIMENTO - TUDOWEB")
print("=" * 45)

for i in range(1, 51):
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
```

## Teste com 10 entrevistados

Para validar o funcionamento do programa, foi realizado um teste com 10 entrevistados.

| Nº | Nome     | Idade | Opinião   |
| -: | -------- | ----: | --------- |
|  1 | Ana      |    18 | EXCELENTE |
|  2 | Bruno    |    20 | BOM       |
|  3 | Carla    |    17 | RUIM      |
|  4 | Diego    |    22 | EXCELENTE |
|  5 | Elisa    |    19 | BOM       |
|  6 | Felipe   |    25 | RUIM      |
|  7 | Gabriela |    21 | EXCELENTE |
|  8 | Henrique |    18 | EXCELENTE |
|  9 | Isabela  |    23 | BOM       |
| 10 | João     |    20 | RUIM      |

### Resultado do teste

[![Excelente](https://img.shields.io/badge/EXCELENTE-4-2ea44f?style=for-the-badge)](#)
[![Bom](https://img.shields.io/badge/BOM-3-6f42c1?style=for-the-badge)](#)
[![Ruim](https://img.shields.io/badge/RUIM-3-d73a49?style=for-the-badge)](#)

* **EXCELENTE:** 4 respostas
* **BOM:** 3 respostas
* **RUIM:** 3 respostas

O resultado confirma que os contadores estão funcionando corretamente.

## Prints do projeto

### Código

![Print do código](print_codigo.png)

### Execução do teste

![Print da execução do teste](print_execucao_teste.png)

## Estrutura dos arquivos

```text
📁 pesquisa-atendimento-tudoweb
│
├── pesquisa_tudoweb.py
├── teste_10_entrevistados.txt
├── print_codigo.png
├── print_execucao_teste.png
└── README.md
```

## Como executar

1. Instale o **Python 3**.
2. Abra o arquivo `pesquisa_tudoweb.py`.
3. Execute o programa.
4. Digite o nome do entrevistado.
5. Digite a idade.
6. Escolha uma das opções de atendimento.
7. Repita o processo até completar os 50 entrevistados.
8. Confira o resultado apresentado ao final.

## Objetivo da atividade

O projeto foi desenvolvido para praticar conceitos fundamentais de programação em Python, principalmente:

* Estruturas de repetição;
* Estruturas de decisão;
* Variáveis;
* Contadores;
* Entrada de dados;
* Validação de informações.

## Autoria

Projeto desenvolvido como atividade acadêmica para a empresa fictícia **TudoWeb**.

---

[![Made with Python](https://img.shields.io/badge/Made%20with-Python-3776AB?style=flat-square\&logo=python\&logoColor=white)](https://www.python.org/)
[![GitHub](https://img.shields.io/badge/Projeto-GitHub-181717?style=flat-square\&logo=github\&logoColor=white)](https://github.com/)
