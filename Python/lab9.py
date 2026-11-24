# Lab 09 - Festival Decoration Designer

print("========================================")
print("      FESTIVAL DECORATION DESIGNER")
print("========================================")

# 1. Take input from the user
n = int(input("Enter the number of rows: "))
print()

# Pattern 1: Star Triangle (Right-Angled)
print("Pattern 1: Star Triangle")
print("-" * 40)
for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()
print()

# Pattern 2: Number Triangle
print("Pattern 2: Number Triangle")
print("-" * 40)
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
print()

# Pattern 3: Inverted Star Triangle
print("Pattern 3: Inverted Star Triangle")
print("-" * 40)
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
print()

# Pattern 4: Pyramid (Centered Triangle)
print("Pattern 4: Pyramid")
print("-" * 40)
for i in range(1, n + 1):
    # Print leading spaces for centering
    print(" " * (n - i), end="")
    # Print stars with spaces
    for j in range(i):
        print("*", end=" ")
    print()
print("========================================")