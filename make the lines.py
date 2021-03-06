import tempfile
import echonest.remix.audio as audio
from echonest.remix.support.ffmpeg import ffmpeg
import matplotlib.pyplot as plt
import numpy as np
import os
import wave
from scipy.io.wavfile import read
import sys

filename = "05.mp3"
af = audio.LocalAudioFile(filename)
tats = af.analysis.tatums
tats_range = []
starts = []
ends = []
for tat in tats:
    tats_range.append((int(tat.start * 44100),  int(tat.start * 44100 + tat.duration * 44100)))
for i in tats_range:
    starts.append(i[0])
    ends.append(i[1])


print tats_range

data = af.render().data
data = (data[:,0] + data[:,1]) / 2
print type(data)
"""
for i in range(len(tats_range)):
    d = data[tats_range[i][0]:tats_range[i][1]]
    print np.amin(d), np.amax(d)
    if i % 2 == 0:
        plt.plot([tats[i].start, tats[i].start + tats[i].duration], [np.amin(d), np.amax(d)], linewidth=0.5, color='b')
    else:
        plt.plot([tats[i].start, tats[i].start + tats[i].duration], [np.amax(d), np.amin(d)], linewidth=0.5, color='b')
"""

for tat in tats:
    beginning = int(tat.start *44100)
    end = int((tat.start + tat.duration) * 44100)
    data = data[beginning:end]
    if tat.absolute_context()[0] % 2 == 0:
        plt.plot([tats.start, tats.start + tats.duration], [np.amin(data), np.amax(data)], linewidth=0.5, color='b')
    else:
        plt.plot([tats.start, tats.start + tats.duration], [np.amax(data), np.amin(data)], linewidth=0.5, color='b')

# for i in range(len(tats_range)):


plt.plot(data[:44100])
plt.plot([100000,100000], [-5000,5000], linewidth=2.0)

plt.show()
#signal = np.fromstring(signal, 'Int16')
#fs = spf.getframerate()

#If Stereo
"""
times = np.arange(len(data))/float(rate)
plt.title('Signal Wave...')

plt.plot(x= times,y = data)
plt.show()

samplerate, data = read(file_to_read)
times = np.arange(len(data))/float(samplerate)

# Make the plot
# You can tweak the figsize (width, height) in inches
plt.figure(figsize=(30, 4))
plt.fill_between(times, data[:,0], data[:,1], color='k')
plt.xlim(times[0], times[-1])
plt.xlabel('time (s)')
plt.ylabel('amplitude')
# You can set the format by changing the extension
# like .pdf, .svg, .eps
plt.savefig('plot.png', dpi=100)
plt.show()
import matplotlib.pyplot as plt
import numpy as np
import wave
import sys


spf = wave.open(file_to_read,'r')

#Extract Raw Audio from Wav File
signal = spf.readframes(-1)
signal = np.fromstring(signal, 'Int16')
fs = spf.getframerate()

#If Stereo
if spf.getnchannels() == 2:
    print 'Just mono files'
    sys.exit(0)


Time=np.linspace(0, len(signal)/fs, num=len(signal))

plt.figure(1)
plt.title('Signal Wave...')
plt.plot(Time,signal)
plt.show()
"""
