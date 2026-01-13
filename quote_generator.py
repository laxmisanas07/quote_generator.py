import random

quotes = [
    "Believe you can and you're halfway there.",
    "Do what you can with what you have, wherever you are.",
    "Success is not final, failure is not fatal: It is the courage to continue that counts.",
    "Dream big and dare to fail.",
    "The only way to do great work is to love what you do."
]

def get_random_quote():
    return random.choice(quotes)

if __name__ == "__main__":
    print("\n✨ Here's your quote for today:\n")
    print(f"\"{get_random_quote()}\"")



