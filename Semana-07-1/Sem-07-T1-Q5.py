'''
    O dodô é uma ave não voadora, extinta atualmente, e que era endêmica da Ilha
    Maurítius, na costa leste da África. A partir do ano 1600, durante cada ano, 6%
    dos animais dos animais vivos no começo do ano morreram e o número de
    animais nascidos ao longo do ano que sobreviveram foi de 1% da população
    inicial.

    Escreva um programa que leia a população de aves no início do ano 1600 e
    imprime, anualmente, a partir do fim de 1600, o número de nascimentos, mortes e o total da população
    por ano (apenas a parte inteira do números, separados por vírgula). O programa encerra sua execução
    quanto a população total cai para menos de 10% da população original.
'''

def imprimir_evolucao(populacao):
    tx_mortalidade = 6/100
    tx_natalidade = 1/100
    parar = populacao * 0.10
    ano = 1600
    while populacao > parar:
        mortes = populacao * tx_mortalidade
        nascidos = populacao * tx_natalidade
        populacao = populacao + nascidos - mortes
        print(f'{ano:d},{nascidos:.0f},{mortes:.0f},{populacao:.0f}')
        ano += 1
    

def main():
    p = int(input('População de aves no início do ano 1600: '))
    imprimir_evolucao(p)

if __name__ == '__main__':
    main()
