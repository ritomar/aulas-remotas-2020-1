def cancao_programadores(inicio=99, final=0, passo=-11):
    for k in range(inicio, final+1, passo):
        print(f'{k} bugs no software, pegue onze deles e conserte...')
        print('Tecle "Ctrl+F5"')
    print('Sem erros no software! Está estabilizado!')

def main():
    cancao_programadores()

if __name__ == '__main__':
    main()
