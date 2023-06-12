def cuenta_vocal(word):
    
    count_a = 0
    count_e = 0
    count_i = 0
    count_o = 0
    count_u = 0
    
    for letters in word.lower():
        if letters == "a":
            count_a += 1
        elif letters == "e":
            count_e += 1
        elif letters == "i":
            count_i += 1
        elif letters == "o":
            count_o += 1
        elif letters == "u":
            count_u += 1
    
    print("letters a: ",count_a)
    print("letters e: ",count_e)
    print("letters i: ",count_i)
    print("letters o: ",count_o)
    print("letters u: ",count_u)
    
cuenta_vocal("bAnANA")