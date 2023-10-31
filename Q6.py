# Faça um algoritmo que leia o tempo de duração de um evento em uma fábrica
# expressa em segundos e mostre-o expresso em horas, minutos e segundos.

meta_diaria = (28800)
uma_hora_em_segundos = (3600)
minutos = (60)
segundos = (60)
hora_trabalhada = float(input('informe quantas horas voce trabalhou hoje: '))
segundos_trabalhados = hora_trabalhada * uma_hora_em_segundos
diario = segundos_trabalhados / minutos

if segundos_trabalhados < meta_diaria:
    print ('META -',meta_diaria,'-','voce nao atingiu a meta diaria e sera descontado no final do mes. -',hora_trabalhada,'hs',diario,'min',segundos_trabalhados,'seg')
elif segundos_trabalhados > meta_diaria:
    print (meta_diaria, ' voce atingiu um indice alto de trabalho e sera recompensado. -',hora_trabalhada,'hs',diario,'min',segundos_trabalhados,'seg')
else:
    print (meta_diaria, ' voce atingiu a meta diarira sem excesso. -',hora_trabalhada,'hs',diario,'min',segundos_trabalhados,'seg')
