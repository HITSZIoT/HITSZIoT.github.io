import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile
from scipy.fft import fft
import soundfile
import librosa
import librosa.display

old_path = r'E:\Blog\source\_posts\FSformer\FSformer\real\SpatialNet2.wav'
save_path = r'E:\Blog\source\_posts\FSformer\FSformer\real\SpatialNet2_gai.wav'

zeros = np.zeros(128)

data, samplerate = soundfile.read(old_path)

data_new = np.concatenate((data, zeros))

soundfile.write(save_path, data_new, samplerate)

