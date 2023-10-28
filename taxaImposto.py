# Importar as bibliotecas necessárias
import os

# Definir a classe Produto
class Produto:
    def __init__(self, valor, nome_do_item, quantidade):
        self.valor = valor
        self.nome_do_item = nome_do_item
        self.quantidade = quantidade

    def calcular_imposto(self):
        return self.valor * 0.15 * self.quantidade

    def calcular_valor_final(self):
        return self.valor + self.calcular_imposto()

# Definir um dicionário para armazenar os produtos
produtos = {}

# Função para cadastrar um produto
def cadastrar_produto():

    # Solicitar o nome do produto
    nome_do_item = input("Informe o nome do produto: ")
    
    # Solicitar o valor do produto
    try:
        valor = float(input("Informe o valor do produto: "))
    except ValueError:
        print("O valor do produto deve ser um número.")
        return

    # Solicitar a quantidade do produto
    try:
        quantidade = int(input("Informe a quantidade do produto: "))
    except ValueError:
        print("A quantidade do produto deve ser um número inteiro.")
        return

    # Criar um novo produto
    produto = Produto(valor, nome_do_item, quantidade)

    # Adicionar o produto ao dicionário
    produtos[produto.nome_do_item] = produto

# Função para listar todos os produtos
def listar_produtos():
    # Imprimir o cabeçalho da lista
    print("Lista de produtos:")
    print("-" * 20)

    # Iterar sobre o dicionário de produtos
    for nome_do_item, produto in produtos.items():
        # Imprimir o produto
        print("Nome do item: %s" % produto.nome_do_item)
        print("Valor: %.2f" % produto.valor)
        print("Quantidade: %d" % produto.quantidade)
        print("Imposto: %.2f" % produto.calcular_imposto())
        print("Valor final: %.2f" % produto.calcular_valor_final())
        print("-" * 20)

# Função principal
def main():
    # Opção do menu
    opcao = 0

    # Loop principal
    while opcao != 3:
        # Imprimir o menu
        print("Menu de opções:")
        print("1 - Cadastrar produto")
        print("2 - Listar produtos")
        print("3 - Sair")

        # Solicitar a opção do usuário
        opcao = int(input("Informe a opção desejada: "))

        # Executar a opção selecionada
        if opcao == 1:
            cadastrar_produto()
        elif opcao == 2:
            listar_produtos()

# Chamar a função principal
if __name__ == "__main__":
    main()
