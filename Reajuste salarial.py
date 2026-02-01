salário = float(input('Qual é o salário do Funcionario? R$'))
novo_salário = salário + (salário * 15/100)
print('O funcionario que antes ganhava R${:.2f}, agora com 15% de aumento ganha R${:.2f}'.format(salário,novo_salário))
