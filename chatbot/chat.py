from chrome import new
import TeachMath
import time
from selenium import webdriver

time = time.ctime()

print("Hello, I am the new chatBot Please ask me a question and i will try my best to answer it.")

while True:
    qs = input('> ') 

    if qs == 'Open browser':
        new.sprint("Sure please wait while i open chrome!")
        new.browser()
        new.sprint('Please click on the link to open:' + ' https://www.google.com/')
    
    elif qs == 'listen to music':
        new.sprint("Sure please wait while i open Youtube!")
        new.youtube()

    elif qs == 'Order item':
        new.sprint("Sure please wait while i open Amazon!")
        new.amazon()
        new.sprint('Please click on the link to open: ' + 'https://www.amazon.com/')
    elif qs == 'whats the weather like':
        new.weather()
    elif qs == "can you add numbers":
        print('Total is ', TeachMath.add())
    elif qs == "can you subtract numbers":
        print('Total is ', TeachMath.subtraction())
    elif qs == "can you multiply numbers":
        print('Total is ', TeachMath.multiplication())
    elif qs == "can you divide numbers":
        print('Total is ', TeachMath.divison())

    elif qs == "what time is it" or "what is the time" and "whats the time":
        print(time)
  

    if (qs == "quit" or qs == "exit"):
        break
 
    