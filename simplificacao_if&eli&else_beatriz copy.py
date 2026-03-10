preco_frutas = {
    'maçã': 2.5,
    'Banana': 1.8,
    'Laranja': 3.0
}

fruta_desejada = 'maçã'

resultado = preco_frutas.get(fruta_desejada, 'fruta não encontrada')


print(f"O preço da {fruta_desejada} é R${resultado}")
