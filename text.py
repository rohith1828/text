import pyttsx3

obj=pyttsx3.init()
s=input("Enter your text:")
obj.say(s)
obj.runAndWait()