import random
import string

def gerar_senha(tamanho):
    letras = string.ascii_letters
    numeros = string.digits
    simbolos = string.punctuation

    caracteres = letras + numeros + simbolos

    senha = ""

    for i in range(tamanho):
        senha += random.choice(caracteres)

    return senha


print("Gerador de Senhas Seguras")

tamanho = int(input("Digite o tamanho da senha: "))

senha = gerar_senha(tamanho)

print("Senha gerada:", senha)
