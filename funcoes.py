#Funçõ
#criação de funções
#Função inicial
#def #vem de define define o nome 

def saudacao():
    print("Seja bem-vindo!")
    print("Me chamo Carolina.")


saudacao()

#função com parametros

def saudacao(nome, idade):
    print(f"Seja Bem Vindo, {nome}!")
    print(f"Fofinha qual sua idade? {idade}")

saudacao("Gatinha","23")

#função com parametros default

def saudacao(nome, idade="23"):
    print(f"Seja Bem Vindo, {nome}!")
    print(f"Fofinha qual sua idade? {idade}")

saudacao("Gatinha","23")

#funções com retornos

def soma (num1, num2):
    return num1+num2
# depois do return independente do código ele encerra a função
resultado = soma (5,7)
print("O resultado da soma é: ", resultado)


def calculadora(num1, num2, operacao="+"):
    if operacao == "+":
        return num1+num2
    elif operacao == "-":
        return num1-num2
    elif operacao == "*":
        return num1*num2
    elif operacao == "/":
        return num1/num2
resultado = calculadora(10,20, "/")
print(resultado)