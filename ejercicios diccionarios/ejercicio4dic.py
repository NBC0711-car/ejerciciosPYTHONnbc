fecha = input("Introduce la fecha (DD/MM/AAAA): ")
partes_fecha = fecha.split("/")
dia = int(partes_fecha[0])
mes = int(partes_fecha[1])
ano = int(partes_fecha[2])
meses = {
    1: "enero",
    2: "febrero",
    3: "marzo",
    4: "abril",
    5: "mayo",
    6: "junio",
    7: "julio",
    8: "agosto",
    9: "septiembre",
    10: "octubre",
    11: "noviembre",
    12: "diciembre"
}
print(f"La fecha es {dia} de {meses[mes]} de {ano}")