Exercícios em Python
Este repositório contém soluções para uma série de exercícios de programação em Python. Cada exercício resolve um problema específico com a implementação de funções.

Exercício 1: Soma de Números Até um Índice
Neste exercício, o objetivo é calcular a soma dos números inteiros de 1 até o valor do índice definido (neste caso, 13).

Código:
python
Copiar código
def exercicio_1():
    INDICE = 13
    SOMA = 0
    K = 0
    while K < INDICE:
        K = K + 1
        SOMA = SOMA + K
    print("SOMA:", SOMA)
Teste:
O programa calcula e imprime a soma dos números de 1 até 13.

Exercício 2: Fibonacci e Verificação de Número
Neste exercício, o objetivo é verificar se um número informado pertence à sequência de Fibonacci.

Código:
python
Copiar código
def exercicio_2(num):
    fib = [0, 1]
    while fib[-1] < num:
        fib.append(fib[-2] + fib[-1])
    if num in fib:
        return f"O número {num} pertence à sequência Fibonacci."
    else:
        return f"O número {num} não pertence à sequência Fibonacci."
Teste:
O programa recebe um número do usuário e verifica se ele pertence à sequência de Fibonacci.

Exercício 3: Cálculo de Faturamento de uma Distribuidora
Neste exercício, o objetivo é calcular o percentual de faturamento de uma distribuidora por estado, dada uma lista de faturamentos.

Código:
python
Copiar código
def exercicio_3(faturamento_estados):
    faturamento_total = sum(faturamento_estados.values())
    for estado, faturamento in faturamento_estados.items():
        percentual = (faturamento / faturamento_total) * 100
        print(f"{estado}: {percentual:.2f}%")
Teste:
O programa recebe um dicionário com os valores de faturamento por estado e imprime o percentual de faturamento de cada um.

Exercício 4: Inverter uma String
Neste exercício, o objetivo é inverter uma string fornecida pelo usuário.

Código:
python
Copiar código
def exercicio_4(s):
    resultado = ""
    for i in range(len(s)-1, -1, -1):
        resultado += s[i]
    return resultado
Teste:
O programa recebe uma string do usuário e imprime a string invertida.

Como Usar
Clone o repositório:

bash
Copiar código
git clone https://github.com/seuusuario/nomedorepositorio.git
Navegue até o diretório do projeto:

bash
Copiar código
cd nomedorepositorio
Execute o código:

bash
Copiar código
python nome_do_arquivo.py
Os testes dos exercícios são realizados automaticamente durante a execução do código.
