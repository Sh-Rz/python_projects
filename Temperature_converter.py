print("Hello! I am the temperature converter I can convert celsius to fahrenheit!")
import time
time.sleep(2)
celsius= float(input("So.. What is the temperature  outside of where you live ?"))
fahrenheit= (celsius*1.8)+32
print(fahrenheit,"°F")
if (celsius>30):
    print("Woah It's hot there, keep drinking water or you might get dehydrated!🥤")

elif (18<celsius<25):
    print("Wow!!! Perfect weather not too hot or not too cold!")

else:
    print("Wow it's cold there isn't it")
