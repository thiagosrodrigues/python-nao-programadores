# Crie uma lista apenas com elementos numéricos
numerica = [1, 2, 3, 4, 5]
# Crie uma lista contendo todos os tipos e estrutura de dados que você aprendeu até agora
mista = [1, 'python', numerica]
# Imprima na tela apenas os 5 primeiros elementos da lista
print(numerica[0:5:1])
# Crie um slice na lista para que imprima na tela os elementos de índice par
# slice[inicio:fim:passo] por exemplo numerica[0:-1:2] O python entende o -1 como o último iten da lista
print(numerica[0:5:2])
# Remova da lista o último item
numerica.pop()
# Insira na lista um novo item
mista.append('thiago')
# Remova da lista um item específico
mista.remove(numerica)