def si_tiene_mas(lista,n):
    
    for i in lista:
        if len(i) > n:
            print(i)

mylis = ["hola","no","si","comida","panaderia"]

si_tiene_mas(mylis,4)