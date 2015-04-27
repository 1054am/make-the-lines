__author__ = 'Austin'
import matplotlib.pyplot as plt
import time
import echonest.remix.audio as audio
import numpy as np
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

plt.ion()

for sect in sects:
    plt.plot([sect.start, sect.start], [-10000, 10000], linewidth=2, color='r')

for beat in beats:
    plt.plot([beat.start, beat.start], [-2500, 2500], linewidth=2, color='g')

for bar in bars:
    plt.plot([bar.start, bar.start], [-5000, 5000], linewidth=2, color='black')

for tat in tats:
    beginning = int(tat.start *44100)
    end = int((tat.start + tat.duration) * 44100)
    data = audio_data[beginning:end]
    if tat.absolute_context()[0] % 2 == 0:
        plt.plot([tat.start, tat.start + tat.duration], [np.amin(data), np.amax(data)], linewidth=.75, color='b')
    else:
        plt.plot([tat.start, tat.start + tat.duration], [np.amax(data), np.amin(data)], linewidth=.75, color='b')
plt.xlim([0,30])
plt.draw()

# time.sleep(1)

def playstuff():
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        for i in range(len(beats)):
            plt.plot([beats[i].start, beats[i].start] , [-5000, 5000], linewidth=3, color='y')
            time.sleep(.15)
            plt.draw()

def graphcurrenttime():
    for i in range(len(tats)):
        plt.plot([i, i] , [-5000, 5000], linewidth=3, color='y')
        time.sleep(1)
    plt.draw()

playstuff()
