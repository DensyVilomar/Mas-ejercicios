def analiza_cadena(cadena):
    
    mayusculas = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    contador = 0
    
    for letter in cadena:
        if letter in mayusculas:
            contador += 1
    print(f"Hay {contador} mayusculas en esta palabra.")

analiza_cadena("OrNiTOrrinCo")

def otra_manera(cadena):
    cont = 0
    
    for i in cadena:
        if i != i.lower():
            cont += 1
    print(cont)
            
otra_manera("HolA")        