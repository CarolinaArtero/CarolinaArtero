
#ESTRUTURAS CONDICIONAIS
"""
idade = 18

if idade >= 18:
    print("Você é maior de idade!")
else: 
    print("Você é menor de idade!")

altura = float(input("Informe a sua altura em cm:"))

if altura >= 165:
    print("Você consegue pegar o potinho em cima do armário :P ")
else:
    print("Tampinha de garrafa")
"""
"""
media = float(input("Informe a media do aluno: "))
if media >= 7:
    print("Você foi aprovado(a)")
elif media >=5:
    print("Você ficou de recuperação!")
else:
    print("Você foi reprovado!")
"""
#operadores ternários
#print("Você consegue pegar o potinho em cima do armário :P ") if altura >= 165 else print("Tampinha de garrafa")

media = float(input("Coloque sua média: "))
presenca = float(input("Seu percentual de frequência:"))

if media >= 7 and presenca >= 70:
    print("Aprovado")
elif media >= 5 and presenca >= 50:
    print("Recuperação")
else: 
    print("Reprovado")
    