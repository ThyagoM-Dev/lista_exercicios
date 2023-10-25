# Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e mostre-a expressa apenas em dias.
from datetime import datetime

def usando_datetime(): # Resolucao mais simprificada e avancada da questao 3
    nome = input('qual o seu nome: ')
    dia = int(input('qual dia voce nasceu: '))
    mes = int(input('de que mes: '))
    ano = int(input('de que ano: '))
    nascimento = datetime(day=dia, month=mes, year=ano)
    dateatual = datetime(2023,10,25)
    difededatas = (dateatual - nascimento).days

    print (difededatas)
    print ('\n',nome, 'Nasceu no dia',dia,'do',mes,'de',ano, 'e com base nessa informacao',nome,'tem',difededatas,'em dias percorrido na terra.')

def forma_complexa_e_errada():
    nome = input('qual o seu nome: ')
    dia = int(input('qual dia voce nasceu: '))
    mes = int(input('de que mes: '))
    ano = int(input('de que ano: '))
    anoatual = 2023
    anosubtraido = anoatual - (ano)
    mesatual = 10
    diaatual = 25
    mesesemdia = 0
    diasdesobra  = abs(diaatual - (dia))
    mesessubtraidos = abs(mesatual - mes)

    if anoatual < ano:
        print ('\ndata invalida')
    elif mes > mesatual:
        anosubtraido = anosubtraido - 1
        mesessubtraidos = 12 - mesessubtraidos
    elif mes == mesatual: # o mes e o mesmo
        if diaatual < dia:
            anosubtraido = anosubtraido - 1

    anosemdias = anosubtraido * 360

    if mesessubtraidos > 0:
        if dia < diaatual:
            diasdesobra = diaatual - dia
            mesesemdia = mesessubtraidos * 30

    totalizador = anosemdias + mesesemdia + diasdesobra
    print ('\n',nome, 'Nasceu no dia',dia,'do',mes,'de',ano, 'e com base nessa informacao',nome,'tem',totalizador,'em dias percorrido na terra.')

usando_datetime()
forma_complexa_e_errada()