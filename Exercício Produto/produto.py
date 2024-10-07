class Produto:
    def __init__(self, codigo, nome, categoria, preco, quantidadeEstoque):
        self.codigo = codigo
        self.nome = nome
        self.categoria = categoria
        self.preco = preco
        self.quantidadeEstoque = quantidadeEstoque

    def get_codigo(self):
        return self.codigo
    
    def get_nome(self):
        return self.nome
    
    def get_categoria(self):
        return self.categoria
    
    def get_preco(self):
        return self.preco
    
    def get_quantidadeEstoque(self):
        return self.quantidadeEstoque
    
    def set_preco(self, novo_preco):
        print(f"\nNovo valor atribuído(a) a(o) {self.nome.capitalize()}!")
        print(f"Preço antigo: {self.preco:.2f}")
        self.preco = novo_preco
        print(f"Preço atual: {self.preco:.2f}\n")

    def vender(self, quantidade_vendida):
        if quantidade_vendida <= self.quantidadeEstoque:
            self.quantidadeEstoque -= quantidade_vendida
            total_venda = quantidade_vendida * self.preco
            print(f"Venda realizada: {quantidade_vendida} unidade(s) de {self.nome}. Estoque atualizado: {self.quantidadeEstoque}")
            print(f"Categoria: {self.categoria}")
            print(f"Preço unitário: R$ {self.preco:.2f}")
            print(f"Total da venda: R$ {total_venda:.2f}\n")
        else:
            print("Erro: Estoque insuficiente para realizar a venda.")

    def comprar(self, quantidade_comprada):
        self.quantidadeEstoque += quantidade_comprada
        print(f"{quantidade_comprada} unidade(s) de {self.nome} foram compradas.")
        print(f"Quantidade atual em estoque: {self.quantidadeEstoque}")

    def listar(self):
        print(f"\nNome da mercadoria: {self.get_nome()}")
        print(f"Categoria: {self.get_categoria()}")
        print(f"Quantidade em estoque: {self.get_quantidadeEstoque()}")
        print(f"Preço: {self.preco:.2f}\n")

produto1 = Produto(1, "CAMISA", "Vestuário", 79.90, 75)
produto2 = Produto(2, "CALÇA", "Vestuário", 119.90, 90)

produto1.listar()

produto1.vender(10)
produto1.comprar(20)

produto2.set_preco(99.90)