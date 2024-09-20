def gerar_fibonacci(limite):
    sequencia = [0, 1]
    while sequencia[-1] < limite:
        proximo_valor = sequencia[-1] + sequencia[-2]
        if proximo_valor > limite:
            break
        sequencia.append(proximo_valor)
    return sequencia

def pertence_fibonacci(numero):
    sequencia = gerar_fibonacci(numero)
    return numero in sequencia

numero = int(input("Informe um número: "))


if pertence_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")