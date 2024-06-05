import numpy as np
import wave
import matplotlib.pyplot as plt
import librosa

f1 = wave.open(r'E:\Blog\source\_posts\CTFTSUNet\CTFTSUNet\clean\target_fileid_793.wav')
f2 = wave.open(r'E:\Blog\source\_posts\CTFTSUNet\CTFTSUNet\clean\target_fileid_1041.wav')
save_path = r'E:\Blog\source\_posts\CTFTSUNet\CTFTSUNet\wav3.png'
# 读取格式信息
params1 = f1.getparams()
nchannnels1, sampwidth1, framerate1, nframes1 = params1[:4]
# 读取波形数据
strData1 = f1.readframes(nframes1)
# 将字符串转换为16位整数
waveData1 = np.frombuffer(strData1, dtype=np.int16)
# 幅值归一化
waveData1 = waveData1 * 1.0 / (max(abs(waveData1)))

params2 = f2.getparams()
nchannnels2, sampwidth2, framerate2, nframes2 = params2[:4]
# 读取波形数据
strData2 = f2.readframes(nframes2)
# 将字符串转换为16位整数
waveData2 = np.frombuffer(strData2, dtype=np.int16)
# 幅值归一化
waveData2 = waveData2 * 1.0 / (max(abs(waveData2)))
# 计算音频的时间
time = np.arange(0, nframes1) * (1.0 / framerate1)
# 绘图
plt.figure(figsize=(14, 5))
plt.plot(time, waveData1)
plt.plot(time, waveData2, color='red')
plt.xlabel("Time(s)")
plt.ylabel("Amplitude")
plt.title("Single channel waveData")

plt.savefig(save_path, bbox_inches='tight', pad_inches=0)
plt.show()

# path = r'E:\Blog\source\_posts\CTFTSUNet\CTFTSUNet\clean\target_fileid_793.wav'
# save_path = r'E:\Blog\source\_posts\CTFTSUNet\CTFTSUNet\clean\wav1.png'
# f = wave.open(path, "rb")
# params = f.getparams()
# nchannels, sampwidth, framerate, nframes = params[:4]
# str_data = f.readframes(nframes)
# DPCRN_wave_data = np.fromstring(str_data, dtype=np.short)
#
# DPCRN_wave_data = DPCRN_wave_data[:160000,]
# print(DPCRN_wave_data.shape)
# plt.figure(1,dpi=600,figsize=(5,4))
#
# plt.specgram(DPCRN_wave_data,Fs = framerate, NFFT=512*3,noverlap=256*3,scale_by_freq = True, sides = 'default')[0]
# plt.xticks(size=5)
# plt.yticks(size=5)
#
# plt.subplots_adjust(wspace =0.1, hspace =0.4)
# plt.savefig(save_path, bbox_inches='tight', pad_inches=0)
# plt.show()
