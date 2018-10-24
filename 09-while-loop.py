counter = 1
limit = 10
while counter <= limit:
    print(counter)
    counter += 1

print("done with loop")

#--------------------------------------------------
#### guessing game
secret_word = "toronto"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Guess a city: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("You're out of guesses, YOU LOSE!")
else:
    print("You Win!")