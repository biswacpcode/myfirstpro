import random
print("Hey I am python!! Lets play a game\nIt is called HANDCRICKET\nThe rules are you choose a number and I choose a number\nEnter you number (1-6) : ")
y=int(input())
c=random.randint(1,6)
score = 0
print(f"I chose {c}")
while y!=c:
    print("HAhhhh.. I couldnt guess it")
    score+=y
    print("Enter again: ")
    y=int(input())
    c= random.randint(1,6)
    print(f"I chose {c}")
print(f"YESSSSSSS I win.... I rule Humans.\nBut Still your score is not bad.\nYour Run is {score}")

