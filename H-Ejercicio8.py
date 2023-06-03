def dos_listas(a,b):
    for element in a:
     for element2 in b:
        if element == element2:
            return True
        
    return False
         
         
lista1 = [1,2,3,4,5,6,7] 

lista2 = [8,9,10,11,12,2] 

print(dos_listas(lista1,lista2))          