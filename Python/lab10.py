# Lab 10 - Text Processing Tool

print("========================================")
print("         TEXT PROCESSING TOOL")
print("========================================")

# 1. Accept a sentence from the user
sentence = input("Enter a sentence: ")

print()
print("--- Processing Results ---")

# 2. Display a character at a specific position using string indexing
index_pos = int(input("Enter position for indexing: "))
char_at_pos = sentence[index_pos]
print(f"Character at position {index_pos} : '{char_at_pos}'")

# 3. Extract a portion of the sentence using string slicing
start_idx = int(input("Enter start index for slicing: "))
end_idx = int(input("Enter end index for slicing: "))
sliced_string = sentence[start_idx:end_idx]
print(f"Sliced string [{start_idx}:{end_idx}]     : '{sliced_string}'")

# 4. Convert the sentence into uppercase
upper_sentence = sentence.upper()
print(f"Uppercase                  : {upper_sentence}")

# 5. Convert the sentence into lowercase
lower_sentence = sentence.lower()
print(f"Lowercase                  : {lower_sentence}")

# 6. Replace a specified word with another word
old_word = input("Enter word to replace: ")
new_word = input("Enter replacement word: ")
replaced_sentence = sentence.replace(old_word, new_word)
print(f"After replace              : {replaced_sentence}")

# 7. Find and display the length of the sentence
length_sentence = len(sentence)
print(f"Length of sentence         : {length_sentence}")

print()
print("========================================")
print("Analysis Complete!")
print("========================================")