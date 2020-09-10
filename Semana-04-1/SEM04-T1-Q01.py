# (Dificuldade de 01 a 05: 3) Escreva um programa que leia, separadamente,
# dia, mês e ano da data atual. Leia, da mesma forma, a data de nascimento
# de uma pessoa, calcule e escreva a idade exata em anos.

def calcula_idade(da, ma, aa, dn, mn, an):
    # da, ma, aa - data atual
    # dn, mn, an - data nascimento
    idade = aa - an - 1
    if (ma >= mn) and (da >= dn):
        idade += 1
    return idade

def main():
    #Entrada de dados
    d1 = int(input('Dia atual:'))
    m1 = int(input('Mês atual:'))
    a1 = int(input('Ano atual:'))
    d2 = int(input('Dia nascimento:'))
    m2 = int(input('Mês nascimento:'))
    a2 = int(input('Ano nascimento:'))
    

    #Processamento chamando a função
    resultado = calcula_idade(d1, m1, a1, d2, m2, a2)

    #Saída de dados
    print(f'Sua idade atual é: {resultado}')

if __name__ == '__main__':
    main()


