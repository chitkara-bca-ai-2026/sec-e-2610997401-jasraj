# Lab 13 - Inventory Control System

# Initialize inventory list with at least 4 products
inventory = ["Notebook", "Pen", "Eraser", "Ruler"]

while True:
    print("\n========================================")
    print("      INVENTORY CONTROL SYSTEM")
    print("========================================")
    print("Select an operation:")
    print("1. View Inventory")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Sort Inventory")
    print("5. Exit")
    
    # Prompt the user to choose an operation
    choice = input("\nEnter your choice (1-5): ")
    
    if choice == '1':
        # View Inventory: Loop through the list and display items with numbers
        print("\n--- Current Inventory ---")
        if len(inventory) == 0:
            print("Inventory is empty.")
        else:
            for idx, item in enumerate(inventory, start=1):
                print(f"{idx}. {item}")
                
    elif choice == '2':
        # Add Item: Accept item name and add using .append()
        new_item = input("Enter item name to add: ")
        inventory.append(new_item)
        print(f"[SUCCESS] \"{new_item}\" added to inventory.")
        
    elif choice == '3':
        # Remove Item: Check existence using 'in' and remove using .remove()
        item_to_remove = input("Enter item name to remove: ")
        if item_to_remove in inventory:
            inventory.remove(item_to_remove)
            print(f"[SUCCESS] \"{item_to_remove}\" removed from inventory.")
        else:
            print(f"[ERROR] \"{item_to_remove}\" not found in inventory.")
            
    elif choice == '4':
        # Sort Inventory: Sort alphabetically using .sort() and display
        inventory.sort()
        print("\n[SUCCESS] Inventory sorted alphabetically.")
        print("Updated Inventory:")
        for idx, item in enumerate(inventory, start=1):
            print(f"{idx}. {item}")
            
    elif choice == '5':
        # Exit: Print goodbye message and break loop
        print("Exiting Inventory System. Goodbye!")
        break
        
    else:
        # Invalid input error message
        print("[ERROR] Invalid choice. Please enter a number between 1 and 5.")