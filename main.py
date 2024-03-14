import random
from gtts import gTTS 
import os
from pathlib import Path
import pygame

pygame.mixer.init()
tex = ["¿Cómo te llamas?",
"¿Cuántos años tienes?",
"¿Cuándo es tu cumpleaños?",
"¿Cúal es la fecha de hoy?",
"¿Qué día es?",
"¿Qué hora es?",
"¿Qué te gusta hacer?",
"¿Qué le gusta hacer a tu mejor amigo?",
"¿Qué no te gusta hacer?"
]
# Language in which you want to convert 
language = 'es'
for i in range(len(tex)):
    text = random.choice(tex)
    myobj = gTTS(text=text, lang=language, slow=True) 
    tex.remove(text)
    myobj.save(f"welcome{i}.mp3")
    pygame.mixer.music.load(f"welcome{i}.mp3")
    pygame.mixer.music.play()
    x = input("enter text")