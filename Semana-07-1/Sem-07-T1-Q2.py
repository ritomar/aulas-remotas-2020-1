'''
    Você tem uma poupança de 10 mil reais, que rende 0,7% ao mês. Você deseja comprar um carro, mas o
    preço do carro sobe a taxa de 0,4% ao mês. Escreva um programa que leia o preço de um carro hoje e
    calcule em quantos meses, com o dinheiro dessa aplicação, você terá dinheiro suficiente para comprar o
    carro à vista.
'''
def tempo_comprar_carro(valor_carro):
    tempo = 0
    valor_poupanca = 10000
    taxa_poupanca = 0.007
    taxa_carro = 0.004
    while valor_poupanca < valor_carro:
        tempo += 1
        valor_poupanca *= (1 + taxa_poupanca)
        valor_carro *= (1 + taxa_carro)
        
    return tempo


def main():
    v = int(input('Preço do carro hoje: '))
    print(f'Você terá dinheiro suficiente em {tempo_comprar_carro(v)} meses.')

if __name__ == '__main__':
    main()
