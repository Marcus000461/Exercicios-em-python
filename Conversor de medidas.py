medida = float(input("Digite uma distancia em metros:"))
cm = medida * 100
mm = medida * 1000
km = medida / 1000
hec = medida / 100
dam = medida / 10
print('A media de {:.0f}cm corresponde a {:.0f}mm a de {:0f} km e de {:.0f}hec e também de {:.0f} dam'.format(medida,cm,km,hec,dam))
