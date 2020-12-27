print("Welcome to ") 
print("CAN YOU GUESS MY NUMBER!")

player1_name = input("Player 1 Name: ")
print("Welcome " + player1_name)

player2_name = input("Player 2 Name: ")
print("Welcome " + player2_name)

print("Ok, time for " + player1_name + " to enter a number" '\n' + player2_name + ", Please don't look at the screen when " + player1_name + " is typing in their number 😠!")
number_1 = input("Please choose a number between 1 to 100: ")
print(number_1)

print("Now, it is time for " + player2_name + " to GUESS YOUR NUMBER!")

number_of_guesses = 0

while number_of_guesses < 3:
    print(player2_name + ", please enter your guess below ")
    guess = input("Guess the Number: ")
    number_of_guesses += 1
    if guess < number_1:
        print("Your Guess is too Low, guess higher")
    if guess > number_1:
        print("Your Guess is too high, guess lower")
    if guess == number_1:
        break
    
    
if guess == number_1:
    print(player2_name + " guessed your number in " + str(number_of_guesses) + " tries!")
else:
    print(player1_name + ", You WON!")
