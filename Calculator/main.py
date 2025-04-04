def calculate_function(number_01, number_02, user_operator):
    operations = {
        "+": number_01 + number_02,
        "-": number_01 - number_02,
        "*": number_01 * number_02,
        "/": number_01 / number_02 if number_02 != 0 else "Error: Division by 0"
    }
    
    return operations.get(user_operator, "Invalid operator!")

while True:
    try:
        number_1 = float(input("Enter first number: "))
        operator = input("Enter operator(+ - * /): ").strip()
        number_2 = float(input("Enter second number: "))

        result = calculate_function(number_1, number_2, operator)
        print(result)
    except ValueError:
        print("Invalid input! Check number 1 and number 2!")
        
    again = input("Exit? (Y/N): ")
    if again.lower() != "n":
        print("Goodbye!")
        break