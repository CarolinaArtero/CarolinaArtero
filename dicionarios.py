#Dicionários
#criando dicionários
#dicionario = {}
#dicionario = dict{}
dicionario={'nome':"Carolina","idade":"23","altura":"1.68"}
print (dicionario)
print(dicionario["idade"])

#adicionar elementos em um dicionário

dicionario["programador"] = True
print(dicionario)

dicionario["altura"]= 1.70
print (dicionario)

for key in dicionario:
    print(key, dicionario[key])

#testando a existência de uma chave
print("peso" in dicionario)
print("altura" in dicionario)