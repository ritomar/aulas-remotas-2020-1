# Escreva um programa que leia 5 (cinco) números inteiros e escreva
# o maior e o menor deles.
# Considere que todos os valores são diferentes.

def maior_de_2(a, b):
    if a > b:
        return a
    else:
        return b
    
def maior_de_5(a, b, c, d, e):
    maior = maior_de_2(a, b)
    maior = maior_de_2(maior, c)
    maior = maior_de_2(maior, d)
    maior = maior_de_2(maior, e)
    return maior

def menor_de_2(a, b):
    if a < b:
        return a
    else:
        return b

def menor_de_5(a, b, c, d, e):
    menor = menor_de_2(a, b)
    menor = menor_de_2(menor, c)
    menor = menor_de_2(menor, d)
    menor = menor_de_2(menor, e)
    return menor    

def main():
    #Entrada de dados
    n1 = int(input('1o número: '))
    n2 = int(input('2o número: '))
    n3 = int(input('3o número: '))
    n4 = int(input('4o número: '))
    n5 = int(input('5o número: '))

    #Processamento chamando a função
    maior = maior_de_5(n1, n2, n3, n4, n5)
    menor = menor_de_5(n1, n2, n3, n4, n5)

    #Saída de dados
    print(f'Maior: {maior}')
    print(f'Menor: {menor}')
    
if __name__ == '__main__':
    main()


