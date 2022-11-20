# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 03:18:41 2022

@author: Alice
"""

import os
import librosa

def get_beats(filename):
    y, sr = librosa.load(filename)
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    print('Estimated tempo: {:.2f} beats per minute'.format(tempo))
    beat_times = librosa.frames_to_time(beat_frames, sr=sr)

    return beat_times