'''
    Dado um país A, com taxa de natalidade de 2% ao ano, e um país B com uma taxa de natalidade de 3%
    ano. Sabe-se que, atualmente, o país A tem população maior que o país B. Faça um programa que leia a
    população de cada país e imprima o tempo necessário para que a população do país B ultrapasse a
    população do país A.
'''

def tempo(pA, pB, txA=2, txB=3):
    tempo = 0
    # Se população de A é menor, troca os valores.
    if pA < pB:
        pA, pB = pB, pA
        
    while pA > pB:
        tempo += 1
        pA *= (1 + (txA / 100))
        pB *= (1 + (txB / 100))
        
    return tempo

def main():
    p1 = int(input('Primeira população: '))
    p2 = int(input('Segunda população: '))
    print(f'O país B passa o país A em {tempo(p1, p2)} anos.')

if __name__ == '__main__':
    main()
