def max_de_tres(a,b,c):
    num = None
    
    if a > b and a > c:
        num = a 
        
    elif b > a and b > c:
        num = b
    
    else:
        num = c
        
    return num

print(max_de_tres(100,555,8123))