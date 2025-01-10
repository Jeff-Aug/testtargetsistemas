def is_fibonacci(num):
    # Inicia a sequência de Fibonacci
    a, b = 0, 1
    
    # Verifica enquanto o valor atual não exceder o número fornecido
    while a <= num:
        if a == num:
            return True
        a, b = b, a + b
    return False

# Entrada do usuário
num = int(input("Informe um número: "))

# Verifica se o número está na sequência
if is_fibonacci(num):
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci.")
