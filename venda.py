from produto import Produto
class Venda:
    def __init__(self, dataVenda: str):
        self._produtos = []
        self._dataVenda = dataVenda
        self._total = 0.0

    def get_produtos(self):
        return self._produtos

    def set_produtos(self, produtos):
        self._produtos = produtos

    def get_dataVenda(self) -> str:
        return self._dataVenda

    def set_dataVenda(self, dataVenda: str):
        self._dataVenda = dataVenda

    def get_total(self) -> float:
        return self._total

    def set_total(self, total: float):
        self._total = total

    def adicionarProduto(self, produto: Produto):
        self._produtos.append(produto)
        self.calcularTotal()

    def removerProduto(self, nome: str):
        for produto in self._produtos:
            if produto.get_nome().lower() == nome.lower():
                self._produtos.remove(produto)
                self.calcularTotal()
                print(f"Produto '{nome}' removido com sucesso!")
                return
        print(f"Produto '{nome}' não encontrado.")

    def listarProdutos(self):
        if not self._produtos:
            print("Nenhum produto na venda.")
        else:
            print(f"Produtos na venda (Data: {self._dataVenda}):")
            for produto in self._produtos:
                print(f"{produto.get_nome()} - R${produto.get_preco():.2f} - Quantidade: {produto.get_quantidade()}")
            print(f"Total da venda: R${self._total:.2f}")

    def calcularTotal(self):
        self._total = sum(produto.get_preco() * produto.get_quantidade() for produto in self._produtos)
