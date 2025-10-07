# Random Joke Generator
# ---------------------

import random

print("😂 Welcome to the Random Joke Generator! 😂")
print("------------------------------------------\n")

# Step 1: Create a list of jokes
jokes = [
    "Why did the computer show up at work late? It had a hard drive!",
    "Why do Java developers wear glasses? Because they don’t see sharp!",
    "Why was the math book sad? Because it had too many problems.",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "What did one ocean say to the other ocean? Nothing, they just waved!",
    "Why did the bicycle fall over? It was two-tired!",
    "What do you call a fake noodle? An Impasta!",
    "Why did the student eat his homework? Because the teacher said it was a piece of cake!"
]

# Step 2: Randomly select one joke from the list
selected_joke = random.choice(jokes)

# Step 3: Display the joke
print(selected_joke)

print("\n🤣 Hope that made you smile!")
