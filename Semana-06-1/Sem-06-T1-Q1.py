'''
    Escreva um programa que pergunte o depósito inicial e a taxa de juros ao ano de uma poupança.
    Mostre em quantos anos o valor acumulado será o dobro do valor inicial.
'''

def tempo_para_dobrar(valor, taxa):
    dobro = valor * 2
    tempo = 0
    while valor < dobro:
        valor *= (1 + (taxa/100))
        tempo += 1
    return tempo

def main():
    pv = float(input('Digite o valor atual: '))
    i = float(input('Digite a taxa de juros: '))
    print(f'O valor irá dobrar em {tempo_para_dobrar(pv, i)} anos')

if __name__ == '__main__':
    main()
