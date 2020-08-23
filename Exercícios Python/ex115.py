import utilidades

def cadastrar_pessoa(nome='', idade=0):
    cadastro = open('Cadastro_de_Pessoas.txt', 'a+')
    print(f'{nome:<30}{idade:>5} anos', file=cadastro)
    cadastro.close()


def ler_cadastro():
    try:
        cadastro = open('Cadastro_de_Pessoas.txt', 'r')
    except FileNotFoundError:
        print(f'O cadastro ainda não foi criado!\nCadastre uma pessoa primeiro.')
    else:
        for linha in cadastro.readlines():
            print(linha, end = '')
        cadastro.close()


utilidades.titulo('Cadastro de Pessoas')
while True:
    utilidades.titulo('MENU PRINCIPAL')
    print('(1) Cadastrar uma pessoa')
    print('(2) Ver a lista de cadastro')
    print('(3) Encerrar o programa')
    escolha = utilidades.leiaint('Digite uma opção: ')
    if escolha == 1:
        utilidades.titulo('--- CADASTRO DE NOVA PESSOA ---')
        while True:
            nome = str(input('Digite o nome: '))
            idade = utilidades.leiaint('Digite a idade: ')
            while True:
                confirma = str(input(f'Confirma: {nome}, {idade} anos? (S/N): ')).strip().upper()[0]
                if confirma in 'SN':
                    break
                print(f'Digite S ou N.')
            if confirma == 'S':
                break
            print(f'Reinicializando o cadastro...')
        cadastrar_pessoa(nome, idade)
        print(f'{nome} cadastrado(a) com sucesso!')
    elif escolha == 2:
        utilidades.titulo('--- LISTA DO CADASTRO ---')
        ler_cadastro()
        utilidades.titulo('--- FIM DA LISTA ---')
    elif escolha == 3:
        utilidades.titulo('--- FIM DO PROGRAMA ---')
        print(f'{"Volte Sempre!":^40}')
        break
    else:
        print(f'A escolha {escolha} é inválida.\nVoltando para o menu principal.')
