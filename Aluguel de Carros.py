dias = int(input('Quantos dias você vai alugar o carro?'))
km = float(input('Quantos km você andou com o carro?'))
pago= (dias * 60) + (km *0.15)
print('O total a pagar é de R${:.2f}'.format(pago))
