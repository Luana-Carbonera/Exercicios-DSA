# Exercício 1 - Imprima na tela os números de 1 a 10. Use uma lista para armazenar os números.
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista)

# Exercício 2 - Crie uma lista de 5 objetos e imprima na tela
lista2 = ["obj1", "obj2", "obj3", "obj4", "obj5"]
print(lista2)

# Exercício 3 - Crie duas strings e concatene as duas em uma terceira string
string1 = "i love "
string2 = "data science"
string = string1 + string2
print(string)

# Exercício 4 - Crie uma tupla com os seguintes elementos: 1, 2, 2, 3, 4, 4, 4, 5 e depois utilize a função count do
# objeto tupla para verificar quantas vezes o número 4 aparece na tupla
tupla = (1, 2, 2, 3, 4, 4, 4, 5)
print(tupla.count(4))

# Exercício 5 - Crie um dicionário vazio e imprima na tela
dict = {}
print(dict)

# Exercício 6 - Crie um dicionário com 3 chaves e 3 valores e imprima na tela
dict1 = {"key1:v1", "key2:v2", "key3:v3"}
print(dict1)

# Exercício 7 - Adicione mais um elemento ao dicionário criado no exercício anterior e imprima na tela
dict1.add("key4:v4")
print(dict1)

# Exercício 8 - Crie um dicionário com 3 chaves e 3 valores. Um dos valores deve ser uma lista de 2 elementos numéricos.
# Imprima o dicionário na tela.
dictlist = {"c1:[1, 2]", "c2:v2", "c3:v3"}
print(dictlist)

# Exercício 9 - Crie uma lista de 4 elementos. O primeiro elemento deve ser uma string,
# o segundo uma tupla de 2 elementos, o terceiro um dcionário com 2 chaves e 2 valores e
# o quarto elemento um valor do tipo float.
# Imprima a lista na tela.
listao = ["string", ("tupla1, tupla2"), {"key1:v1", "key2:v2"}, 4.3]
print(listao)

# Exercício 10 - Considere a string abaixo. Imprima na tela apenas os caracteres da posição 1 a 18.
frase = "Cientista de Dados é o profissional mais sexy do século XXI"
print(frase[:18])
