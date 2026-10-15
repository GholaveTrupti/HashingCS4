
# Dictionary Application using Hash Table

size = 10
hash_table = [None] * size

def hash_function(word):
    return sum(ord(ch) for ch in word) % size

def insert(word, meaning):
    index = hash_function(word)

    for i in range(size):
        pos = (index + i) % size

        if hash_table[pos] is None:
            hash_table[pos] = (word, meaning)
            print("Word added successfully!")
            return

        if hash_table[pos][0] == word:
            hash_table[pos] = (word, meaning)
            print("Meaning updated successfully!")
            return

    print("Dictionary is full!")

def search(word):
    index = hash_function(word)

    for i in range(size):
        pos = (index + i) % size

        if hash_table[pos] is None:
            break

        if hash_table[pos][0] == word:
            print("Meaning:", hash_table[pos][1])
            return

    print("Word not found!")

def display():
    print("\nDictionary Contents:")
    for item in hash_table:
        if item is not None:
            print(item[0], ":", item[1])

while True:
    print("\n--- Dictionary Menu ---")
    print("1. Add Word")
    print("2. Search Word")
    print("3. Display Dictionary")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        word = input("Enter word: ").strip().lower()
        meaning = input("Enter meaning: ").strip()

        if word and meaning:
            insert(word, meaning)
        else:
            print("Word and meaning cannot be empty!")

    elif choice == "2":
        word = input("Enter word to search: ").strip().lower()
        search(word)

    elif choice == "3":
        display()

    elif choice == "4":
        print("Thank you for using the Dictionary!")
        break

    else:
        print("Invalid choice! Try again.")
