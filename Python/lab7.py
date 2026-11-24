# Lab 07 - Calendar Verification System

print("========================================")
print("     CALENDAR VERIFICATION SYSTEM")
print("========================================")

# 1. Take input from the user
year = int(input("Enter year: "))

# 2. Validate the input
if year <= 0:
    print("Error: Please enter a positive integer greater than 0.")
else:
    print("----------------------------------------")
    print(f"Year: {year}")
    
    # 3. Check leap year rules using if-else
    if year % 400 == 0:
        status = "LEAP YEAR"
        reason = "Century year divisible by 400"
        days_in_year = "366 days"
        days_in_feb = "29 days"
    elif year % 100 == 0:
        status = "COMMON YEAR"
        reason = "Century year not divisible by 400"
        days_in_year = "365 days"
        days_in_feb = "28 days"
    elif year % 4 == 0:
        status = "LEAP YEAR"
        reason = "Divisible by 4 and not a century year"
        days_in_year = "366 days"
        days_in_feb = "29 days"
    else:
        status = "COMMON YEAR"
        reason = "Not divisible by 4"
        days_in_year = "365 days"
        days_in_feb = "28 days"

    # 5. Display the results clearly
    print(f"Status: {status}")
    print(f"Days in Year: {days_in_year}")
    print(f"Days in February: {days_in_feb}")
    print(f"Reason: {reason}")
    print("----------------------------------------")