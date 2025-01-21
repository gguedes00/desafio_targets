#DESAFIO 2

def pertence_a_fibonacci(numero):
    if numero < 0:
        return False
    a, b = 0, 1
    while b <= numero:
        if b == numero:
            return True
        a, b = b, a + b
    return False

# Entrada do número
numero = int(input("Digite um número: "))

# Verificação e resposta
if pertence_a_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")

else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")


