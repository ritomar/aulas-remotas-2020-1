'''
    Sendo H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/n, escreva um programa para calcular
    o valor de H. O número n é lido.
'''

def valor_de_h(n):
    soma = 0
    for k in range(1, n+1):
        soma += 1/k
    return soma        

def main():
    n = int(input('Digite o valor de n: '))
    print(f'H({n}) = {valor_de_h(n):.4f}')

if __name__ == '__main__':
    main()
