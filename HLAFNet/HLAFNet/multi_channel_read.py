import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile
from scipy.fft import fft
import soundfile
import librosa
import librosa.display

old_path = r"E:\Temp\Desktop\HLAFNet\HLAFNet\rir\rirnoisy_fileid_1041.wav"

data, samplerate = soundfile.read(old_path)

aa = data[:, 0]

soundfile.write('E:\Temp\Desktop\HLAFNet\HLAFNet\\rir\\rirnoisy_fileid_1041.wav', aa, samplerate, subtype='PCM_16')
