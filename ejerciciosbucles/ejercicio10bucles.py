numero = int(input('give me a number: '))

if numero > 1:
    for i in range(2, numero):
        if numero%i == 0:
            print('tu numero no es primo')
    else:
        print('numero primo')
else:
    print('no es primo')


        