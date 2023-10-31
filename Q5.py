# Faça um algoritmo que leia as 3 notas de um aluno e calcule a média final deste aluno.
# Considerar que a média é ponderada e que o peso das notas é: 2,3 e 5, respectivamente

aluno = "carlos"
primeirobm = (2.3)
segundobm = (2.3)
terceirobm = (2.3)
media = int(5)

totalNota = primeirobm + segundobm + terceirobm
totalMedia = media

totalfinal = totalNota 

if totalNota >= totalMedia:
    print ('parabens ' + aluno + ', voce foi aprovado')
else:
    print (aluno + ', infelizmente voce foi reprovado')