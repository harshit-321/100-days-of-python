# Palindrome Checker Game
# ------------------------
# A fun interactive game that checks if a word or phrase is a palindrome.
# Written to be human-readable, beginner-friendly, and professional.

def is_palindrome(text: str) -> bool:
    """
    Check if the given text is a palindrome.
    Ignores spaces, punctuation, and capitalization.
    """
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]


def play_game():
    """
    Run the interactive palindrome game.
    The player enters words or phrases until they choose to quit.
    """
    print("=" * 50)
    print(" 🎮 Welcome to the Palindrome Checker Game! 🎮 ")
    print("=" * 50)
    print("Rules:")
    print("1. Enter any word or phrase.")
    print("2. The program will tell you if it's a palindrome.")
    print("3. Type 'quit' to exit.\n")

    while True:
        user_input = input("👉 Enter a word or phrase: ")

        if user_input.lower() == "quit":
            print("\nThanks for playing! 👋 Goodbye.")
            break

        if is_palindrome(user_input):
            print("✅ That's a palindrome!\n")
        else:
            print("❌ Not a palindrome.\n")


if __name__ == "__main__":
    play_game()