# (Dificuldade de 01 a 05: 2)
# Escreva um programa que leia um número inteiro entre 10 e 99, mostre uma das mensagens, a seguir, conforme o número lido.
# * Nenhum dígito é ímpar.
# * Apenas um dígito é ímpar.
# * Os dois dígitos são ímpares.


def e_impar(n):
    return n % 2 != 0

def conta_impares(n):
    qtd = 0
    
    k = n % 10
    n = n // 10
    if e_impar(k):
        qtd += 1

    k = n % 10
    n = n // 10
    if e_impar(k):
        qtd += 1

    return qtd

def main():
    #Entrada de dados
    n = int(input('Digite um número entre 10 e 99: '))

    #Processamento chamando a função
    if n >= 10 and n <= 99:
        resultado = conta_impares(n)
    else:
        resultado = -1

    #Saída de dados
    if resultado == 0:
        print('Nenhum dígito é ímpar.')
    elif resultado == 1:
        print('Apenas um dígito é ímpar.')
    elif resultado == 2:
        print('Os dois dígitos são ímpares.')


if __name__ == '__main__':
    main()
