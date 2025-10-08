precio = (input('precio del producto en euros y centimos(formato E.CC): '))
precioPartes = precio.split('.')
euros = precioPartes[0]
centimos = precioPartes[1]
print(f'son {euros}€ y {centimos} centimos')