import random
def CompChoice():
    n=random.randint(0,2)
    c=["snake", "water", "gun"]
    return c[n]

p1=0
p2=0
win={"snake":"water", "water":"gun", "gun":"snake"}
while(p1<3 and p2<3):
    choice = input("Enter ur choice")
    Cchoice=CompChoice()
    print(f"{choice} Vs {Cchoice}")
    if choice.lower()==Cchoice:
        print("Tie")
    elif win.get(choice)==Cchoice:
        print("u win")
        p1+=1
    else:
        print("Computer wins")
        p2+=1

if p1>p2:
    print("U win the whole Match")
else:
    print("Computer wins the whole match")
