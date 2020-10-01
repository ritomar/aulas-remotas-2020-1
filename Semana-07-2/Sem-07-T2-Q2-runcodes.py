'''
    A Sequência de Fibonacci é uma sequência de números inteiros, começando por 0 e 1, na qual, cada termo
    subsequente corresponde à soma dos dois anteriores (0, 1, 1, 2, 3, 5, 8, 13, ...). Escreva um programa que
    leia um número n, calcule e mostre os n primeiros termos da sequência de Fibonacci.
    O valor lido para n sempre será maior ou igual a 2.
'''

def fibonacci(n):
    if n >= 2:
        n0, n1 = 0, 1
        fib = '0, 1'
        for k in range(3, n+1):
            proximo = n0 + n1
            fib += ', ' + str(proximo)
            n0, n1 = n1, proximo
        return fib
    else:
        raise ValueError('Valor inválido para gerar sequencia')
        

def main():
    n = int(input())
    print(fibonacci(n))

if __name__ == '__main__':
    main()
