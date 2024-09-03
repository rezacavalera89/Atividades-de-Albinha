from livro import *
class Biblioteca:
    def __init__(self):
        self._livros = []

    def adicionarLivro(self, livro: Livro):
        self._livros.append(livro)
        print(f"Livro '{livro.get_titulo()}' adicionado com sucesso!")

    def removerLivro(self, titulo: str):
        for livro in self._livros:
            if livro.get_titulo().lower() == titulo.lower():
                self._livros.remove(livro)
                print(f"Livro '{titulo}' removido com sucesso!")
                return
        print(f"Livro '{titulo}' não encontrado.")

    def buscarLivro(self, titulo: str):
        for livro in self._livros:
            if livro.get_titulo().lower() == titulo.lower():
                print(f"Livro encontrado: {livro.get_titulo()} - {livro.get_anoPublicacao()}")
                return livro
        print(f"Livro '{titulo}' não encontrado.")
        return None

    def listarLivros(self):
        if not self._livros:
            print("Nenhum livro na biblioteca.")
        else:
            print("Livros na biblioteca:")
            for livro in self._livros:
                print(f"{livro.get_titulo()} ({livro.get_anoPublicacao()}) - {livro.get_autor().get_nome()}")
