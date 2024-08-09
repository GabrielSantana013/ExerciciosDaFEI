def numCaracteres(senha):
    if len(senha) >=8:
        return True
    else:
        return False

def procuraMaiuscula(senha):
    for i in senha:
        if i >='A' and i <='Z':
            return True
    return False

def procuraMinuscula(senha):
    for i in senha:
        if i >= 'a' and i <= 'z':
            return True
    return False

def procuraNum(senha):
    for i in senha:
        if i >='0' and i <='9':
            return True
    return False


def capitalizar(texto):
    text_final = ""
    maiusculo = False
    texto = texto.capitalize()
    for i in texto:
        if i == '.' or i == '!' or i == '?':
            maiusculo = True
        if maiusculo and i.isalpha():
            text_final += i.upper()
            maiusculo = False
        else:
            text_final += i
    return text_final