dados_aluno = dict()
dados_aluno['Nome'] = str(input('Nome: '))
dados_aluno['Média'] = float(input(f'Média de {dados_aluno["Nome"]}: '))
if dados_aluno["Média"] >= 7:
    dados_aluno['situação'] = 'Aprovado'
elif 5 <=  dados_aluno["Média"] <7:
    dados_aluno['situação'] = 'Recuperação'
else:
    dados_aluno['situação'] = 'Reprovado'
print('=-=' * 30)
for k, v in dados_aluno.items():
    print(f' - {k} é igual a {v}')
