def add(a, b):
    """Returns the sum of a and b."""
    return a + b

def subtract(a, b):
    """Returns the difference of a and b."""
    return a - b

def multiply(a, b):
    """Returns the product of a and b."""
    return a * b

def divide(a, b):
    """Returns a / b; returns None if b == 0 to prevent crash."""
    if b == 0:
        return None
    return a / b

def mod(a, b):
    """Returns a % b; returns None if b == 0."""
    if b == 0:
        return None
    return a % b

def power(base, exp=2):
    """Computes power using base ** exp with a default argument (exp=2)."""
    return base ** exp

def format_number(n):
    """Helper returning an integer if the value has no decimal part, otherwise float."""
    if isinstance(n, float) and n.is_integer():
        return int(n)
    return n

def main():
    history = []
    
    while True:
        print("\nSelect an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Modulus / Remainder (%)")
        print("6. Power / Exponentiation (Default: Square)")
        print("7. View Calculation History")
        print("8. Exit")
        
        choice = input("\nEnter your choice (1-8): ").strip()
        
        if choice == '8':
            print("Exiting program. Goodbye!")
            break
            
        elif choice == '7':
            if not history:
                print("No calculations performed yet.")
            else:
                print("\n--- Calculation History ---")
                for entry in history:
                    print(entry)
            continue
            
        elif choice in ['1', '2', '3', '4', '5', '6']:
            try:
                if choice == '6':
                    base_input = input("Enter base: ")
                    base = float(base_input) if '.' in base_input else int(base_input)
                    
                    exp_input = input("Enter exponent (press Enter for default 2): ").strip()
                    if exp_input == "":
                        result = power(base)
                        formatted_base = format_number(base)
                        calc_str = f"{formatted_base} ** 2 = {format_number(result)}"
                    else:
                        exp = float(exp_input) if '.' in exp_input else int(exp_input)
                        result = power(base, exp)
                        formatted_base = format_number(base)
                        formatted_exp = format_number(exp)
                        calc_str = f"{formatted_base} ** {formatted_exp} = {format_number(result)}"
                        
                    history.append(calc_str)
                    print(f"[RESULT] {format_number(result)}")
                    
                else:
                    a_input = input("Enter first number: ")
                    b_input = input("Enter second number: ")
                    
                    a = float(a_input) if '.' in a_input else int(a_input)
                    b = float(b_input) if '.' in b_input else int(b_input)
                    
                    formatted_a = format_number(a)
                    formatted_b = format_number(b)
                    
                    if choice == '1':
                        result = add(a, b)
                        op_symbol = "+"
                    elif choice == '2':
                        result = subtract(a, b)
                        op_symbol = "-"
                    elif choice == '3':
                        result = multiply(a, b)
                        op_symbol = "*"
                    elif choice == '4':
                        result = divide(a, b)
                        op_symbol = "/"
                        if result is None:
                            print("[ERROR] Division by zero is not allowed.")
                            continue
                    elif choice == '5':
                        result = mod(a, b)
                        op_symbol = "%"
                        if result is None:
                            print("[ERROR] Modulus by zero is not allowed.")
                            continue
                            
                    formatted_res = format_number(result)
                    calc_str = f"{formatted_a} {op_symbol} {formatted_b} = {formatted_res}"
                    history.append(calc_str)
                    print(f"[RESULT] {formatted_res}")
                    
            except ValueError:
                print("[ERROR] Invalid numeric input. Please enter valid numbers.")
        else:
            print("[ERROR] Invalid choice. Please select a valid option from 1 to 8.")

if __name__ == "__main__":
    main()