import random #to import the function for the computer system to generate a random number
name = input("Please enter your name..") #getting the users nume to make the message more personalised to the user
print("Hello", name, "welcome to the number guessing game") #greeting the user 
print("The computer will generate a random number between 1 and 100 and you will have to try guess the number. If you get it wrong, I'll give you some advice to say if you should guess higher or lower. Good Luck") #explaining the game to the user

numgen = random.randint(1,100) #outputting a random integer in the range 1 and 100 inclusive
numguess = int(input("Guess a number between 1 and 100")) #making the user guess an integer between 1 and 100
guesses = 1 #creating a variable to keep track on how many guesses the user has used

while numgen != numguess: #creating a while loop to allow the user to keep on guessing while their guess is not equal to the generated number
    if numgen < numguess: #giving relevant advice if the user guesses too high
        numguess = int(input("Your guess was too high, try guessing a lower number")) #updating the variable numguess for the next round of checking
        guesses = guesses + 1 #updating the number of guesses
    
    elif numgen > numguess: #giving relevant avice if the user guesses too low
        numguess = int(input("Your guess was too low, try guessing a higher number")) #updating the variable numguess for the next round of checking
        guesses = guesses + 1 #updating the number of guesses

print("You got the number right!! Congratulations!!") #since the user is outside the while loop, their guess muct be right because they cal only leave the while loop if the variables numgen and numguess are equal
print("You did it in", guesses, "guesses" ) #telling the user how many guesses it took them to guess the correct number