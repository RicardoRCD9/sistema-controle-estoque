import time
print('\nDesenvolvimento de um Sistema de Controle de Estoque\n')

estoque = []

# Adicionando produtos ao estoque.
def adicionar_produtos():
    while True:
        while True:
            try:
                codigo = int(input('Código: '))
                if codigo <= 0:
                    print('Digite um valor maior que 0.')
                    continue
                codigos_cadastrados = []    
                for c in estoque:
                    codigos_cadastrados.append(c['Código'])
                if codigo in codigos_cadastrados:
                    print('Código já cadastrado!')
                    continue
                break
            except ValueError:
                print('Digite um valor válido!')
        produto = input('Nome: ').strip()
        while produto == '':
            print('Digite um nome para o produto.')
            produto = input('Nome: ').strip()
        while True:
            try:
                preco = float(input('Preço: ').replace(',','.'))
                if preco >= 0:
                    break
                else:
                    print('Digite um valor igual ou superior a 0.')
            except ValueError:
                print('Digite um valor válido!')
        while True:
            try:
                quantidade = int(input('Quantidade: '))
                if quantidade >= 0:
                    break
                else:
                    print('Digite um valor igual ou superior a 0.')
            except ValueError:
                print('Digite um valor válido!')

        novo_produto = {
            'Código': codigo,
            'Produtos': produto,
            'Preco': preco,
            'Quantidade': quantidade
        }
        estoque.append(novo_produto)
        print('Produto cadastrado com SUCESSO.')

        print()
        while True:
            continuar = input('\nDeseja cadastrar outro produto? [SIM/NÃO]: ').strip().upper()
            if continuar == 'SIM':
                break
            elif continuar in ['NAO', 'NÃO']:
                return
            else:   
                print('Digite SIM ou NÃO!')

# Consultar produtos cadastrados.
def consulta_cadastrados():
    if not estoque:
        print('\nSem produtos cadastrados, voltando ao menu...')
        for c in range(3, 0, -1):
            print(f'{c}...')
            time.sleep(1)
        return
    print('\nProdutos cadastrados.\n')
    for c in estoque:
        print(c)
    # Executa o retorno ao MENU.
    voltar_menu()

# Calcula o total de itens cadastrados e a quantidade de produtos em estoque.
def calcular_estoque():
    print('=' * 30)
    print('\nCalculando estoque.\n')
    print('=' * 30)
    soma_codigo = len(estoque)
    print(f'O total de produtos cadastrados é {soma_codigo}')
    soma_quantidade = 0
    for produto in estoque:
        soma_quantidade += produto['Quantidade']
    print(f'A soma total de produtos é: {soma_quantidade}')
    # Executa o retorno ao MENU.
    voltar_menu()

# Volta para o MENU.
def voltar_menu():
    voltar = input('\nPara voltar ao menu pressione [ENTER]: ')

# MENU PRINCIPAL DA GESTÃO DE ESTOQUE.
while True:
    print('=' * 30)
    print('|| GESTÃO DE ESTOQUE ||'.center(30))
    print('=' * 30)
    print('''
[1] \u2192 Cadastrar produtos.
[2] \u2192 Consultar produtos cadastrados.
[3] \u2192 Consultar soma total do estoque.
[4] \u2192 Para sair...''')
    opcao = input('Digite uma opção: ')
    print()
    if opcao == '1':
        adicionar_produtos()
    elif opcao == '2':
        consulta_cadastrados()
    elif opcao == '3':
        calcular_estoque()
    elif opcao == '4':
        print('Programa encerrado.')
        break
    else:
        print('\nDigite uma opção entre 1 e 4.\n')