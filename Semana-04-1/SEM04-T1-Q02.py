# (Dificuldade de 01 a 05: 4)
# Escreva um programa que leia 2 datas (cada data é composta
# por 3 variáveis inteiras: dia, mês e ano) e escreva no formato
# DD/MM/AAAA a mais recente.

def data_formatada(dia, mes, ano):
    return f'{dia}/{mes}/{ano}'

def mais_recente(d1, m1, a1, d2, m2, a2):
    if a1 > a2:
        return d1, m1, a1
    if a1 < a2:
        return d2, m2, a2
    else: # mesmo ano
        if m1 > m2:
            return d1, m1, a1
        if m1 < m2: 
            return d2, m2, a2
        else: # mesmo mes
            if d1 > d2:
                return d1, m1, a1
            else: # d2 é igual ou maior
                return d2, m2, a2 
            
def main():
    #Entrada de dados
    d1 = int(input('Dia data 1:'))
    m1 = int(input('Mês data 1:'))
    a1 = int(input('Ano data 1:'))
    d2 = int(input('Dia data 2:'))
    m2 = int(input('Mês data 2:'))
    a2 = int(input('Ano data 2:'))
    
    #Processamento chamando a função
    d, m, a = mais_recente(d1, m1, a1, d2, m2, a2)

    #Saída de dados
    print(f'A data mais recente é: {data_formatada(d, m, a)}')

if __name__ == '__main__':
    main()


