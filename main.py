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

answer = input("What sound does a horse make? ")
if answer == ("NEIGH") or ("neigh"):
    print("You betcha!")

else:
    print("Nay way you said that...")

answer = input("How many legs does a horse usually have? ")
if answer == ("4") or ("four"):
    print("Absolutely!")

else:
    print("uhhh... no.")

answer = input("What is female adult horse called? ")
if answer == ("mare"):
    print("Correct!")

else:
    print("girl...")

