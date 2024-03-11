import numpy as np
import wave
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib import rcParams
import matplotlib


path = r'E:\Blog\source\_posts\CTFTSUNet\CTFTSUNet\ours\rirnoisy_fileid_1001.wav'
save_path = r'E:\Blog\source\_posts\CTFTSUNet\CTFTSUNet\ours\rirnoisy_fileid_1001.png'
f = wave.open(path, "rb")
params = f.getparams()
nchannels, sampwidth, framerate, nframes = params[:4]
str_data = f.readframes(nframes)
DPCRN_wave_data = np.fromstring(str_data, dtype=np.short)

DPCRN_wave_data = DPCRN_wave_data[:160000,]
print(DPCRN_wave_data.shape)
plt.figure(1,dpi=600,figsize=(5,4))

plt.specgram(DPCRN_wave_data,Fs = framerate, NFFT=512*3,noverlap=256*3,scale_by_freq = True, sides = 'default')[0]
plt.xticks(size=5)
plt.yticks(size=5)

plt.subplots_adjust(wspace =0.1, hspace =0.4)
plt.savefig(save_path, bbox_inches='tight', pad_inches=0)
plt.show()
