'''
    Escreva um programa que simula o valor (com duas casas decimais) da prestação de uma compra
    parcelada sem juros de 1x até 24x. O valor da compra é digitado pelo usuário. O valor da prestação sem
    juros, deve ser calculado como o valor da compra dividido pelo número de prestações de 1 até 24.
'''

def simulacao(valor):
    for k in range(1, 25):
        print(f'{k}x de R$ {valor/k:.2f}')

def main():
    v = float(input('Valor da compra: '))
    simulacao(v)

if __name__ == '__main__':
    main()
