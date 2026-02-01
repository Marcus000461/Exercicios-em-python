real = float(input('Quanto de dinheiro você tem na carteira? R$ :'))
dolar = real / 5.26
euro = real/ 6.23
print('Com R${:.2f} você pode comprar U${:.2f}'.format(real,dolar))
print('Com R${:.2f} você pode comprar euro {:.2f}'.format(real,euro))