print('\033[7;33m='*5, 'GroceryStore', '='*5, '\033[m')
print('{:=^40}'.format(' Grocery Store '))
v_preco = float(input('Preço das compras: R$'))
print('\033[4mFormas de Pagamento\033[m')
print('[ 1 ] à vista dinheiro/cheque\n[ 2 ] à vista cartão\n[ 3 ] 2x no cartão\n[ 4 ] 3x ou mais no cartão')
forma_ = int(input('Qual opção?\n'))
#v_parc = int(input('Quantas Parcelas'))
#if  v_fpag == 1:
if forma_ == 1:
   # result_ = v_preco - v_preco * 0.10
    result_ = v_preco - (v_preco * 10 / 100)
elif forma_ == 2:
    result_ = v_preco - ( v_preco * 5 / 100)
elif forma_ == 3:
    result_ = v_preco
    parcela = result_ / 2
    print('Sua compra foi parcelada em 2x de R${:.2f}.'.format(parcela))
elif forma_ == 4:
    result_ = v_preco + (v_preco * 20 / 100)
    qtd_parcela = int(input('Quantidade de parcelas? '))
    parcela = result_ / qtd_parcela
    print('Sua compra foi parcelada em {}x de R${:.2f}, COM JUROS.'.format(qtd_parcela, parcela))
print('O valor total das compras era R${:.2f} e passa a custar R${:.2f}'.format(v_preco, result_))
