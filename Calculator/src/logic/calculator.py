def calculate_function(number_01, number_02, user_operator):
    operations = {
        "+": number_01 + number_02,
        "-": number_01 - number_02,
        "*": number_01 * number_02,
        "/": number_01 / number_02 if number_02 != 0 else "Error: Division by 0"
    }
    
    return operations.get(user_operator, "Invalid operator!")