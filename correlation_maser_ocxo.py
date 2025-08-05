# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import os
import numpy.fft as ft
import scipy as sp
import scipy.fft as sf
import logging
import datetime

maser_file_path_pol1 = 'MASER_Pol1_NGin_09may24.raw'
rubidium_file_path_pol1 = 'OCXO_Pol1_NGin_09may24.raw'

maser_file_path_pol2 = 'MASER_Pol2_NGin_09may24.raw'
rubidium_file_path_pol2 = 'OCXO_Pol2_NGin_09may24.raw'

mode = 1
#1 for m1 r1
#2 for m2 r2
#3 for m1 m2
#4 for r1 r2
#5 for m2-r1
#6 for m1-m1
#7 for m2-m2
#8 for r1-r1
#9 for r2-r2

N=7200
f = np.fft.rfftfreq(7500,1/75000000)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

print(f"STARTING CODE RUN WITH MODE {mode}")
print()
print("-----------------------------------")

if mode == 1:
  file1 = maser_file_path_pol1
  file2 = rubidium_file_path_pol1

elif mode == 2:
  file1 = maser_file_path_pol2
  file2 = rubidium_file_path_pol2

elif mode == 3:
  file1 = maser_file_path_pol1
  file2 = maser_file_path_pol2

elif mode == 4:
  file1 = rubidium_file_path_pol1
  file2 = rubidium_file_path_pol2

elif mode == 5:
    file1 = maser_file_path_pol2
    file2 = rubidium_file_path_pol1
    
elif mode == 6:
    file1 = maser_file_path_pol1
    file2 = maser_file_path_pol1

elif mode == 7:
    file1 = maser_file_path_pol2
    file2 = maser_file_path_pol2

elif mode == 8:
    file1 = rubidium_file_path_pol1
    file2 = rubidium_file_path_pol1

elif mode == 9:
    file1 = rubidium_file_path_pol2
    file2 = rubidium_file_path_pol2

X=np.zeros([N,3751], dtype=np.complex)
Y=np.zeros([N,7500], dtype=np.complex)

for i in np.arange(N):
  logging.info(f"Running iteration number {i}")

  logging.info(f"Reading file data for iteration {i}")
  file_data_1 = np.fromfile(file1, count=75000000, offset = i*75000000, dtype=np.int8).astype(np.float).reshape([-1,7500])
  file_data_2 = np.fromfile(file2, count=75000000, offset = i*75000000, dtype=np.int8).astype(np.float).reshape([-1,7500])

  # logging.info(f"Computing correlation for iteration {i}")
  # correlation = np.correlate(file_data_1.flatten(), file_data_2.flatten(), mode='full')

  logging.info(f"Performing FFT for iteration {i}")
  file_1_fft = sf.rfft(file_data_1, axis=1)
  file_2_fft = sf.rfft(file_data_2, axis=1)

  X[i,:] = (file_1_fft * np.conj(file_2_fft)).mean(0)
  # Y[i,:] = (correlation).mean(0)

  logging.info(f"Done iteration number {i}")

np.save(f'mode-{mode}-Xspec.npy', X)
# np.save(f'mode-{mode}-yspec.npy', Y)

print("ALL ITERATIONS COMPLETED")

plt.semilogy(f/1E6, np.abs(X[:,:]).T)
plt.title("Amplitude vs Frequency")
plt.xlabel("Amplitude")
plt.ylabel("Phase")
#plt.savefig(f'amp_vs_freq_{mode}.png')
plt.close()

plt.plot(np.angle(X[:,:])*180/np.pi)
plt.title("Phase plot")
#plt.savefig(f'phase_{mode}.png')
plt.close()

print()
print("CODE RUN SUCCESS")
