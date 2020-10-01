'''
    Escreva um programa que leia uma quantidade indefinida de números inteiros positivos terminada pelo
    número 0 (zero). Ao final, o programa deve mostrar a média aritmética de todos os números lidos
    (excluindo o zero).
'''

def main():
    soma = 0
    qtd = 0
    while True:
        n = int(input())
        soma += n
        qtd += 1
        if n == 0:
            break
    qtd -= 1
    if qtd > 0:
        print(f'{soma/qtd:.2f}')
        
if __name__ == '__main__':
    main()
