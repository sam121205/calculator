def calculator():
    print("🧮 Simple Calculator")
    print("Choose operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    try:
        choice = int(input("Enter choice (1/2/3/4): "))
        if choice not in [1, 2, 3, 4]:
            print("❌ Invalid choice")
            return

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 1:
            print(f"Result: {num1} + {num2} = {num1 + num2}")
        elif choice == 2:
            print(f"Result: {num1} - {num2} = {num1 - num2}")
        elif choice == 3:
            print(f"Result: {num1} * {num2} = {num1 * num2}")
        elif choice == 4:
            if num2 != 0:
                print(f"Result: {num1} / {num2} = {num1 / num2}")
            else:
                print("❌ Error: Division by zero is not allowed.")

    except ValueError:
        print("❌ Please enter valid numbers.")

# Run the calculator
if __name__ == "__main__":
    calculator()