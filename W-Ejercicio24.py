while True:
    
    print("Choose a product\n")
    
    print("Product          Code\n") 
    
    print("""T-shirt.......... 1\nBelt............. 2\nShoes............ 3\nPants............ 4\nSocks............ 5\nSkirts........... 6\nCaps............. 7\nSweater.......... 8\nTie.............. 9\nJacket........... 10\n""")
    
    t_shirt, belt, shoes, pants, socks, skirts, caps, sweater, tie,jacket, = 10, 20, 30, 40, 50, 60, 70, 80, 90, 10
    
    code = int(input("Insert a code: "))
    
    if code == 1:
        print(f"It costs: ${t_shirt}\n")
    elif code == 2:
        print(f"It costs: ${belt}\n")
    elif code == 3:
        print(f"It costs: ${shoes}\n")
    elif code == 4:
        print(f"It costs: ${pants}\n")
    elif code == 5:
        print(f"It costs: ${socks}\n")
    elif code == 6:
        print(f"It costs: ${skirts}\n")
    elif code == 7:
        print(f"It costs: ${caps}\n")
    elif code == 8:
        print(f"It costs: ${sweater}\n")
    elif code == 9:
        print(f"It costs: ${tie}\n")
    elif code == 10:
        print(f"It costs: ${jacket}\n")
    else:
        print("Insert a number between 1 and 10")
        exit()


    amount = int(input("Insert an amount: "))
    
    if code == 1:
        print(f"Total price: ${amount * t_shirt}\n")
    elif code == 2:
        print(f"Total price: ${amount * belt}\n")
    elif code == 3:
        print(f"Total price: ${amount * shoes}\n")
    elif code == 4:
        print(f"Total price: ${amount * pants}\n")
    elif code == 5:
        print(f"Total price: ${amount * socks}\n")
    elif code == 6:
        print(f"Total price: ${amount * skirts}\n")
    elif code == 7:
        print(f"Total price: ${amount * caps}\n")
    elif code == 8:
        print(f"Total price: ${amount * sweater}\n")
    elif code == 9:
        print(f"Total price: ${amount * tie}\n")
    elif code == 10:
        print(f"Total price: {amount * jacket}\n")
    else:
        print("Insert a number between 1 and 10")
        exit()
    
    again = input("Do you want to leave? (Y/N)\n").lower()
    
    if again == "y" or again == "yes":
        break
    else:
        continue