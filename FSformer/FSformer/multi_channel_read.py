import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile
from scipy.fft import fft
import soundfile
import librosa
import librosa.display

old_path = r"C:\Users\Administrator\Desktop\技巧\一些程序\1988-24833-0027.wav"

data, samplerate = soundfile.read(old_path)

aa = data[:, 0]

soundfile.write('new.wav', aa, samplerate, subtype='PCM_16')
path = r"C:\Users\Administrator\Desktop\技巧\一些程序\new.wav"
