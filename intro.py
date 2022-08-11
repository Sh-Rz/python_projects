from tkinter import N


print("Welcome please answer a few question to continue")
print("What's your first name?")
fName= input()
print("..and last name please")
lName =input()
print("That's a lovely name!")
import time
time.sleep(2.5)
print("Which country do you live in", fName, lName,"?")
country=input()
print("Woooow!!! I've always wanted to visit", country,"!")
time.sleep(2.5)
print("Which city in",country,"do you live in?")
city=input()
print("ooooo I have heard of",city,"being one of the must go places in", country)
time.sleep(2.5)
print("Are you from", country, "?   *answer with n/y in lower case")
ny=input()
if ny=="n":
        print("Then Where are you from?")
        birthPlace=input()
        print("wooooah ", birthPlace, "is sooo beautiful from what I have heard")
        

time.sleep(2.5)
print(" I will call you",fName,"from now on beacuse I think we're frinds so no formalities right? thank you😊😁!")
print("how old are you",fName,"?")
age= float(input())
if age<18:
    print("Oh so you are still in school. Study hard then!💪")
    time.sleep(2)
    print("So... Which school do you study in?")
    school=input()
    print('which year do you study in at',school)
    year= int(input())
    print("you are in year",year,"Weeeelll I hope you are ready for year",year+1,"😅")
    time.sleep(2)
    print("...Beeeecause it's soo fun🎉!")
    print("Well now I have ran out of charge so I must say good bye now",fName,"I'll see you soon my first ever friend!😁😄😊😊!!!")
    time.sleep(2)
    print(" Oh and don't worry about your exams they're going to be easy if you study hard and if you don't get distracted😉!")

else:
    print("So you're now out of school. Do you miss it? ")
    notInschool= input()

if notInschool== "yes":
    print('Awwww its ok you can visit it anytime 😉:)')
    print("Well now I have ran out of charge so I must say good bye now",fName,"I'll see you soon my first ever friend!😁😄😊😊!! ")
    time.sleep(2)
    print("Oh and also go and visit you're school on sept it's the best time trust me!😉")

else:
    print("So you don't miss your friends, fav teachers,lockers or your usual hangout place during lunch?😢😔😒 TT_TT")
    print("Anyways I have ran out of charge so I must say good bye now",fName,"I'll see you soon my first ever friend!😁😄😊😊!! ")
    time.sleep(2)    
    print("Oh and this is a reminder to call or message you school friends it gonna make them and you happy😉")


