# Lab 14 - Library Book Collection

# 1. Initial Data Setup
# Store at least 4 default books as tuples in a list 'books'
books = [
    ("Python Crash Course", "Eric Matthes", "2019", "Programming"),
    ("Automate the Boring Stuff", "Al Sweigart", "2020", "Programming"),
    ("Artificial Intelligence: A Modern Approach", "Stuart Russell", "2021", "AI"),
    ("Clean Code", "Robert C. Martin", "2008", "Software Engineering")
]

# Extract the initial unique categories into a set named 'library_categories'
library_categories = {book[3] for book in books}

# Initialize a second set named 'student_wishlist' with at least 4 requested genres
student_wishlist = {"AI", "Cloud Computing", "Robotics", "Cybersecurity"}

while True:
    print("\n========================================================")
    print("          LIBRARY BOOK & CATEGORY MANAGER")
    print("========================================================")
    print("Select an operation:")
    print("1. View Cataloged Books")
    print("2. Add New Book Record")
    print("3. View Unique Library Categories")
    print("4. Add Category to Student Wishlist")
    print("5. Run Category Gap Analysis")
    print("6. Exit")
    
    # Prompt user to choose an operation using numeric choices (1 to 6)
    choice = input("\nEnter your choice (1-6): ")
    
    if choice == '1':
        # 1. View Cataloged Books — Display all fixed book records using tuple unpacking
        print("\n--- Current Library Catalog (Fixed Records) ---")
        for idx, (title, author, year, category) in enumerate(books, start=1):
            print(f"{idx}. \"{title}\" by {author} ({year}) | Genre: {category}")
        print(f"Total Books: {len(books)}")
        
    elif choice == '2':
        # 2. Add New Book Record — Register a new book as an immutable tuple and update category set[cite: 14]
        print("\n--- Add New Book Record ---")
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        year = input("Enter publication year: ")
        category = input("Enter category/genre: ")
        
        new_book = (title, author, year, category)
        books.append(new_book)
        library_categories.add(category)
        
        print(f"\n[SUCCESS] \"{title}\" added as an immutable catalog record.")
        print(f"[INFO] Category set updated with: \"{category}\"")
        
    elif choice == '3':
        # 3. View Unique Library Categories — Display all unique genres currently held in the library[cite: 14]
        print("\n--- Unique Categories Available in Library (Set) ---")
        for cat in sorted(library_categories):
            print(f" - {cat}")
        print(f"Total Unique Genres: {len(library_categories)}")
        
    elif choice == '4':
        # 4. Add Category to Student Wishlist — Add a newly requested genre to the student demand set[cite: 14]
        print("\n--- Add Category to Student Wishlist ---")
        new_wish = input("Enter requested genre/category: ")
        student_wishlist.add(new_wish)
        print(f"[SUCCESS] \"{new_wish}\" added to student wishlist.")
        
    elif choice == '5':
        # 5. Run Category Gap Analysis — Perform set operations (Intersection, Difference, Union)[cite: 14]
        print("\n--- Category Gap Analysis ---")
        matching_genres = library_categories.intersection(student_wishlist)
        missing_genres = student_wishlist.difference(library_categories)
        combined_genres = library_categories.union(student_wishlist)
        
        print(f"Library Categories Held : {library_categories}")
        print(f"Student Wishlist Demands: {student_wishlist}")
        print("-" * 55)
        print(f"Available Wishlist Items (Intersection): {matching_genres}")
        print(f"Missing Wishlist Items (Difference)   : {missing_genres}")
        print(f"Total Combined Universe (Union)       : {combined_genres}")
        
    elif choice == '6':
        # 6. Exit — Terminate the program[cite: 14]
        print("Exiting Library Book Collection Manager. Goodbye!")
        break
        
    else:
        print("[ERROR] Invalid choice. Please enter a number between 1 and 6.")