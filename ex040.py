nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print('Com as notas {:.1f} e {:.1f} você obtve a média {:.1f}'.format(nota1, nota2, media))
if media < 5:
    print('O aluno foi REPROVADO!')
#elif media >= 5 and media <= 6.9:
elif 7 > media >= 5:
    print('RECUPERAÇÃO!')
else:
    print('APROVADO!')