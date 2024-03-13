import random
from gtts import gTTS 
import os

tex = ["pizza", "icecream", "burger", "fries", "chicken", "pasta", "cake", "donut", "taco", "burrito"]
# Language in which you want to convert 
language = 'es'
for i in tex:
    x = input("Enter the text: ")
    text = random.choice(tex)
    myobj = gTTS(text=i, lang=language, slow=False) 
    tex.remove(text)
    myobj.save("welcome.mp3") 
    os.system("welcome.mp3")