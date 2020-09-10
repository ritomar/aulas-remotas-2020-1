# O índice de massa corporal (IMC) é uma medida internacional usada para
# calcular se uma pessoa está no peso ideal. O IMC é determinado pela
# divisão da massa do indivíduo pelo quadrado de sua altura, em que a
# massa está em quilogramas e a altura em metros. Escreva um programa
# que leia a massa e a altura de uma pessoa e calcula o IMC de uma pessoa,
# e depois, mostra uma das seguintes mensagens:

# IMC     Classificação
# < 18,5  Abaixo do peso
# < 25    Peso normal
# < 30    Sobrepeso
# < 35    Obeso leve
# < 40    Obeso moderado
# >=40    Obeso mórbido

def imc(massa, altura):
    resultado = massa / (altura ** 2)
    if resultado < 18.5:
        msg = 'Abaixo do peso'
    elif resultado < 25:
        msg = 'Peso normal'
    elif resultado < 30:
        msg = 'Sobrepeso'
    elif resultado < 35:
        msg = 'Obeso leve'
    elif resultado < 40:
        msg = 'Obeso moderado'
    elif resultado >= 40:
        msg = 'Obeso mórbido'
    return resultado, msg

def main():
    #Entrada de dados
    massa = float(input('Digite sua massa (peso): '))
    altura = float(input('Digite sua altura: '))

    #Processamento chamando a função
    valor_imc, mensagem = imc(massa, altura)

    #Saída de dados
    print(f'Resultado do IMC: {valor_imc:.2f}')
    print(f'Mensagem: {mensagem}')

if __name__ == '__main__':
    main()


