from classes.produto import Produto

def menu():
    print()
    print("1 - Listar Produtos")
    print("2 - Inserir Produto")
    print("3 - Alterar Produto")
    print("4 - Excluir Produto")
    print("0 - Sair")
    print()

opcao = 1

while opcao != 0:
    menu()
    opcao = int(input('Escolha uma oção: '))

    match opcao:
        case 1:
            print('------------------------------------------------------------------------')
            Produto.listarTodos()
            print('------------------------------------------------------------------------')

        case 2:
            codigo = input('Digite o código: ')
            nome = input('Digite o nome: ')
            quantidade = input('Digite a quantidade: ')
            valor = input('Digite o valor: ')

            produto = Produto(codigo, nome, quantidade, valor)
            produto.inserir()

        case 3:
            Produto.listarTodos()
            selecionado = int(input('Qual ítem deseja alterar? '))
            item = Produto.consultar(selecionado)
            print(selecionado)
            print(item)

            quantidade = int(input('Qual a nova quantidade? '))
            valor = int(input('Qual o novo valor? '))
            produto = Produto(item['codigo'], item['nome'], quantidade, valor)
            produto.alterar(selecionado)

        case 4:
            Produto.listarTodos()
            selecionado = int(input('Qual item deseja excluir? '))

            Produto.excluir(selecionado)

print()
print("Até a próxima!")