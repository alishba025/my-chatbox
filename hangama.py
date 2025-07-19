import random

# Step 1: Define a list of words
words = ["apple", "house", "water", "chair", "plant"]

# Step 2: Randomly choose one word
secret_word = random.choice(words)

# Step 3: Create variables to store game data
guessed_letters = []
wrong_guesses = 0
max_wrong = 6

# Step 4: Game loop
while wrong_guesses < max_wrong:
    # Show word with guessed letters
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"
    
    print("Word: ", display_word)
    
    # Check if player has guessed all letters
    if "_" not in display_word:
        print("🎉 You won! The word was:", secret_word)
        break
    
    # Take input from user
    guess = input("Guess a letter: ").lower()
    
    # Check if letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue
    
    # Add guess to guessed letters
    guessed_letters.append(guess)
    
    # Check if guess is correct
    if guess not in secret_word:
        wrong_guesses += 1
        print("❌ Wrong guess. You have", max_wrong - wrong_guesses, "tries left.")
    else:
        print("✅ Good guess!")

# If loop ends and player didn’t guess the word
