from math import radians, sin, cos, tan
ângulo = float(input("Digite o ângulo que você deseja: "))
seno = sin(radians(ângulo))
print('O ângulo de {} têm o seno de {:.2f}'.format(ângulo, seno))
coseno = cos(radians(ângulo))
print('O ângulo de {} têm o coseno de {:.2f}'.format(ângulo, coseno))
tangente = tan(radians(ângulo))
print('O ângulo de {} têm a tangente de {:.2f}'.format(ângulo, tangente))

