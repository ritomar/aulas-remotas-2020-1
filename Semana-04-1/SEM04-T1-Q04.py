# Escreva um programa que leia 5 (cinco) números inteiros,
# calcule a sua média e escreva os que são maiores que a média.
# Considere duas casas decimais.

def media_de_5(a, b, c, d, e):
    return (a + b + c + d + e) / 5

def main():
    #Entrada de dados
    n1 = float(input('1a número: '))
    n2 = float(input('2a número: '))
    n3 = float(input('3a número: '))
    n4 = float(input('4a número: '))
    n5 = float(input('5a número: '))

    #Processamento chamando a função
    media = media_de_5(n1, n2, n3, n4, n5)

    #Saída de dados
    print(f"Média: {media:.2f}")
    print('Maiores que a média:')
    if n1 > media:
        print(f'{n1:.2f}')
    if n2 > media:
        print(f'{n2:.2f}')
    if n3 > media:
        print(f'{n3:.2f}')
    if n4 > media:
        print(f'{n4:.2f}')
    if n5 > media:
        print(f'{n5:.2f}')


if __name__ == '__main__':
    main()
