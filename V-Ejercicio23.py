import random

while True:

    try:
        cantidad_compra = float(input("Total de su compra: $"))
    except ValueError:
        print("Introduce un numero.")
        continue

    if cantidad_compra < 100:
        print("No aplica a la promocion.")
    else:
        numero_random = random.randint(1,5)
        if numero_random == 1:
            print("Has obetinido la bola amarilla.")
            print("Tu descuento es de 20%")
            print(f"Cantidad a pagar despues del descuento: {cantidad_compra - ((20 / 100) * cantidad_compra)}")
        elif numero_random == 2:
            print("Has obetinido la bola roja.")
            print("Tu descuento es de 10%")
            print(f"Cantidad a pagar despues del descuento: {cantidad_compra - ((10 / 100) * cantidad_compra)}")
        elif numero_random == 3:
            print("Has obetinido la bola azul.")
            print("Tu descuento es de 25%")
            print(f"Cantidad a pagar despues del descuento: {cantidad_compra - ((25 / 100) * cantidad_compra)}")
        elif numero_random == 4:
            print("Has obetinido la bola verde.")
            print("Tu descuento es de 50%")
            print(f"Cantidad a pagar despues del descuento: {cantidad_compra - ((50 / 100) * cantidad_compra)}")
        else:
            print("Has obtenido la bola blanca.")
            print("No obtienes ningun descuento.")
            
    break