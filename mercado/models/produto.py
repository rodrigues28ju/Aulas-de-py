from utils.helper import formata_float_str_moeda

class Produto:
    contador: int = 1
    # construtor do objeto
    def __init__(self:object, nome:str, preco:float) -> None:
        # primeiro o objeto e depois a ação
        self.__codigo:int = Produto.contador
        self.__nome: str = nome
        self.__preco: float = preco
        Produto.contador += 1

    #propriedades define retorno de cada propriedade
    # ao ser chamada

    @property
    def codigo(self:object) -> int:
        return self.__codigo

    @property
    def nome(self:object) -> str:
        return self.__nome

    @property
    def preco(self:object) -> float:
        return self.__preco

    # \n = <br> em html; quebra linha
    def __str__(self) -> str:
        return f'Código: {self.codigo} \nNome: {self.nome} \nPreço:{formata_float_str_moeda(self.preco)}'