'''
    A tartaruga e a lebre vão apostar uma corrida. A lebre concede à tartaruga o direito de
    sair n sua frente.     A tartaruga corre a 1 metro por minuto e a lebre corre a 10 metros por minuto.
    Faça um programa que leia quantos metros a tartaruga sai à frente da lebre e calcule quantos minutos
    levará até que a lebre alcance a tartaruga.
    Por exemplo, se a tartaruga sair 500 metros à frente a lebre alcança em 56 minutos.
'''

def tempo_corrida(vantagem):
    # início da corrida no tempo zero.
    tempo = 0

    # posição da lebre no início é zero
    posicao_lebre = 0

    # a tartaruga sai com uma vantagem em metros na frente
    posicao_tartaruga = posicao_lebre + vantagem

    # enquanto a tartaruga estiver na frente
    while posicao_tartaruga > posicao_lebre:
        # após 1 minuto no tempo
        tempo += 1

        # a lebre andou 10 metros
        posicao_lebre += 10

        # a tartaruga andou 1 metro
        posicao_tartaruga += 1

    # retorna a quantidade de tempo
    return tempo


def main():
    d = int(input())
    print(f'{tempo_corrida(d)}')

if __name__ == '__main__':
    main()
