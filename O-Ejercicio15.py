def bin_a_int(binario):
    entero = 0
    
    for bit in binario:
        entero = entero * 2 + bit
    return entero

numero_binario = input("Ingrese un numero binario: ")
numero_entero = bin_a_int(numero_binario)
print(numero_entero)