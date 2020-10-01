def cancao_programadores(inicio=99, final=250, passo=1):
    for k in range(inicio, final+1, passo):
        print(f'{k} bugs no software, pegue sete deles e conserte...')
        print('Tecle "Ctrl+F5"')
    print('Vamos fazer mais um café!')

def main():
    cancao_programadores(passo=7)

if __name__ == '__main__':
    main()
