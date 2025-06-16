import requests
import time

WORD_API_URL = "https://random-words-api.kushcreates.com/api"
DICT_API_URL = "https://api.dictionaryapi.dev/api/v2/entries/en"

def get_word_with_hint():
    """Fetch one word with a valid hint (definition)."""
    while True:
        try:
            # Fetch one random word
            resp = requests.get(WORD_API_URL, params={"language": "en", "words": 1})
            resp.raise_for_status()
            word = resp.json()[0]["word"]
        except Exception as e:
            print(f" Failed to fetch word: {e}")
            return None, None

        try:
            # Get definition as hint
            dict_resp = requests.get(f"{DICT_API_URL}/{word}")
            dict_resp.raise_for_status()
            hint = dict_resp.json()[0]["meanings"][0]["definitions"][0]["definition"]
            if hint and isinstance(hint, str) and word.isalpha():
                return word.lower(), hint
        except Exception:
            continue  # Skip if no valid hint

def play_guessing_game():
    word, hint = get_word_with_hint()
    if not word:
        print(" Could not get a valid word and hint.")
        return

    guessed_letters = set()
    attempts = 6

    print("\n Guess the word letter by letter!")
    print(f" Hint: {hint}")
    print(f" The word has {len(word)} letters.\n")

    while attempts > 0:
        display = " ".join(letter if letter in guessed_letters else "_" for letter in word)
        print(f"Word: {display}")
        guess = input("Enter a letter (or 'exit' to quit): ").lower()

        if guess == "exit":
            print("Exiting game. Goodbye!")
            return

        if len(guess) != 1 or not guess.isalpha():
            print(" Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print(" You've already guessed that letter.")
            continue

        if guess in word:
            guessed_letters.add(guess)
            print(" Correct!")
        else:
            attempts -= 1
            print(f" Wrong! Attempts left: {attempts}")

        # Check if all letters are guessed
        if all(letter in guessed_letters for letter in word):
            print(f"\nYou guessed it! The word was '{word}'.")
            return

    print(f"\n Game over! The word was '{word}'.")

# Run the game
if __name__ == "__main__":
    play_guessing_game()
