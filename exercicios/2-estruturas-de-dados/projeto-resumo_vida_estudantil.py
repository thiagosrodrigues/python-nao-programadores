# Nesse exercício coletaremos dados de uma estudante, armazenaremos em um dicionário e imprimiremos na tela esse dados em um formato amigável.

# 1. Solicite a estudante os seguintes dados: nome, ano que conheceu o LinkedIn, ano atual e os cursos realizados no LinkedIn Learning separados por virgula em ordem cronológica
# 2. Armazene esses dados em um dicionário
# 3. Imprima na tela uma string com as informações de nome, ano_conheceu_linkedin, total de anos transcurridos, total de cursos realizados e (apenas) o primeiro e último curso.

estudante = {}

estudante['nome'] = input('Informe seu nome completo:')
estudante['ano_linkedin'] = int(input('Ano que conheceu LinkedIn:'))
estudante['ano_atual'] = int(input('Informe ano atual:'))
cursos = input('Quais cursos realizados LinkedIn learning (separe por vírgula)?')

estudante['cursos'] = cursos.split(', ')

total_anos = estudante['ano_atual'] - estudante['ano_linkedin']
total_cursos = len(estudante['cursos'])

print(f"Olá {estudante['nome']}, desde {estudante['ano_linkedin']} você conhece o LinkedIn. Nesses {total_anos} anos, você realizou {total_cursos} cursos, sendo o primeiro curso {estudante['cursos'][0]} e o último curso foi {estudante['cursos'][-1] } ")