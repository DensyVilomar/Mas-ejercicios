def interes_anual(amount,interest,years):
    
    value = amount * (1 + interest/100) ** years
    return value

print(interes_anual(10000,4.5,20))