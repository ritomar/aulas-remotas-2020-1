def cancao_programadores(inicio=99, final=250, passo=1):
    for k in range(inicio, final+1, passo):
        print(f'{k} bugs no software, pegue um deles e conserte...')

def main():
    cancao_programadores()

if __name__ == '__main__':
    main()
