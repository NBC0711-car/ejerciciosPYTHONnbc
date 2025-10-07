pPayaso = 112
pMuñeca = 75
nPayaso = int(input('Numero de payasos vendidos: '))
nMuñeca = int(input('Numero de muñecas vendidas: '))
pTotal = (nPayaso * pPayaso) + (nMuñeca * pMuñeca)
print(f'El peso total es: {pTotal}g')