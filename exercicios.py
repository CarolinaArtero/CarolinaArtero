#QUESTÃO
"""
x = int(input("Digite um número inteiro: "))

if x<0:
    resp1 = ("negativo")
else:
    resp1 = ("positivo")    
if x%2==0:
    resp2 = ("par")
else:
    resp2 = ("impar")
    

print("o número {} é {} e {}".format(x, resp1, resp2))
"""
"""
lista_inicial = [10, 5, -7, 6, -42, 63, -8, -5, 13]

lista_final = []

for item in lista_inicial:

    if item % 2 == 0:

        if item < 0:

            lista_final.append(-item)
    
        else:

            lista_final.append(item)
    else:

        if item < 0:
            
            lista_final.append(-2*item)
    
        else:

            lista_final.append(2*item)
            print(lista_final)
        """