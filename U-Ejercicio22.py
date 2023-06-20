def interes_anual(amount,interest,years):
    
    final_value = amount * (1 + interest/100) ** years
    return final_value

print(interes_anual(10000,4.5,20))