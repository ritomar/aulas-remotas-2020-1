'''
Faça um programa que leia a nota de um aluno, entre zero e dez. Mostre a mensagem "Nota inválida."
caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido. Após informar
uma nota válida, o aluno deve ver seu conceito, segundo a tabela:
    Conceito Nota
    A        >= 8,5.
    B        >= 7,0
    C        >= 5,0
    D        >= 4
    E        >= 0
'''

def conceito(nota):
    if nota >= 8.5:
        return 'A'
    if nota >= 7.0:
        return 'B'
    if nota >= 5.0:
        return 'C'
    if nota >= 4.0:
        return 'D'
    if nota >= 0.0:
        return 'E'
    else:
        raise ValueError('Nota inválida')


def main():
    while True:
        nota = float(input('Digite uma nota entre 0 (zero) e 10 (dez): '))
        if 0 <= nota <= 10:
            break
        else:
            print('Nota inválida.')
        
    print(f'Nota {nota:.1f} - Conceito: {conceito(nota)}')

if __name__ == '__main__':
    main()
