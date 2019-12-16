total_idade_ = 0
max_idade_homem_ = 0
max_nome_homem_ = ''
cont_mul_ = 0
for p_ in range(1, 5):
    print(5 * '-', '{}ª PESSOA'.format(p_), 5 * '-')
    name_ = str(input('Nome: '))
    age_ = float(input('Idade: '))
    sex_ = str(input('Sexo [M/F]: ')).upper().strip()
    total_idade_ += age_
    med_ = total_idade_ / p_
    if sex_ == 'M':
        if age_ > max_idade_homem_:
            max_idade_homem_ = age_
            max_nome_homem_ = name_
    elif sex_ == 'F' and age_ < 20:
        cont_mul_ += 1

print('A média de idade do grupo é {:.2f} anos'.format(med_))
print('O homem mais velho tem {} anos de idade e se chama {}'.format(max_idade_homem_, max_nome_homem_))
print('Tem {} mulher(es) com menos de 20 anos'.format(cont_mul_))
