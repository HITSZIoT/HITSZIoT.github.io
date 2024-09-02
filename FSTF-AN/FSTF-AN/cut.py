import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile
from scipy.fft import fft
import soundfile
import librosa
import librosa.display

old_path = r'E:\Blog\source\_posts\FSTF-AN\FSTF-AN\clean\target_fileid_2651.wav'
save_path = r'E:\Blog\source\_posts\FSTF-AN\FSTF-AN\target_fileid_2651.wav'

data, samplerate = soundfile.read(old_path)

data_new = data[:64000]

soundfile.write(save_path, data_new, samplerate)

