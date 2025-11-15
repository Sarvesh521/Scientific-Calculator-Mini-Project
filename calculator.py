import math
import time

def square_root(x):
    return math.sqrt(x) if x >= 0 else None

def factorial(x):
    if not isinstance(x, int) or x < 0:
        return None
    return math.factorial(x)

def natural_log(x):
    if x <= 0:
        return None
    return math.log(x)

def power(x, b):
    return math.pow(x, b)

def display_menu():
    print("\n--- Scientific Calculator ---", flush=True)
    print("1. Square Root (√x)", flush=True)
    print("2. Factorial (!x)", flush=True)
    print("3. Natural Logarithm (ln(x))", flush=True)
    print("4. Power (x^b)", flush=True)
    print("5. Exit", flush=True)
    print("---------------------------------", flush=True)

def main():
    # print("Calculator application started. Waiting for connection...", flush=True)
    # time.sleep(60)
    while True:
        display_menu()
        choice = input("Enter your function choice: ")
        if choice == '1':
            try:
                num = float(input("Enter a number: "))
                print(f"Result: {square_root(num)}", flush=True)
            except ValueError:
                print("Invalid input. Please enter a number.", flush=True)

        elif choice == '2':
            try:
                num = int(input("Enter a non-negative integer: "))
                result = factorial(num)
                if result is not None:
                    print(f"Result: {result}", flush=True)
                else:
                    print("Invalid input. Factorial is not defined for negative numbers or non-integers.", flush=True)
            except ValueError:
                print("Invalid input. Please enter an integer.", flush=True)

        elif choice == '3':
            try:
                num = float(input("Enter a positive number: "))
                result = natural_log(num)
                if result is not None:
                    print(f"Result: {result}", flush=True)
                else:
                    print("Invalid input. Natural logarithm is not defined for zero or negative numbers.", flush=True)
            except ValueError:
                print("Invalid input. Please enter a number.", flush=True)
        
        elif choice == '4':
            try:
                base = float(input("Enter the base (x): "))
                exponent = float(input("Enter the exponent (b): "))
                print(f"Result: {power(base, exponent)}", flush=True)
            except ValueError:
                print("Invalid input. Please enter numbers.", flush=True)

        elif choice == '5':
            print("Exiting calculator...", flush=True)
            break
        else:
            print("Invalid choice.", flush=True)

if __name__ == "__main__":
    main()