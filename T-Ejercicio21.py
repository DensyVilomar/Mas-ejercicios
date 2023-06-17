def rima_o_no(word,word2):
    if (word[-3:]) == word2[-3:]:
        print("Si rima.")
    elif (word[-2:]) == (word2[-2:]): 
        print("Rima un poco.")
    else: 
        print("No rima")
    
hola = "hola"    
rima_o_no("comida","soda")    