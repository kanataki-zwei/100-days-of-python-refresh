import random 
hangman_stages = [
    """
     ------
     |    |
     |    O
     |   /|\\
     |   / \\
     |   
    _|_
    """,

    """
     ------
     |    |
     |    O
     |   /|\\
     |   / 
     |   
    _|_
    """,

    """
     ------
     |    |
     |    O
     |   /|\\
     |    
     |   
    _|_
    """,

    """
     ------
     |    |
     |    O
     |   /|
     |    
     |   
    _|_
    """,

    """
     ------
     |    |
     |    O
     |    |
     |    
     |   
    _|_
    """,

    """
     ------
     |    |
     |    O
     |   
     |    
     |   
    _|_
    """,

    """
     ------
     |    |
     |    
     |   
     |    
     |   
    _|_
    """
]


wordlist = ['science', 'nature', 'jurassic', 'alien', 'angry', 'mastermind']

chosen_word = random.choice(wordlist)
print(chosen_word)
display = ['_' for char in chosen_word]
print(' '.join(display))

game_over = False
lives = 6
guessed_letters = set()
while game_over == False:
    guess = input("Guess a letter in the word: ").lower()
    if guess in guessed_letters:
        print(f"You have already guessed letter {guess}")
        continue
    guessed_letters.add(guess)
    if guess in chosen_word:
        print(f"You have correctly guessed {guess}")
        for index, letter in enumerate(chosen_word):
            if guess == letter:
                
                display[index] = guess
        if '_' in display:
            print(' '.join(display))
        else:
            print("Game Over! You win!")
            print(' '.join(display))
            game_over = True
    else:
        lives-=1
        if lives==0:
            print(hangman_stages[lives])
            print("Game Over! You Lose!")
            print(f"The word was: {chosen_word}")
            game_over = True
        else:
            print(hangman_stages[lives])
            print(f"Incorrect guess, you have {lives} trials remaining!")

    