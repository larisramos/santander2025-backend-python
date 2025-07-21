curso = "pYthon"

print(curso.upper()) #CAIXA ALTA: MAIUSCULA
print(curso.lower()) # Todas minusculas
print(curso.title()) # Primeira Maiuscula. Como em um título.

# Eliminando espaços em branco
curso2 = "    Python Santander  "

print(curso2.strip()) # Remove espaço em branco
print(curso2.lstrip()) # Remove o espaço em branco da esquerda.
print(curso2.rstrip()) # Remove o espaço em branco da direita.

#Junções e Centralização
curso1 = "Python"

print(curso1.center(10, "#")) #Aqui alinhamos ao centro e demos os parametros de 10 caracteres (python contem 6), ou seja, haverá 4 caracteres adicionados do #. Neste espaço também podemos deixar em branco.
print(".".join(curso1)) # SAIDA: P.y.t.h.o.n  | Apontamos primeiro o que desejamos inserir entre as strings, após apontamos o metódo join e por fim definimos que ele será aplicavel na variavel curso1.
