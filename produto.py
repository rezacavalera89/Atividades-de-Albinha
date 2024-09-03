class Produto:
    def __init__(self, nome: str, preco: float, quantidade: int):
        self._nome = nome
        self._preco = preco
        self._quantidade = quantidade

    def get_nome(self) -> str:
        return self._nome

    def set_nome(self, nome: str):
        self._nome = nome

    def get_preco(self) -> float:
        return self._preco

    def set_preco(self, preco: float):
        self._preco = preco

    def get_quantidade(self) -> int:
        return self._quantidade

    def set_quantidade(self, quantidade: int):
        self._quantidade = quantidade
