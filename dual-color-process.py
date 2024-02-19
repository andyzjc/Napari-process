import napari
import glob
import os
from skimage import io
import imageio
import numpy as np
import cmap

output_path = '/Users/andyzjc/Downloads/Test/output/'
nucleus_cmap = cmap.Colormap('hot').lut()
membrane_cmap = cmap.Colormap('cyan').lut()

viewer = napari.Viewer()
viewer.dims.ndisplay = 3

#cell3_cont
nchannels = [488, 560]
file_pattern = "/Users/andyzjc/Downloads/Test/{}/*.tif"
channels = [file_pattern.format(i) for i in nchannels]
tiff_files_1 = glob.glob(channels[0])
# tiff_files_1[1:400] = reversed(tiff_files_1[1:400])
tiff_files_2 = glob.glob(channels[1])
# tiff_files_2[0:3] = reversed(tiff_files_2[0:3])
# tiff_files_2[3:400] = reversed(tiff_files_2[3:400])
assert len(tiff_files_1) == len(tiff_files_2), "The number of TIFF files in each folder must be the same."
# for some bizarre reason, cell3_cont is read-in in reverse order

i = 0
for tiff_file_1, tiff_file_2 in zip(tiff_files_1, tiff_files_2):
    image_1 = io.imread(tiff_file_1)
    image_2 = io.imread(tiff_file_2)
    print(tiff_file_1)
    print(tiff_file_2)

    layer1 = viewer.add_image(image_1, name='488', colormap=membrane_cmap, contrast_limits=[0, 2000], opacity=1)
    layer2 = viewer.add_image(image_2, name='560', colormap=nucleus_cmap, contrast_limits=[0, 3000], opacity=0.6)

    viewer.dims.ndisplay = 3
    viewer.camera.angles = (0, 0, 90)
    viewer.camera.center = (0, 300, 530)
    viewer.camera.zoom = 2.5

    save_image = output_path + f'image_{i}.png'  # Change file extension if necessary

    frame = viewer.screenshot(path=save_image, size=[1000, 1000])  # Take a screenshot of the current view
    viewer.layers.remove(layer1)
    viewer.layers.remove(layer2)
    i += 1