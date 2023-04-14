
"""for variavel in range(5):
    print(variavel)"""

"""for variavel in range(1,10):
    print(variavel)"""

"""for variavel in range(1,10,2):
    print(variavel)"""

"""nota1 = float(input("Informe nota 1ºBimestre"))
nota2 = float(input("Informe nota 2º Bimestre"))
nota3 = float(input("Informe nota 3º Bimestre"))"""

soma = 0 
for i in range(1, 5):
    nota = float(input(f"Informe sua nota {i} Bimestre: "))

    soma = soma + nota

print(soma / 4)

if soma / 4 >= 7:
    print("Aprovado")
elif soma / 4 >= 5:
    print("Recuperação")
else:
    print("Reprovado")


