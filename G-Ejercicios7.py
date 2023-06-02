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
               
es_palindromo("hola")