# Escreva um programa que leia três números por parâmetro e
# mostre na tela em ordem crescente.

def ordena(a, b, c):
    if (a <= b) and (a <= c):
        if b <= c:
            return a, b, c
        else:
            return a, c, b
    if (b <= a) and (b <= c):
        if a <= c:
            return b, a, c
        else:
            return b, c, a
    if (c <= a) and (c <= b):
        if a <= b:
            return c, a, b
        else:
            return c, b, a

def main():
    #Entrada de dados
    n1 = int(input('1o número: '))
    n2 = int(input('2o número: '))
    n3 = int(input('3o número: '))

    #Processamento chamando a função
    n1, n2, n3 = ordena(n1, n2, n3)

    #Saída de dados
    print(f'Menor: {n1}')
    print(f'Meio: {n2}')
    print(f'Maior: {n3}')

if __name__ == '__main__':
    main()


