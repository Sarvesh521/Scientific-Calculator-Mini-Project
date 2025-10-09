import math
def square_root(x):
    return math.sqrt(x) if x >= 0 else None
def display_menu():
    print("\n--- Scientific Calculator v1.0 ---")
    print("1. Square Root (√x)")
    print("5. Exit")
def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            num = float(input("Enter a number: "))
            print(f"Result: {square_root(num)}")
        elif choice == '5': break
        else: print("Invalid choice.")
if __name__ == "__main__": main()