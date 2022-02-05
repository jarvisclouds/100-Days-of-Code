# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name1low = name1.lower()
name2low = name2.lower()

truecount = name1low.count("t") + name1low.count("r") + name1low.count("u") + name1low.count("e") + name2low.count("t") + name2low.count("r") + name2low.count("u") + name2low.count("e")

lovecount = name1low.count("l") + name1low.count("o") + name1low.count("v") + name1low.count("e") + name2low.count("l") + name2low.count("o") + name2low.count("v") + name2low.count("e")

score = int(str(truecount) + str(lovecount))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
