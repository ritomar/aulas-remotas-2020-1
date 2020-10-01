'''
    Escreva um programa que leia uma quantidade indefinida de números inteiros positivos terminada pelo
    número 0 (zero). Ao final, o programa deve mostrar o maior e o menor de todos os números lidos
    (excluindo o zero). Dica: use repetição com teste no final
'''

def main():
    maior = 0
    menor = 0
    qtd = 0
    while True:
        n = int(input())
        if maior == 0 or n > maior: maior = n
        if (menor == 0 or n < menor) and (n != 0): menor = n
        qtd += 1
        if n == 0: break
        
    qtd -= 1 # Descarta o zero
    if qtd > 0:
        print(f'{maior}')
        print(f'{menor}')
        
if __name__ == '__main__':
    main()
