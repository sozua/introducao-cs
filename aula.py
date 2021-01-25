print(type(10)) # <class 'int'>
print(type(10)) # <class 'int'>
print(type(5 / 2)) # <class 'float'>

peso = 78
altura = 1.78

imc = peso / (altura ** 2)

print(imc)
print(type(imc)) # <class 'float'>

imcInteiro = int(imc)

print(imcInteiro)
print(type(imcInteiro))

temp = str(imc)
print(temp)
print(type(temp))
print(len(temp)) # Comprimento do float