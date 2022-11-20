# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 16:39:59 2022

@author: Alice
"""

from pytube import YouTube
import os
import subprocess

def convert_to_wav(file):
    # convert mp3 to wav file
    newfile = file.split('.')[0]
    subprocess.call(["ffmpeg", "-i", file,
                     f"{newfile}.wav"])
    return newfile

def youtube_download(url):
    #yt_letsgo = YouTube('https://www.youtube.com/watch?v=YZAQBG4Qbt8')
    #yt_yourtrash = YouTube('https://www.youtube.com/watch?v=ftrSAhq_Qm8')
    #yt_rickroll = YouTube('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    yt = YouTube(url)

    video = yt.streams.filter(only_audio=True).first()

    out_file = video.download(output_path=".")

    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    return new_file

def load_sound(url):
    new_file = youtube_download(url)
    return convert_to_wav(new_file)

'''
# %% Try text to voice
# importing the pyttsx library
import pyttsx3

# initialisation
engine = pyttsx3.init()
voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
engine.setProperty('voice', voice_id)
engine.setProperty('rate', 120)
# testing
engine.say("skwat")
engine.runAndWait()
engine.stop()
'''
