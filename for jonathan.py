import tempfile
import echonest.remix.audio as audio
from echonest.remix.support.ffmpeg import ffmpeg
import matplotlib.pyplot as plt
from matplotlib.pyplot import draw, plot, show
import numpy as np
import os
import wave
import sys
import random as r
import aqplayer
import time
import pygame
import multiprocessing

filename = "05.mp3"
af = audio.LocalAudioFile(filename)
tats = af.analysis.tatums
sects = af.analysis.sections
bars = af.analysis.bars
beats = af.analysis.beats
audio_data = af.render().data
audio_data = (audio_data[:,0] + audio_data[:,1]) / 2


# Plot sections
for sect in sects:
    plot([sect.start, sect.start], [-10000, 10000], linewidth=2, color='r')

# Plot beats
for beat in beats:
    plot([beat.start, beat.start], [-2500, 2500], linewidth=2, color='g')

# Plot bars
for bar in bars:
    plot([bar.start, bar.start], [-5000, 5000], linewidth=2, color='black')

# Plot tatums LAST!!
for tat in tats:
    beginning = int(tat.start *44100)
    end = int((tat.start + tat.duration) * 44100)
    data = audio_data[beginning:end]
    if tat.absolute_context()[0] % 2 == 0:
        plot([tat.start, tat.start + tat.duration], [r.uniform(0.75, 1.0) * np.amin(data), r.uniform(0.75, 1.0) * np.amax(data)], linewidth=.75, color='b')
    else:
        plot([tat.start, tat.start + tat.duration], [r.uniform(0.75, 1.0) * np.amax(data), r.uniform(0.75, 1.0) * np.amin(data)], linewidth=.75, color='b')
def playstuff():
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue

def playstuff2():
    player = aqplayer.Player()
    player.play(beats)

def graphstuff():
    show()

def graphcurrenttime():
    for i in range(len(tats)):
        plot([tats[i].start, tats[i].start], [-10000,10000], linewidth = 1, color='y')

if __name__ == '__main__':
    p1 = multiprocessing.Process(target=playstuff)
    p1.start()
    p2 = multiprocessing.Process(target=graphstuff)
    p2.start()
    p1.join()
    p2.join()
