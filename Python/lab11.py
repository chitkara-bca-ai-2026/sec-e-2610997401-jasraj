# Lab 11 - Online Account Registration

print("========================================")
print("      PASSWORD VALIDATION REPORT")
print("========================================")

# 1. Take input from the user
username = input("Enter your username: ")
password = input("Enter your password: ")

# 2. Validate the password against rules
length_pass = len(password) >= 8
length_status = "PASS" if length_pass else "FAIL"

digit_pass = any(char.isdigit() for char in password)
digit_status = "PASS" if digit_pass else "FAIL"

upper_pass = any(char.isupper() for char in password)
upper_status = "PASS" if upper_pass else "FAIL"

# Overall validity
is_valid = length_pass and digit_pass and upper_pass

# Mask password for display
masked_password = "*" * len(password)

# 3. Display the validation results in a clean, formatted manner
print()
print(f"Username: {username}")
print(f"Password: {masked_password}")
print()
print("--- Validation Rules ---")
print(f"[{length_status}] Minimum 8 characters ({len(password)} characters)")
print(f"[{digit_status}] At least one digit")
print(f"[{upper_status}] At least one uppercase letter")
print()
print("--- Result ---")
if is_valid:
    print("Password is VALID!")
    print(f"Account created successfully for {username}!")
else:
    print("Password is INVALID!")
print("========================================")