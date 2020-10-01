'''
    Escreva um programa que leia dois valores inteiros (x e y) e mostre
    todos os números primos entre x e y.

'''

def e_divisor(n, m):
    return n % m == 0

def e_primo(n):
    for k in range(2, n):
        if e_divisor(n, k):
            return False
    return True

def main():
    x = int(input())
    y = int(input())
    for k in range(x, y+1):
        if e_primo(k):
            print(k)

if __name__ == '__main__':
    main()
