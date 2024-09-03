class Autor:
    def __init__(self, nome: str, nacionalidade: str, dataNascimento: str):
        self._nome = nome
        self._nacionalidade = nacionalidade
        self._dataNascimento = dataNascimento

    def get_nome(self) -> str:
        return self._nome

    def set_nome(self, nome: str):
        self._nome = nome

    def get_nacionalidade(self) -> str:
        return self._nacionalidade

    def set_nacionalidade(self, nacionalidade: str):
        self._nacionalidade = nacionalidade

    def get_dataNascimento(self) -> str:
        return self._dataNascimento

    def set_dataNascimento(self, dataNascimento: str):
        self._dataNascimento = dataNascimento

    def exibirAutor(self):
        print(f"Nome: {self._nome}")
        print(f"Nacionalidade: {self._nacionalidade}")
        print(f"Data de Nascimento: {self._dataNascimento}")
