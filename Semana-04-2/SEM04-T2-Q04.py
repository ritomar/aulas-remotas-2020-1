# (Dificuldade de 01 a 05: XX)
# Escreva um programa que leia a data de nascimento do usuário,
# e informa qual o seu signo. Considere exatamente:
# Áries (21/03 a 19/04); Touro (20/04 a 20/05);
# Gêmeos (21/05 a 21/06); Câncer (22/06 a 22/07);
# Leão (23/07 a 22/08); Virgem (23/08 a 22/09);
# Libra (23/09 a 22/10); Escorpião (23/10 a 21/11);
# Sagitário (22/11 a 21/12); Capricórnio (22/12 a 19/01);
# Aquário (20/01 a 18/02); Peixes (19/02 a 20/03);

def signo(dia, mes):
    if mes == 3:
        return 'Peixes' if dia < 21 else 'Áries'
    if mes == 4:
        return 'Áries' if dia < 20 else 'Touro'
    if mes == 5:
        return 'Touro' if dia < 21 else 'Gêmeos'
    if mes == 6:
        return 'Gêmeos' if dia < 22 else 'Câncer'
    if mes == 7:
        return 'Câncer' if dia < 23 else 'Leão'
    if mes == 8:
        return 'Leão' if dia < 23 else 'Virgem'
    if mes == 9:
        return 'Virgem' if dia < 23 else 'Libra'
    if mes == 10:
        return 'Libra' if dia < 23 else 'Escorpião'
    if mes == 11:
        return 'Escorpião' if dia < 22 else 'Sagitário'
    if mes == 12:
        return 'Sagitário' if dia < 22 else 'Capricórnio'
    if mes == 1:
        return 'Capricórnio' if dia < 20 else 'Aquário'
    if mes == 2:
        return 'Aquário' if dia < 19 else 'Peixes'

def main():
    #Entrada de dados
    d = int(input('Dia do nascimento: '))
    m = int(input('Mês do nascimento: '))

    #Processamento chamando a função
    meu_signo = signo(d, m)

    #Saída de dados
    print(f'O signo é: {meu_signo}')

if __name__ == '__main__':
    main()


