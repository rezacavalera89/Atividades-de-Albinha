from biblioteca import Autor, Livro, Biblioteca

def menu():
    biblioteca = Biblioteca()

    while True:
        print("\nMenu:")
        print("1. Adicionar Livro")
        print("2. Remover Livro")
        print("3. Buscar Livro")
        print("4. Listar Livros")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Título do livro: ")
            nome_autor = input("Nome do autor: ")
            nacionalidade = input("Nacionalidade do autor: ")
            data_nascimento = input("Data de nascimento do autor (dd/mm/aaaa): ")
            ano_publicacao = int(input("Ano de publicação: "))

            autor = Autor(nome_autor, nacionalidade, data_nascimento)
            livro = Livro(titulo, autor, ano_publicacao)
            biblioteca.adicionarLivro(livro)

        elif opcao == "2":
            titulo = input("Título do livro a remover: ")
            biblioteca.removerLivro(titulo)

        elif opcao == "3":
            titulo = input("Título do livro a buscar: ")
            biblioteca.buscarLivro(titulo)

        elif opcao == "4":
            biblioteca.listarLivros()

        elif opcao == "5":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
