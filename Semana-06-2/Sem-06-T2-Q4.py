'''
    O cardápio de uma casa de lanches, especializada em sanduíches, é dado abaixo.

        CÓDIGO  PRODUTO         PREÇO (R$)
        H       Hamburger       5,50
        C       Cheeseburger    6,80
        M       Misto Quente    4,50
        A       Americano       7,00
        Q       Queijo Prato    4,00
        X       PARA TOTAL DA CONTA

    Escreva um programa que leia o código de vários itens comprados por um freguês e acumule o total da
    compra. Ao finalizar com “X”, exiba o total a pagar.

    Observações:
        Se for informada uma opção que não está no menu deve mostrar a mensagem "Opção inválida.".
        Enquanto o código não for 'X' o programa deve continuar lendo os itens.
'''


def menu(msg):
    print('CÓDIGO  PRODUTO         PREÇO (R$)')
    print('H       Hamburger       5,50')
    print('C       Cheeseburger    6,80')
    print('M       Misto Quente    4,50')
    print('A       Americano       7,00')
    print('Q       Queijo Prato    4,00')
    print('X       PARA TOTAL DA CONTA')

    opcao = input(msg).upper()[0]

    return opcao


def main():
    total = 0
    while True:
        op = menu('Digite sua opção: ')
        if op == 'H':
            total += 5.50
        elif op == 'C':
            total += 6.80
        elif op == 'M':
            total += 4.50
        elif op == 'A':
            total += 7.00
        elif op == 'Q':
            total += 4.00
        if op == 'X': break
    print(f'{total:.2f}')

if __name__ == '__main__':
    main()
