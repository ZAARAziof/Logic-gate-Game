def AND_gate(input1, input2):
    return input1 & input2

def OR_gate(input1, input2):
    return input1 | input2

def XOR_gate(input1, input2):
    return input1 ^ input2

def NOT_gate(input1):
    return 1 - input1

def perform_operation(expression):
    # Convert binary strings to integers
    operand1, operator, operand2 = expression.split()
    operand1 = int(operand1, 2)
    operand2 = int(operand2, 2)

    if operator == 'AND':
        result = AND_gate(operand1, operand2)
    elif operator == 'OR':
        result = OR_gate(operand1, operand2)
    elif operator == 'XOR':
        result = XOR_gate(operand1, operand2)
    else:
        return "Invalid Operator!"

    return bin(result)[2:]  # Return result in binary format

def start_game():
    print("Welcome to the Binary Circuit Challenge! 🧠")
    print("You’ll solve binary expressions using logic gates. Can you handle the challenge?")

    # Sample expressions
    expressions = [
        "1101 AND 1010",
        "1010 OR 0110",
        "1001 XOR 0110"
    ]

    # Loop through and challenge the player
    for expr in expressions:
        print("\nSolve this binary circuit:")
        print(f"Expression: {expr}")
        player_answer = input("Your answer (in binary): ")

        # Get the correct answer
        correct_answer = perform_operation(expr)
        
        if player_answer == correct_answer:
            print("Correct! 🎉 You solved it!")
        else:
            print(f"Oops! The correct answer is: {correct_answer}")

# Start the game
if __name__ == "__main__":
    start_game()
