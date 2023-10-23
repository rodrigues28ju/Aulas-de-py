from typing import List, Dict
from time import sleep

from models.produto import Produto
from utils.helper import formata_float_str_moeda

import os

produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []

def main() -> None:
    menu()

def limpar():
    os.system('cls')

def menu() -> None:
    print('*' * 20)
    print('*** Boas vindas! ***')
    print('*' * 20)
    print('')
    print('Selecione uma opção abaixo:')
    print('1) Cadastrar produto')
    print('2) Listar produto')
    print('3) Comprar produto')
    print('4) Visualizar carrinho')
    print('5) Fechar pedido')
    print('6) Sair do sistema')
    print('')
    print('*' * 20)
    print('')
    opcao = int(input('Digite a sua opção: '))
    print('')
    print('*' * 20)
    print('')

    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produtos()
    elif opcao == 3:
        comprar_produto()
    elif opcao == 4:
        visualizar_carrinho()
    elif opcao == 5:
        fechar_pedido()
    elif opcao == 6:
        print('Volte sempre :o)')
        sleep(2)
        exit(0)
    else:
        print('Opção inválida!')
        sleep(1)
        menu()

def cadastrar_produto() -> None:
    print('Cadastro de produto')
    print('')
    print('*' * 20)
    print('')

    nome: str = input('Informe o nome do produto: ')
    preco: float = float(input('Informe o preço do produto: R$'))
    produto: Produto = Produto(nome, preco)

    produtos.append(produto)

    print('')
    print(f'O produto {produto.nome} foi cadastrado com sucesso!')
    print('')
    sleep(2)
    menu()

def listar_produtos() -> None:
    if len(produtos) > 0:
        print('Listagem de produtos')
        print('')
        print('*' * 20)
        print('')
        for produto in produtos:
            print(produto)
            print('')
            print('*' * 20)
            print('')
            sleep(1)
    else:
        print('Ainda não existem produtos cadastrados.')
    sleep(2)
    menu()

def comprar_produto() -> None:
    if len(produtos) > 0:
        print('*' * 20)
        print('* PRODUTOS DISPONÍVEIS *')
        for produto in produtos:
            print(produto)
            print('')
            print('*' * 20)
            print('')
            print('Informe o código do produto para adicionar ao carrinho: ')
            sleep(1)

        codigo: int = int(input())
        produto: Produto = pega_produto_por_codigo(codigo)

        if produto:
            if len(carrinho) > 0:
                tem_no_carrinho: bool = False
                for item in carrinho:
                    quant: int = item.get(produto)
                    if quant:
                        item[produto] = quant + 1
                        print('')
                        print(f'O produto {produto.nome} agora possui {quant + 1} unidades no carrinho.')
                        print('')
                        tem_no_carrinho = True
                        sleep(2)
                        menu()
                if not tem_no_carrinho:
                    prod = {produto: 1}
                    carrinho.append(prod)
                    print('')
                    print(f'O produto {produto.nome} foi adicionado ao carrinho.')
                    print('')
                    sleep(2)
                    menu()
            else:
                item = {produto: 1}
                carrinho.append(item)
                print('')
                print(f'O produto {produto.nome} foi adicionado ao carrinho.')
                print('')
                sleep(2)
                menu()
        else:
            print('')
            print(f'O produto com código {codigo} não foi encontrado.')
            print('')
            sleep(2)
            menu()
    else:
        print('')
        print('Ainda não existem produtos para vender.')
        print('')
        sleep(2)
        menu()

def visualizar_carrinho() -> None:
    if len(carrinho) > 0:
        print('Produtos no carrinho: ')

        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                print('-----------------------')
                sleep(1)
    else:
        print('Ainda não existem produtos no carrinho.')
        print('')
    sleep(2)
    menu()

def fechar_pedido() -> None:
    if len(carrinho) > 0:
        valor_total: float = 0

        print('Produtos do Carrinho')
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                valor_total += dados[0].preco * dados[1]
                print('------------------------')
                sleep(1)
        print(f'Sua fatura é {formata_float_str_moeda(valor_total)}')
        print('Volte sempre!')
        carrinho.clear()
        sleep(5)
    else:
        print('Ainda não existem produtos no carrinho.')
        sleep(2)
        menu()

def pega_produto_por_codigo(codigo: int) -> Produto:
    p: Produto = None

    for produto in produtos:
        if produto.codigo == codigo:
            p = produto
    return p

if __name__ == '__main__':
    main()