# Faça um algoritmo que leia a idade de uma pessoa expressa em dias e mostre
# a expressa em anos, meses e dias.

numeros_De_dias = int(input('infome quantidaddes de dias que tens: '))
anos = numeros_De_dias // 365
dias_restantes_do_ano = (numeros_De_dias - anos * 365)
meses = dias_restantes_do_ano // 30
dias = dias_restantes_do_ano - meses * 30

print (anos,'ano',meses,'mes',dias,'dia') 




















'''
import datetime
ano = int(input('informe ano: '))
mes = int(input('informe mes: '))
dia = int(input('informe dia: '))

d1 = datetime.datetime(year=ano,month=mes,day=dia)
d2 = datetime.datetime.now()

diff = d2 - d1

days = diff.days
years, days = days // 365, days % 365
months, days = days // 30, days % 30

seconds = diff.seconds
hours, seconds = seconds // 3600, seconds % 3600
minutes, seconds = seconds // 60, seconds % 60

print("Desde {} passaram {} anos, {} meses, {} dias, {} horas, {} minutos e {} segundos".format(d1, years, months, days, hours, minutes, seconds))


No objeto diff teremos a diferença entre as datas. Pelo atributo day e seconds pegamos esta diferença 
em relação ao número de dias e segundos, respectivamente. Para saber a quantidade de anos, calculamos
a divisão inteira entre a quantidade de dias por 365 e atualizamos o valor de days para descontar a quantia 
relativa a esses anos. Com o mês, calculamos a divisão por 30 e atualizamos novamente a quantidade de dias.
Para as horas e minutos a lógica é exatamente a mesma, dividindo o número de segundos por 3600 e 60, respectivamente.

Vale lembrar que esta diferença é aproximada, pois não leva em considerações ano bissextos dentro do intervalo considerado,
nem a quantidade exata de dias em cada mês.

'''