def AND_gate(input1, input2):
    return input1 & input2

def OR_gate(input1, input2):
    return input1 | input2

def NOT_gate(input1):
    return 1 - input1

def NAND_gate(input1, input2):
    return 1 - (input1 & input2)

def NOR_gate(input1, input2):
    return 1 - (input1 | input2)

def XOR_gate(input1, input2):
    return input1 ^ input2

def create_circuit():
    print("Welcome to the Logic Gate Puzzle Master!")
    print("Your goal is to solve the logic gate puzzle by correctly combining gates to match the target output.")
    
    # Example puzzle: input1 = 1, input2 = 0, desired_output = 1
    input1 = int(input("Enter the first input (0 or 1): "))
    input2 = int(input("Enter the second input (0 or 1): "))
    target_output = int(input("Enter the target output (0 or 1): "))

    print("\nNow, choose a logic gate to apply to the inputs:")
    print("1. AND\n2. OR\n3. NOT (apply to one input)\n4. NAND\n5. NOR\n6. XOR")
    gate_choice = int(input("Select a gate (1-6): "))
    
    # Apply the chosen gate to the inputs
    if gate_choice == 1:
        result = AND_gate(input1, input2)
    elif gate_choice == 2:
        result = OR_gate(input1, input2)
    elif gate_choice == 3:
        input_to_not = int(input("Which input to apply NOT to? (1 or 2): "))
        if input_to_not == 1:
            result = NOT_gate(input1)
        else:
            result = NOT_gate(input2)
    elif gate_choice == 4:
        result = NAND_gate(input1, input2)
    elif gate_choice == 5:
        result = NOR_gate(input1, input2)
    elif gate_choice == 6:
        result = XOR_gate(input1, input2)
    else:
        print("Invalid choice! Please choose a number between 1 and 6.")
        return

    print(f"\nResult of applying the selected gate: {result}")

    if result == target_output:
        print("Congratulations! You solved the puzzle! 🎉")
    else:
        print("Oops! Try again and think about the gate logic. 🤔")

# Run the game
if __name__ == "__main__":
    create_circuit()
