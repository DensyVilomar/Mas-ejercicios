def max_20(edades):
    for edad in edades:
        if edad >= 20:  print(edad, end=" ")

# x = (10,20,30,40,50,11,12,13,14,15)
# max_20(x)

### mis inventos ###

def prueba():
    lis = []
    while True:
        edades = input("Ingrese una edad (q) para salir: ")
        if edades == "q": break
        else:
            conv = int(edades)
            lis.append(conv)
            
    lis = tuple(lis)
    max_20(lis)
        
prueba()    