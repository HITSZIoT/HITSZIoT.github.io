import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile
from scipy.fft import fft
import soundfile
import librosa
import librosa.display

old_path = r'E:\Blog\source\_posts\CTFTSUNet\CTFTSUNet\clean\target_fileid_1041.wav'
save_path = r'E:\Blog\source\_posts\CTFTSUNet\CTFTSUNet\clean\target_fileid_1041.png'

data, samplerate = soundfile.read(old_path)

soundfile.write('new.wav', data, samplerate, subtype='PCM_16')
path = r"E:\Blog\source\_posts\CTFTSUNet\CTFTSUNet\new.wav"

# 读取音频，采样率为44100Hz，持续时间为2秒
y, sr = librosa.load(path, sr=16000)

# 将 stft 之后的 幅度值的绝对值 转换为 分贝值，将返回值传入specshow()方法中
data = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)

# 绘制图像
plt.rcParams['font.sans-serif'] = 'times new roman'

fig, ax = plt.subplots(1, 1)
# x轴是时间（单位：秒），y轴是由fft窗口和采样率决定的频率值（单位：Hz）
img = librosa.display.specshow(data, sr=sr, x_axis='time', y_axis='linear')
# plt.ylim(0, 8500) # 8000Hz以上没有能量显示，因此y轴上限设为8500
# plt.title('CTFUNet 语谱图', fontproperties="SimSun", fontsize=16)
fig.colorbar(img, ax=ax, format="%+2.f dB")

plt.savefig(save_path, bbox_inches='tight', pad_inches=0, dpi=600)
plt.show()
