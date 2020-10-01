'''
    Escreva um programa que, para um número indeterminado de pessoas:
    a. leia a idade de cada pessoa, sendo que a leitura da idade 0 (zero) indica o fim dos
       dados (flag) e não deve ser considerada;
    b. calcule e escreva o número de pessoas;
    c. calcule e escreva a idade média do grupo;
    d. calcule e escreva a menor idade e a maior idade.
'''

def main():
    qtd = soma = 0
    menor = maior = 0
    
    while True:
        idade = int(input())
        qtd += 1
        soma += idade

        if (menor == 0) or (idade < menor and idade != 0):
            menor = idade
        if (maior == 0) or (idade > maior):
            maior = idade
            
        if idade == 0: break

    qtd -= 1

    if qtd > 0:
        print(f'{qtd}')
        print(f'{soma/qtd:.2f}')
        print(f'{menor}')
        print(f'{maior}')

if __name__ == '__main__':
    main()
