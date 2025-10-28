sexo = input('con que te identificas, Hombre o Mujer (H/M): ')
nombreAl = input('Como te llamas? ')
if ( nombreAl[0] < 'M' and sexo == 'M' or nombreAl[0] > 'N' and sexo == 'H'):
    print('perteneces al grupo A')
else:
    print ('perteneces al grupo B')
