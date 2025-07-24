nome = "Larissa"
idade = 30
profissao = "Designer"
linguagem = "Python"

# Método de saída antigo
print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculada no curso de %s." % (nome, idade, profissao, linguagem))

# Método de saída format
print() #pula a linha
print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculada no curso de {}." .format(nome, idade, profissao, linguagem)) 
print() #pula a linha
print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculada no curso de {linguagem}." .format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))

# Método F-STRING
print() #pula a linha
print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculada no curso de {linguagem}.")

# Formatando strings com casas decimais
PI = 3.14159 # Quando a variavel está em maiúscula é porquê representa uma constante.

print(f"\nValor de PI: {PI:.2f}" )