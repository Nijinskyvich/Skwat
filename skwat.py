# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 16:13:14 2022

@author: Alice
"""

import serial
import time
import winsound
import pyttsx3
import random
import pygame
import threading

from beatDetection import get_beats
from audio import load_sound


song_file = load_sound('https://www.youtube.com/watch?v=zWaymcVmJ-A')

# get song beats
beat_times = get_beats(song_file)

# %%

ser = serial.Serial('COM3', 115200, timeout=1)
time.sleep(2)

score = 0
squat_count = 0
pushup_count = 0
squat_time = time.time()
pushup_time = time.time()

# Start playing song
pygame.init()
rick = pygame.mixer.Sound(song_file)
rick.set_volume(0.2)
pygame.mixer.Channel(0).play(rick)
start_song_time = time.time()

for i in range(100):
    line = ser.readline()
    if line:
        string = line.decode().strip()
        if string == "Squat":
            squat_time_now = time.time()

            # find index of closest beat
            index, value = min(enumerate(beat_times), key=lambda x: abs(x[1] - time.time() + start_song_time))
            time_diff = value - time.time() + start_song_time

            print(time_diff)
            if time_diff > 0.1:
                print("TOO FAST")
            elif time_diff < -0.1:
                print("TOO SLOW")
            else:
                score += 1
                print("Score: ", score)

            # play counting sound - generated using pyttsx
            squat_count += 1
            pygame.mixer.Channel(2).play(pygame.mixer.Sound(f"./audio_count/{squat_count} squat.wav"))

            if squat_time_now - squat_time > 20:
                pygame.mixer.Channel(1).play(pygame.mixer.Sound("Lets Go.wav"))
                print("WELCOME BACK")
            elif squat_time_now - squat_time > 5:
                pygame.mixer.Channel(1).play(pygame.mixer.Sound("Trash_short.wav"))
                print("YOU'RE TRASH")
            else:
                if random.random() < 0.02:
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("goodjob.wav"))
                print("GOOD")

            squat_time = squat_time_now

        if string == "PushUp":
            pushup_time_now = time.time()

            index, value = min(enumerate(beat_times), key=lambda x: abs(x[1] - time.time() + start_song_time))
            time_diff = value - time.time() + start_song_time

            print(time_diff)
            if time_diff > 0.1:
                print("TOO FAST")
            elif time_diff < -0.1:
                print("TOO SLOW")
            else:
                score += 1
                print(score)

            pushup_count += 1
            pygame.mixer.Channel(2).play(pygame.mixer.Sound(f"./audio_count/{pushup_count} pushup.wav"))


            if pushup_time_now - pushup_time > 20:
                pygame.mixer.Channel(1).play(pygame.mixer.Sound("Lets Go.wav"))
                print("WELCOME BACK")
            elif pushup_time_now - pushup_time > 5:
                pygame.mixer.Channel(1).play(pygame.mixer.Sound("Trash_short.wav"))
                print("YOU'RE TRASH")
            else:
                print("GOOD")

ser.close()
print("done")