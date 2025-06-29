calc1 = float(input("Number1: "))
operator = input("Operator: ")
calc2 = float(input("Number2: "))

if operator == "*":
    result1 = calc1 * calc2
    print(round(result1, 2))
    
elif operator == "/":
    result2 = calc1 / calc2
    print(round(result2, 2))
    
elif operator == "+":
    result3 = calc1 + calc2
    print(round(result3, 2))
    
elif operator == "-":
    result4 = calc1 - calc2
    print(round(result4, 2))
    
else:
    print("Error! Try again.")