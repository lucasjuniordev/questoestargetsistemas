# Exercicio 1: Soma de números até um índice
def exercicio_1():
    INDICE = 13
    SOMA = 0
    K = 0
    while K < INDICE:
        K = K + 1
        SOMA = SOMA + K
    print("SOMA:", SOMA)

# Exercicio 2: Fibonacci e verificação se número pertence à sequência
def exercicio_2(num):
    fib = [0, 1]
    while fib[-1] < num:
        fib.append(fib[-2] + fib[-1])
    if num in fib:
        return f"O número {num} pertence à sequência Fibonacci."
    else:
        return f"O número {num} não pertence à sequência Fibonacci."

# Exercicio 3: Cálculo de faturamento de uma distribuidora
def exercicio_3(faturamento_estados):
    faturamento_total = sum(faturamento_estados.values())
    for estado, faturamento in faturamento_estados.items():
        percentual = (faturamento / faturamento_total) * 100
        print(f"{estado}: {percentual:.2f}%")

# Exercicio 4: Inverter uma string
def exercicio_4(s):
    resultado = ""
    for i in range(len(s)-1, -1, -1):
        resultado += s[i]
    return resultado

# Testes
if __name__ == "__main__":
    # Testando o Exercício 1
    exercicio_1()
    
    # Testando o Exercício 2
    num = int(input("Informe um número para verificar se pertence à sequência Fibonacci: "))
    print(exercicio_2(num))
    
    # Testando o Exercício 3
    faturamento_estados = {
        'SP': 67836.43,
        'RJ': 36678.66,
        'MG': 29229.88,
        'ES': 27165.48,
        'Outros': 19849.53
    }
    exercicio_3(faturamento_estados)
    
    # Testando o Exercício 4
    string = input("Informe uma string para inverter: ")
    print(f"A string invertida é: {exercicio_4(string)}")
