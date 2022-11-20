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
from audio import youtube_download


song_file = youtube_download('https://www.youtube.com/watch?v=auAfDfZY7zI')

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


white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

background_colour = (100,100,100)
(width, height) = (900, 600)
display_surface = pygame.display.set_mode((width, height))
pygame.display.flip()
display_surface.fill(background_colour)
pygame.display.set_caption('Skwat Simulator 2022 - GOTY edition')


font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('Score :', True, green, blue)

textRect = text.get_rect()

textRect.center = (width // 2, height // 2)


imp = pygame.image.load("./Tim/SquatUp.png").convert()
imp2 = pygame.image.load("./Tim/SquatDown.png").convert()


done = False
running = True
score = 0
squat_buffer = 0

for i in range(100):
    line = ser.readline()
    if squat_buffer >= 0:
        squat_buffer -=1
    if line:
        string = line.decode().strip()
        if string == "Squat":
            squat_buffer = 2
            display_surface.blit(imp2, (0,0))
            pygame.display.update()
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
            time.sleep(0.1)

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
            squat_buffer = 2
            display_surface.blit(imp2, (0,0))
            pygame.display.update()
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
            time.sleep(0.1)



    #Put voice generation bit here
    #if squat_buffer == 1:
    #    display_surface.blit(imp2, (0,0))
    #else:
    #   display_surface.blit(imp, (0,0))
    display_surface.blit(imp, (0,0))

    display_surface.blit(text, textRect)
    pygame.display.update()
    text = font.render('Score :' + str(score), True, green, blue)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
                running = False
                break # break out of the for loop
    if done:
        break

pygame.display.quit()
pygame.quit()

ser.close()
print("done")