# Parâmetros
def boasvindas(nome, quantidade):
    print(f'Bem vindo {nome}')
    print(f'A quantidade atual do produto é de {quantidade}')

# Argumentos
boasvindas('Marcos', 10)
boasvindas('Ronaldo', 12)
boasvindas('Linda', 16)

'''
Default: definido no parâmetro
Non-Default: Não definido no parâmetro

example: def boasvindas(nome, quantidade=6)
'''