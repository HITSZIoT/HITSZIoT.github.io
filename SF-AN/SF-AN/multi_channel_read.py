import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile
from scipy.fft import fft
import soundfile
import librosa
import librosa.display

old_path = r"C:\Users\Administrator\Desktop\111\EaBNet.wav"

data, samplerate = soundfile.read(old_path)

aa = data[:, 0]

soundfile.write('EaBNet.wav', aa, samplerate, subtype='PCM_16')
