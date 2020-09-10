# Escreva um programa que leia o nome e o estado civil de uma pessoa,
# considere apenas "1" para casado e "2" para solteiro. Se a pessoa
# for casada, leia, também, o nome do cônjuge. Mostre quantos caracteres
# no total existem no(s) nome(s) lido(s).

def main():
    #Entrada de dados
    nome = input('Digite seu nome: ')
    estado_civil = int(input('Digite 1 para CASADO ou 2 para SOLTEIRO: '))


    #Processamento chamando a função
    qtd_caracteres = len(nome)
    if estado_civil == 1:
        nome_conjuge = input('Digite o nome do cônjuge: ')
        qtd_caracteres += len(nome_conjuge)


    #Saída de dados
    print(f'O total de caracteres lidos foi: {qtd_caracteres}')

if __name__ == '__main__':
    main()


