import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

Words_List = ["Apple","Banana","orange"]
dispaly=[]
#Random word from the list
chosen_word = random.choice(Words_List)
print(chosen_word)
word_length= len(chosen_word)
lives=6
for letter in range(word_length):
    dispaly+="_"
print(dispaly)
# Guess the word
end_0f_game=False

while not end_0f_game:
    guess = input("Enter word to match: ").lower()
    # match guess word to word list
    for position in range(word_length):
        letter=chosen_word[position]
        if letter == guess:
            dispaly[position]=letter
    print(dispaly)

    if guess not in chosen_word:
        lives-=1
        if lives==0:
            end_0f_game=True
            print("You Lose")

    if "_" not in dispaly:
        end_0f_game=True
        print("You Win")

    print(stages[lives])


