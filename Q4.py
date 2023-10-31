# Faça um algoritmo que leia a idade de uma pessoa expressa em dias e mostre
# a expressa em anos, meses e dias.

# import datetime

numeros_De_dias = int(input('infome quantidades de dias que tens: '))
anos = numeros_De_dias // 365
dias_restantes_do_ano = (numeros_De_dias - anos * 365)
meses = dias_restantes_do_ano // 30
dias = dias_restantes_do_ano - meses * 30

print (anos,'ano',meses,'mes',dias,'dia') 