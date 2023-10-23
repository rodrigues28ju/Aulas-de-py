# forma de passar o valor de uma função para que retorne
# como queremos
def formata_float_str_moeda(valor: float) -> str:
    return f'R${valor:,.2f}'