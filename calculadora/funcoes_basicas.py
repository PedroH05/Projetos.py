def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero não é permitida."
    return a / b
def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero não é permitida."
    return a / b


def calculadora(): 
    print("\n--- CALCULADORA ---")

    while True:
        escolha = input("Voce deseja fazer o calculo? (S/N): ").lower().strip()
        
        if escolha == "n":
            print("encerrando a calculadora...")
            break
        elif escolha != "s":
            print("Opcao invalida. Tente novamente.")
            continue
        
        a = float(input("Digite o primeiro numero: "))
        b = float(input("Digite o segundo numero: "))
        escolha_operacao = input("Escolha sua operacao: 1 - SOMA 2 - SUBTRAÇÃO, 3 - MULTIPLICAÇÃO, 4 - DIVISÃO: ").strip()
        
        if escolha_operacao == "1":
            resultado = somar(a,b)
        elif escolha_operacao == "2":
            resultado = subtrair(a,b)
        elif escolha_operacao == "3":
            resultado = multiplicar(a,b)
        elif escolha_operacao == "4":
            resultado = dividir(a,b)
        else:
            print("Operação inválida.")
            continue
        
        print(f"Resultado: {resultado}\n")

calculadora()
