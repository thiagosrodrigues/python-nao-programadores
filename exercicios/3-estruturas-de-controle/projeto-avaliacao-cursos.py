# Nesse desafio você verificará dentro de uma lista se o item estar contido nela, caso verdadeiro deverá imprimir na tela essa informação, além disso deverá solicitar avaliação para o item e armazená-la em um dicionário.
# 1. Crie uma lista com 5 diferentes cursos do LinkedIn Learning
# 2. Crie 3 variáveis do tipo string e associe 1 curso a cada uma delas
# 3. Crie um dicionário vazio para armazenar a nota do curso
# 4. Crie uma estrutura condicional para verificar se cada variável está contida na lista
# 5. Se o curso estiver na lista, solicite uma nota para avaliação
# 6. Armazene essa nota no dicionário, sendo a chave o título do curso e o valor a nota

cursos = ['python', 'sql', 'excel', 'python: basico', 'programação']
curso_python = 'python'
curso_git = 'git'
curso_excel = 'excel'

notas_cursos = {}

if curso_python in cursos:
  print(f"O curso {curso_python} consta no catálogo. Por favor avalie o curso")
  notas_cursos[curso_python] = int(input('Qual a nota do curso? '))
if curso_git in cursos:
  print(f"O curso {curso_git} consta no catálogo. Por favor avalie o curso")
  notas_cursos[curso_git] = int(input('Qual a nota do curso? '))
if curso_excel in cursos:
  print(f"O curso {curso_excel} consta no catálogo. Por favor avalie o curso")
  notas_cursos[curso_python] = int(input('Qual a nota do curso? '))
else:
  print("Infelizmente curso não consta catálogo.")

  print(notas_cursos)