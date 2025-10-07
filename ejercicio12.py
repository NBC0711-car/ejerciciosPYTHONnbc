pBarra = 3.49
dPorcentaje = 0.6
barras_no_dia = int(input('Numero de barras no frescas vendidas: '))
dEuros = pBarra * dPorcentaje
pFinal = pBarra * (1 + dPorcentaje)
cTotal = barras_no_dia * pFinal
print(f'Precio de una barra normal: {pBarra}')
print(f'Descuneto por no ser fresca: {dEuros}')
print(f'Coste final: {cTotal}')