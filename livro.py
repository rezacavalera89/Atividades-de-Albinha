from autor import Autor
class Livro:
    def __init__(self, titulo: str, autor: Autor, anoPublicacao: int):
        self._titulo = titulo
        self._autor = autor
        self._anoPublicacao = anoPublicacao

    def get_titulo(self) -> str:
        return self._titulo

    def set_titulo(self, titulo: str):
        self._titulo = titulo

    def get_autor(self) -> Autor:
        return self._autor

    def set_autor(self, autor: Autor):
        self._autor = autor

    def get_anoPublicacao(self) -> int:
        return self._anoPublicacao

    def set_anoPublicacao(self, anoPublicacao: int):
        self._anoPublicacao = anoPublicacao
