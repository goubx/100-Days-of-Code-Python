import random
import hangman_art
import hangman_words

word_list = hangman_words.word_list

chosen_word = random.choice(word_list)

print(hangman_art.logo)
print(chosen_word)

placeholder = ""
for letter in chosen_word:
    placeholder += "_"
print(placeholder)

display = ""
previous = ""
lives = 6

while display != chosen_word:
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    display = ""
    guess = input("Guess a letter: ").lower()

    if guess in previous:
        print("You've already guessed that. Try again!")
        continue

    for letter in chosen_word:
        if letter == guess:
            previous += guess
            display += guess
        elif letter in previous:
            display += letter
        else:
            display += "_"
    print(display)

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        print(hangman_art.stages[lives])
        if lives == 0:
            print(f"***********************YOU LOSE. The word was {chosen_word}**********************")
            break

else:
    print("****************************YOU WIN****************************")
