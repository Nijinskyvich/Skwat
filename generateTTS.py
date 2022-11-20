# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 04:44:34 2022

@author: Alice
"""

import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 120)

for i in range(50):
    text = f"{i} pushup"
    engine.save_to_file(text, f'./audio_count/{text}.wav')
    engine.runAndWait()