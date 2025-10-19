dictionary = {
    "python": "A high-level programming language.",
    "algorithm": "A step-by-step procedure for solving a problem.",
    "variable": "A name used to store data value.",
    "function": "A block of code that performs a specific task."
}

while True:
    word = input("\nEnter a word (or 'exit' to quit): ").lower()
    if word == "exit":
        print("Goodbye!")
        break
    print("Meaning:", dictionary.get(word, "Word not found!"))
