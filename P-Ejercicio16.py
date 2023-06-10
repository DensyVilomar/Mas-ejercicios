def next_age():
    year = int(input("what year is this?\n"))
    for i in range(3):
        name = input("What's your name: ")
        your_year = int(input("When were you born: "))
        next_age = year - your_year
        print(f"{name} will be {next_age} years old this year.\n")
        
next_age()
