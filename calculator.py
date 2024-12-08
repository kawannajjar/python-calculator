"""
Calculator CLI Project

A simple command-line calculator to perform basic mathematical operations.
Features:
- Addition
- Subtraction
- Multiplication
- Division

Author: Kawan Najjar
Email: kawannajjar@gmail.com
GitHub: https://github.com/kawannajjar
Instagram: https://www.instagram.com/kavannajjar/
Date: 2024-12-08
"""


def add(a: float, b: float) -> float:
    """Adds tow numbers."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Subtracts the second number from the first."""
    return a - b 


def multiply(a: float, b: float) -> float:
    """Multiplies two numbers."""
    return a * b


def divide(a: float, b: float) -> float:
    """Divides the firs number by the second.Raises eroor if b is zero."""
    if b == 0:
        raise ValueError("Cannt divide by zero")
    return a / b


def display_menu():
    """Displays the Calculator menu."""
    print("\n--- Calculator Menu ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    print("-----------------------")


def main():
    """Main function to run the calculator."""
    while True:
        display_menu()
        choice = input("Select an operation (1-5): ")
        
        if choice == "5":
            print("Goodbye! Thank you for using the calculator.")
            break
        
        if choice in ["1", "2", "3", "4"]:
            try:
                num1 = float(input("Enter the first number: "))        
                num2 = float(input("Enter the second number: "))
                
                if choice == "1":
                    result = add(num1, num2)
                    print(f"The result is: {result}")
                elif choice == "2":
                    result = subtract(num1, num2)
                    print(f"The result is: {result}")
                elif choice == "3":
                    result = multiply(num1, num2)
                    print(f"The result is: {result}")
                elif choice == "4":
                    result = divide(num1, num2)
                    print(f"The result is: {result}")
            except ValueError as e:
                print(f"Erorr: {e}")
        else:
            print("Invalid choice.Please try again")
            
            
if __name__ == "__main__":
    main()            