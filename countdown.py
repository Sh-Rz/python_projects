
import time

print('Hello! This is the countdown machine')

def countdown(n):
  if(n==0):
    print("Blast off")
  else:
    print(n)
    print("*"*n)
    time.sleep(n*1)
    countdown(n-1)

n=int(input("Where do you want the countdown to start "))
countdown(n)