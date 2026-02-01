preço = float(input('Leia o preço de um produto? R$'))
novo = preço - (preço *5/100)
print('O produto que custava  R${:.2f}, agora com o desconto de 5% custa R${:.2f}'.format(preço,novo))

