from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nacsicmento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de trabalho (0 Não tem): '))
if dados["ctps"] != 0:
    dados['contratacao'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário: '))
    dados['aposentadoria'] = (dados["contratacao"] + 50) - nasc
print('=-=' * 30)
for k, v in dados.items():
    print(f'- {k} tem valor {v}')
