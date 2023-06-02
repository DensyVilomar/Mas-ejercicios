def es_palindromo(palabra):
    word = ""
    indice = len(palabra) - 1
    
    while indice >= 0:
        word += (palabra[indice])
        indice -= 1
        
    if word == palabra:
        print(True)
    else:
        print(False)
<<<<<<< HEAD
               
es_palindromo("hola")
=======
            
es_palindromo("hola")
>>>>>>> 97fdfd1f5761517d67d3fec0b1f4bc48eeb3dd9a
