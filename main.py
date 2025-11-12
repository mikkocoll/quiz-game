print("How well do you know horses? Let's find out!")

play_game = input("Are you ready to play? ")

print(play_game)

if play_game != "yes":
    print("????")
    quit()

print("HOORAY LET'S GO!!!")

# questions
answer = input("What is a baby horse called? ")
if answer == ("foal"):
    print("Correct!")

else:
    print("uhhh... no.")