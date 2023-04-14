#LISTAS

#antes
nota1 = 7.3
nota2 = 8.5
nota3 = 5.6

#com lista
notas = [7.3, 8.5, 5.6]

#criando listas
lista = []
lista = list()
lista = [26, "carol", 3.14159, False]
lista_de_listas = [10, [1, 2, 3]]

#indexação e slices (fatiamento)

lista = [23, "carol", 3.14159, True]
print(lista[0]) #o 0 indica o primeiro item da lista
# o -1 indica o último elemento, -2 o penúltimo e assim sucessivamente.

#slices
lista = [10, 20, 30, 40, 50]
print(lista[0:3])
# o 0:3 indica o item 1 , 2 e 3 
print (lista [2:5])
print (lista[0:5:2])

#interações com FOR

#1. Ultilizando os próprios elementos da lista

for elemento in lista:
    print(elemento)

#2.Utilizando os índices:

print("Comprimento da lista: ",len(lista))

for i in range(len(lista)):
    print(lista[i])
    
#exercicio pratico
lista = [1, 2, 3, 4, 5, 6, 7, 8]
print (lista[0:7:2])
for i in range (len(lista)):
    print(lista[i])