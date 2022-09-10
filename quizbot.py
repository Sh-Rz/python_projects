from textblob import TextBlob
import random
import time
import pyqrcode
import png
from pyqrcode import QRCode
score=0
s = ''

url = pyqrcode.create(s)

url.png('QR.png', scale = 10)

url.svg('QR.svg', scale= 10)

print(input('Hii there! My name is quiz bot, Nice to meet you! Wha your name?'))
country= print(input('oooooo Thats a nice name! So where do you live '))
celsius= float(input("So.. What is the temperature  there"))
fahrenheit= (celsius*1.8)+32
print(fahrenheit,"°F")
if (celsius>30):
    print("Woah It's hot there, keep drinking water or you might get dehydrated!🥤")

elif (18<celsius<25):
    print("Wow!!! Perfect weather not too hot or not too cold!")

else:
    print("Wow it's cold there isn't it")

print('So now I know more about you shall we continue with the quiz?')
def countdown(n):
  if(n==0):
    print("lets start")
  else:
    print(n)
    print("*"*n)
    time.sleep(n*1)
    countdown(n-1)
n=5  
answer1=('egg')
answer2=('all of the months')
answer3=('are you asleep')
answer4=('bank')
answer5=('darkness')
answer6=('blackboard')
answer7=('breath')
answer8=('dictionary')
answer9=('they both way the same')
answers=[answer1,answer2,answer3,answer4,answer5,answer6,answer7,answer8,answer9]
countdown(n)
question1= TextBlob(input('What has to be broken before you can use it?'))
if question1==answer1:
  print('...')
  time.sleep(1)
  print("Thaaaats Correct🎉🎉✨🎊")
  score+1
question2= TextBlob(input('What month of the year has 28 days?'))
question3= TextBlob(input('What question can you never answer yes to correctly?'))
question4= TextBlob(input(' I have branches, but no fruit, trunk or leaves. What am I?'))
question5= TextBlob(input('The more of this there is, the less you see. What is it?'))
question6= TextBlob(input('What is black when it’s clean and white when it’s dirty?'))
question7= TextBlob(input(' I’m lighter than a feather, yet the strongest person can’t hold me for five minutes. What am I?'))
question8= TextBlob(input('Where does today come before yesterday?'))
question9= TextBlob(input('Which is heavier: a ton of bricks or a ton of feathers?'))
questions= [question1,question2,question3,question4,question5,question6,question8,question7,question9]

if question1==answer1:
  print('...')
  time.sleep(1)
  print("Thaaaats Correct🎉🎉✨🎊")
  score+1
else:
  print('...')
  time.sleep(1)
  print("Sorry thats wrong. try again. I belive in you!😊😄💪")

if question2==answer2:
  print('...')
  time.sleep(1)
  print("Thaaaats Correct🎉🎉✨🎊")
  score+1
else:
  print('...')
  time.sleep(1)
  print("Sorry thats wrong. try again. I belive in you!😊😄💪")

if question3==answer3:
  print('...')
  time.sleep(1)
  print("Thaaaats Correct🎉🎉✨🎊")
  score+1
else:
  print('...')
  time.sleep(1)
  print("Sorry thats wrong. try again. I belive in you!😊😄💪")

if question4==answer4:
  print('...')
  time.sleep(1)
  print("Thaaaats Correct🎉🎉✨🎊")
  score+1
else:
  print('...')
  time.sleep(1)
  print("Sorry thats wrong. try again. I belive in you!😊😄💪")

if question5==answer5:
  print('...')
  time.sleep(1)
  print("Thaaaats Correct🎉🎉✨🎊")
  score+1
else:
  print('...')
  time.sleep(1)
  print("Sorry thats wrong. try again. I belive in you!😊😄💪")

if question6==answer6:
  print('...')
  time.sleep(1)
  print("Thaaaats Correct🎉🎉✨🎊")
  score+1
else:
  print('...')
  time.sleep(1)
  print("Sorry thats wrong. try again. I belive in you!😊😄💪")


