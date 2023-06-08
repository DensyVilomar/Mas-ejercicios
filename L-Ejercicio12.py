def mas_larga(*args):
    mydit = {} 
    for elements in args:
        mydit[elements] = 0
        for letter in elements:
            mydit[elements] += 1
            
    print("La palabra mas larga es: ", max(mydit, key=mydit.get))
                
        
mas_larga("parancuritimicuaro","acidodesoxirribonucleico","endodoncia","endotelio","esternocleidomastoideo")

def me_quiero_morir(*lista):
    mas_larga = ""
    
    for i in lista:
        if len(i) > len(mas_larga):
            mas_larga = i
    
    return(mas_larga)

print(me_quiero_morir("parancuritimicuaro","acidodesoxirribonucleico","endodoncia","endotelio","esternocleidomastoideo"))