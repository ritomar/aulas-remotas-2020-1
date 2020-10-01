'''
Escreva um programa que calcule o fatorial de um número inteiro lido, sabendo-se que:
    N ! = 1 x 2 x 3 x ... x N-1 x N
    0 ! = 1
'''

def fatorial(n):
    resultado = 1
    for k in range(1, n+1):
        resultado *= k
    return resultado
    

def main():
    n = int(input('Digite um número para calcular o fatorial: '))
    print(f'O fatorial de {n} é: {fatorial(n)}')

if __name__ == '__main__':
    main()
