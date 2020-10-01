'''
    Escreva um programa que leia número inteiro qualquer e mostre na forma invertida.
'''

def inverter(n):
    n_invertido = 0
    while n > 0:
        n_invertido = (10 * n_invertido) + (n % 10)
        n //= 10
    return n_invertido

def main():
    n = int(input())
    print(inverter(n))
        
if __name__ == '__main__':
    main()
