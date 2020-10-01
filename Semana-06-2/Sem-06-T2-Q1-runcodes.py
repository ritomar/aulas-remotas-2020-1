'''
    Escreva um programa que leia um conjunto de números inteirose exiba a soma dos mesmos.
    Observação: A condição de saída do laço será a leitura do valor 0 (flag).
'''

def main():
    soma = 0
    qtd = 0
    while True:
        qtd += 1
        n = int(input())
        soma += n
        if n == 0: break
    print(f'{soma}')

if __name__ == '__main__':
    main()
