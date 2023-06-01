def calcula_long(parametro):
     counter = 0
     for i in parametro:
         counter += 1
     print(f"Hay {counter} elementos.")
            
fruits = ["banana", "manzana", True, 384, 23.2]        
calcula_long(fruits)

calcula_long("vamos a ver")