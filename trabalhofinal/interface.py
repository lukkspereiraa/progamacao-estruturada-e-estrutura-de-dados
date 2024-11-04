import sys
from main import GerenciamentoProdutos

# Instancia o gerenciamento de produtos
gerente = GerenciamentoProdutos()

def mostrar_menu():
    """
    Exibe o menu principal do sistema de gerenciamento de produtos.
    """
    print("\n=== Gerenciamento de Produtos ===")
    print("1. Cadastrar produto")
    print("2. Buscar produto por nome")
    print("3. Buscar produto por código de barras")
    print("4. Listar produtos ordenados por nome")
    print("5. Listar produtos ordenados por preço")
    print("6. Reabastecer produto")
    print("7. Vender produto")
    print("8. Adicionar pedido")
    print("9. Atender pedido")
    print("10. Remover produto")
    print("11. Gerar relatório")
    print("0. Sair")
    print("============================")

def cadastrar_produto():
    """
    Solicita os dados de um novo produto ao usuário e o cadastra no sistema.
    """
    nome = input("Digite o nome do produto: ")
    categoria = input("Digite a categoria do produto: ")
    preco = float(input("Digite o preço do produto: "))
    codigo_barras = input("Digite o código de barras do produto: ")

    produto = {
        "nome": nome,
        "categoria": categoria,
        "preco": preco,
        "codigo_barras": codigo_barras
    }

    gerente.cadastrar_produto(produto)
    print(f"Produto '{nome}' cadastrado com sucesso!")

def buscar_por_nome():
    """
    Solicita o nome de um produto e busca por ele no sistema.
    """
    nome = input("Digite o nome do produto: ")
    produto = gerente.buscar_por_nome(nome)
    if produto:
        print(f"Produto encontrado: {produto}")
    else:
        print(f"Produto com nome '{nome}' não encontrado.")

def buscar_por_codigo_barras():
    """
    Solicita o código de barras de um produto e busca por ele no sistema.
    """
    codigo_barras = input("Digite o código de barras do produto: ")
    produto = gerente.buscar_por_codigo_barras(codigo_barras)
    if produto:
        print(f"Produto encontrado: {produto}")
    else:
        print(f"Produto com código de barras '{codigo_barras}' não encontrado.")

def listar_produtos_por_nome():
    """
    Lista todos os produtos cadastrados no sistema, ordenados por nome.
    """
    produtos = gerente.listar_produtos(key="nome")
    print("Produtos ordenados por nome:")
    for produto in produtos:
        print(produto)

def listar_produtos_por_preco():
    """
    Lista todos os produtos cadastrados no sistema, ordenados por preço de forma decrescente.
    """
    produtos = gerente.listar_produtos(key="preco", reverse=True)
    print("Produtos ordenados por preço (decrescente):")
    for produto in produtos:
        print(produto)

def reabastecer_produto():
    """
    Solicita o nome de um produto e realiza o reabastecimento do estoque.
    """
    nome = input("Digite o nome do produto a ser reabastecido: ")
    produto = gerente.buscar_por_nome(nome)
    if produto:
        gerente.reabastecer(produto)
        print(f"Produto '{nome}' reabastecido com sucesso!")
    else:
        print(f"Produto com nome '{nome}' não encontrado.")

def vender_produto():
    """
    Realiza a venda de um produto, retirando-o do estoque.
    """
    produto = gerente.vender_produto()
    if produto:
        print(f"Produto vendido: {produto}")
    else:
        print("Nenhum produto para vender.")

def adicionar_pedido():
    """
    Adiciona um novo pedido de um produto com base no nome fornecido pelo usuário.
    """
    nome = input("Digite o nome do produto a ser adicionado ao pedido: ")
    produto = gerente.buscar_por_nome(nome)
    if produto:
        gerente.adicionar_pedido(produto)
        print(f"Pedido adicionado para o produto '{nome}'.")
    else:
        print(f"Produto com nome '{nome}' não encontrado.")

def atender_pedido():
    """
    Atende um pedido, retirando-o da lista de pendentes.
    """
    pedido = gerente.atender_pedido()
    if pedido:
        print(f"Pedido atendido: {pedido}")
    else:
        print("Nenhum pedido para atender.")

def remover_produto():
    """
    Solicita o nome e o código de barras de um produto e o remove do sistema.
    """
    nome = input("Digite o nome do produto a ser removido: ")
    codigo_barras = input("Digite o código de barras do produto a ser removido: ")
    gerente.remover_produto(nome, codigo_barras)
    print(f"Produto '{nome}' removido com sucesso!")

def gerar_relatorio():
    """
    Gera um relatório com informações sobre os produtos cadastrados.
    """
    gerente.gerar_relatorio()

def main():
    """
    Função principal que controla o loop do sistema de gerenciamento de produtos.
    O usuário escolhe uma das opções disponíveis no menu.
    """
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_produto()
        elif opcao == '2':
            buscar_por_nome()
        elif opcao == '3':
            buscar_por_codigo_barras()
        elif opcao == '4':
            listar_produtos_por_nome()
        elif opcao == '5':
            listar_produtos_por_preco()
        elif opcao == '6':
            reabastecer_produto()
        elif opcao == '7':
            vender_produto()
        elif opcao == '8':
            adicionar_pedido()
        elif opcao == '9':
            atender_pedido()
        elif opcao == '10':
            remover_produto()
        elif opcao == '11':
            gerar_relatorio()
        elif opcao == '0':
            print("Saindo...")
            sys.exit()  # Encerra o programa
        else:
            print("Opção inválida, tente novamente!")

if __name__ == '__main__':
    main()
