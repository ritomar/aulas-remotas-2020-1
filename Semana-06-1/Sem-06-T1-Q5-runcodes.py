'''
    Pedro recebe um salário mensal e tem aumentos salariais de 5% uma vez por ano no mês de março. Pedro
    também tem uma dívida no cartão de crédito com uma taxa de juros de 15% ao mês. Considerando que a
    situação se refere ao mês de outubro do ano de 2016, faça um programa leia o valor do salário e o valor
    da dívida e calcula, simulando a evolução do salário e da dívida de Pedro, em que mês e ano a dívida com
    o cartão de crédito será superior ao seu próprio salário.
'''

def main():
    vr_salario = float(input())
    tx_salario = (5/100)

    vr_divida = float(input())
    tx_divida = (15/100)

    mes = 10
    ano = 2016

    while vr_salario > vr_divida:
        if mes < 12:
            mes += 1
        else:
            mes = 1
            ano += 1

        vr_divida = vr_divida * (1 + tx_divida)
        if mes == 3:
            vr_salario = vr_salario * (1 + tx_salario)

    print(f'{mes}/{ano}')

if __name__ == '__main__':
    main()
