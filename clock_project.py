from datetime import datetime
now = datetime.now()

value =input("What is your name? ") #name input
print("Well...Hello there!")

str1=("""The date today is %02d/%02d/%04d""" % (now.day, now.month, now.year))
str2=(""" and the exact time is %02d:%02d:%02d.""" % (now.hour, now.minute, now.second))
print(str1 + str2)

if now.hour < 12: #define time of day
    print("I hope you are having a nice morning",value,".")
elif now.hour < 17:
    print("Have a great afternoon",value,".")
elif now.hour < 21:
    print("Have a lovely evening", value,".")
elif now.hour <23:
    print("Good night", value)

if now.weekday() in (5, 6): #define greeting of progress through week to weekend
    print("It is here, have a nice weekend")
if now.weekday() in (3, 4):
    print("Don't worry, it is nearly the weekend!")
if now.weekday() in (0,1,2):
    print('I hope you have a nice week!')