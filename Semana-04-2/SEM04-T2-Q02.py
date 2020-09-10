# (Dificuldade de 01 a 05: 2)
# Escreva um programa que leia um número inteiro entre 100 e 999,
# mostre quantos dígitos pares existem nesse número.
# Por exemplo: 245 tem 2 dígitos pares; 135 tem 0 dígitos pares;
# 134 tem 1 dígito par.

def e_par(n):
    return n % 2 == 0

def conta_pares(n):
    qtd = 0
    
    k = n % 10
    n = n // 10
    if e_par(k):
        qtd += 1

    k = n % 10
    n = n // 10
    if e_par(k):
        qtd += 1

    k = n % 10
    n = n // 10
    if e_par(k):
        qtd += 1

    return qtd

def main():
    #Entrada de dados
    n = int(input('Digite um número entre 100 e 999: '))

    #Processamento chamando a função
    if n >= 100 and n <= 999:
        resultado = conta_pares(n)

        #Saída de dados
        print(f'O número {n} tem {resultado} números pares.')

if __name__ == '__main__':
    main()
