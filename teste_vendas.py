from venda import Produto, Venda

def menu():
    dataVenda = input("Data da Venda (dd/mm/aaaa): ")
    venda = Venda(dataVenda)

    while True:
        print("\nMenu:")
        print("1. Adicionar Produto")
        print("2. Remover Produto")
        print("3. Listar Produtos")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do produto: ")
            preco = float(input("Preço do produto: "))
            quantidade = int(input("Quantidade: "))

            produto = Produto(nome, preco, quantidade)
            venda.adicionarProduto(produto)
            print(f"Produto '{nome}' adicionado com sucesso!")

        elif opcao == "2":
            nome = input("Nome do produto a remover: ")
            venda.removerProduto(nome)

        elif opcao == "3":
            venda.listarProdutos()

        elif opcao == "4":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
