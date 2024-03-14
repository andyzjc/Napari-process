import os
import json
import glob
from skimage import io
import numpy as np
import cmap
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def exponential_decay(t,a,b,c):
    return a * np.exp(-b*t) + c

output = 'Z:\Tian-Ming_Fu\Files_from_Janelia\LLS/20201209_LLS\LLCPK1_ER-mEmerald-H2B-mCherry\Cell3_Cont\GPUdecon/bleach_curve.json'
nucleus_cmap = cmap.Colormap('hot').lut()
membrane_cmap = cmap.Colormap('cyan').lut()

#cell3_cont
nchannels = [488, 560]
file_pattern = "Z:\Tian-Ming_Fu\Files_from_Janelia\LLS/20201209_LLS\LLCPK1_ER-mEmerald-H2B-mCherry\Cell3_Cont\GPUdecon/dual-color-process/{}/*.tif"
channels = [file_pattern.format(i) for i in nchannels]
tiff_files_1 = glob.glob(channels[0])
# tiff_files_1[1:400] = reversed(tiff_files_1[1:400])
tiff_files_2 = glob.glob(channels[1])
# tiff_files_2[0:3] = reversed(tiff_files_2[0:3])
# tiff_files_2[3:400] = reversed(tiff_files_2[3:400])
assert len(tiff_files_1) == len(tiff_files_2), "The number of TIFF files in each folder must be the same."
# for some bizarre reason, cell3_cont is read-in in reverse order

mean_1 = np.zeros(shape=(len(tiff_files_1)))
mean_2 = np.zeros(shape=(len(tiff_files_2)))

i = 0
for tiff_file_1, tiff_file_2 in zip(tiff_files_1, tiff_files_2):
    image_1 = io.imread(tiff_file_1)
    image_2 = io.imread(tiff_file_2)
    print(tiff_file_1)
    print(tiff_file_2)

    # calculate mean
    mean_1[i] = image_1.mean()
    mean_2[i] = image_2.mean()
    i += 1

# fit in exponential
time_point = np.arange(len(mean_1))
t1 = curve_fit(exponential_decay, time_point, mean_1)
t2 = curve_fit(exponential_decay, time_point, mean_2)

# save in json
curve = {
    "488": {
        "a": t1[0][0],
        "b": t1[0][1],
        "c": t1[0][2]},
    "560": {
        "a": t2[0][0],
        "b": t2[0][1],
        "c": t2[0][2],
    }
}

with open(output, 'w') as file:
    json.dump(curve, file)
    file.close()

# save plot