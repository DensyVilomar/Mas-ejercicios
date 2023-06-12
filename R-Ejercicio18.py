def search_names(list_of_names,letter):
    
    cont = 0
    
    for names in list_of_names:
        if names.startswith(letter.upper()):
            cont += 1
            print(names) ### Innecesario ###
                
    if len(letter) > 1:
        print("Introduzca una sola letra.")
    else:  
        print(f"Hay {cont} nombres que inician con la letra {letter.upper()}.")
                
lis = ["Densy","Jose","Daniela","Darlin","Manuel","Gilbert","Samara","Jesus","Marcos","Samuel"]

search_names(lis,"d")