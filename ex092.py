from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nacsicmento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de trabalho (0 Não tem): '))
print('=-=' * 30)
for k, v in dados.items():
    print(f'- {k} tem valor {v}')
