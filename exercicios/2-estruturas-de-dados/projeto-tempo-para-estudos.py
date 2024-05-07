# Criaremos um script que imprimirá na tela o total de horas que uma pessoa estudou durante um determinado período:

# 1. Crie uma variável chamada "nome" e, usando o método input(), atribua a ela um nome;
nome = input('Qual é o seu nome? ')

# 2. Crie uma variável chamada "total_dias" e, usando o método input(), solicite o total de dias dedicados ao estudo por semana;
total_dias = input('Quantos dias você estuda? ')

# 3. Crie uma variável chamada "total_horas" e, usanod o método input(), solicite a média de horas estudada por dia;
total_horas = input('E por quantas horas? ')

# 4. Crie uma variável chamada "curso" e, usando o método input(), solicite o título do curso desejado;
curso = input('Qual o seu curso? ')

# 5. Imprima na tela uma frase informando o nome da estudante, o total_dias dedicados aos estudos, o total horas semanais e o curso.
total_dias = int(total_dias) #função input salva os valores como string, é necessário conversão para cálculo. 
total_horas = int(total_horas)
print(f'Olá {nome}, você estuda {total_dias} dias por semana, durante {total_horas} horas diariamente, isso dá em média {total_dias*total_horas} horas semanais para o curso {curso}')