'''
    Um número é, por definição, primo se ele não tem divisores, exceto 1 e ele próprio. Escreva um programa
    que leia um número e determine se ele é ou não primo.
'''

def e_divisor(n, m):
    return n % m == 0

def e_primo(n):
    for k in range(2, n):
        if e_divisor(n, k):
            return False
    return True

def main():
    n = int(input('Digite um número: '))
    print(f'{n} é um número primo?\n{e_primo(n)}')

if __name__ == '__main__':
    main()
