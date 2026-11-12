import json
import csv

with open('data.json', 'r') as file:
    data = json.load(file)

print(data)

# ejercicio 1

for usuario, compras in data.items():
    total = 0

    for compra in compras:
        total += compra["precio"]

    print(f"{usuario}: {total:.2f} €")

# ejercicio 2

mayor_gasto = 0
cliente_vip = ""

for usuario, compras in data.items():
    total = 0

    for compra in compras:
        total += compra["precio"]

    if total > mayor_gasto:
        mayor_gasto = total
        cliente_vip = usuario

print(f"Cliente VIP: {cliente_vip}")
print(f"Gasto total: {mayor_gasto:.2f} €")

# ejercicio 3

mayor_cantidad = 0
cliente_mas_productos = ""

for usuario, compras in data.items():
    cantidad = len(compras)

    if cantidad > mayor_cantidad:
        mayor_cantidad = cantidad
        cliente_mas_productos = usuario

print(f"Cliente: {cliente_mas_productos}")
print(f"Cantidad de productos: {mayor_cantidad}")

# ejercicio 4

producto_mas_caro = None
producto_mas_barato = None

for usuario, compras in data.items():
    for compra in compras:

        if producto_mas_caro is None or compra["precio"] > producto_mas_caro["precio"]:
            producto_mas_caro = compra
            usuario_mas_caro = usuario

        if producto_mas_barato is None or compra["precio"] < producto_mas_barato["precio"]:
            producto_mas_barato = compra
            usuario_mas_barato = usuario

print("PRODUCTO MÁS CARO:")
print(f"{producto_mas_caro['producto']} - {producto_mas_caro['precio']:.2f} € - {usuario_mas_caro}")

print("PRODUCTO MÁS BARATO:")
print(f"{producto_mas_barato['producto']} - {producto_mas_barato['precio']:.2f} € - {usuario_mas_barato}")

# ejercicio 5

gastos_categoria = {}

for usuario, compras in data.items():
    for compra in compras:
        categoria = compra["categoria"]
        precio = compra["precio"]

        if categoria in gastos_categoria:
            gastos_categoria[categoria] += precio
        else:
            gastos_categoria[categoria] = precio

print(gastos_categoria)

# ejercicio 6

for usuario, compras in data.items():
    for compra in compras:
        compra["precioIVA"] = compra["precio"] * 1.21

print(data)

# ejercicio 7

with open("contabilidad_a.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)

    writer.writerow(["producto", "precioIVA"])

    for usuario, compras in data.items():
        for compra in compras:
            writer.writerow([compra["producto"], compra["precioIVA"]])
