print('====== DESAFIO 04 ======')

a = input('Digite algo: ')
print('O tipo primitivo desse valor é: ',type(a))
print('Só tem espaços? ', a.isspace())
print('Esse valor é um numero? ', a.isnumeric())
print('É alfabético? ', a.isalpha())
print('É alfanumérico? ', a.isalnum())
print('Está em maiusculas? ',a.isupper())
print('Está em minusculas? ',a.islower())
print('Está capitalizada? ', a.istitle())


#print(a.isdecimal())
#print(a.isidentifier())
#print(a.isdigit())
#print(a.isascii())
#print(a.isprintable())