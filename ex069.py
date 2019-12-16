idade_c_ = m_cont_ = f_cont_ = 0
while True:
    idade_ = int(input('Idade: '))
    sexo_ = ' '
    while sexo_ not in 'MF':
        sexo_ = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if idade_ > 18:
        idade_c_ += 1
    if sexo_ == 'M':
        m_cont_ += 1
    if sexo_ == 'F' and idade_ < 20:
        f_cont_ += 1
    print('-*-' * 10)
    request_ = ' '
    while request_ not in 'SN':
        request_ = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if request_ == 'S':
        continue
    else:
        break
print(f'Total de pessoas com mais de 18 anos: {idade_c_}')
print(f'Ao todo temos {m_cont_} homens cadastrados')
print(f'E temos {f_cont_} mulheres com menos de 20 anos')
