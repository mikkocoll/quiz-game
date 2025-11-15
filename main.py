print("How well do you know horses? Let's find out!")

play_game = input("Are you ready to play? ")

if play_game.lower() != "yes":
    print("????")
    quit()

print("HOORAY LET'S GO!!!")
score = 0

# questions
answer = input("What is a baby horse called? ")
if answer.lower()  == ("foal"):
    print("Correct!")
    score += 1
else:
    print("uhhh... no.")

answer = input("What sound does a horse make? ")
if answer.lower()  == ("NEIGH") or ("neigh"):
    print("You betcha!")
    score += 1
else:
    print("Nay way you said that...")

answer = input("How many legs does a horse usually have? ")
if answer == ("4") or ("four"):
    print("Absolutely!")
    score += 1
else:
    print("try again!")

answer = input("What is female adult horse called? ")
if answer == ("mare"):
    print("Correct!")
    score += 1
else:
    print("girl...")

print("You got " + str(score) + " questions correct!")