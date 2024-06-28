import napari
import glob
import os
from skimage import io
import imageio
import numpy as np
import cmap

output_path = '/Users/andyzjc/Downloads/'
colormap = cmap.Colormap('yellow').lut()

file_pattern = "/Users/andyzjc/Downloads/*.tif"
tiff_files_1 = glob.glob(file_pattern)
tiff_files_1.sort()

viewer = napari.Viewer()

i = 0
for tiff_file_1 in tiff_files_1:
    print(tiff_file_1)

    image_1 = io.imread(tiff_file_1)

    layer1 = viewer.add_image(image_1, name='fly', colormap=colormap, blending='additive',
                              contrast_limits=[300, 10000], gamma=0.35)

    save_image = output_path + f'image_{i}.png'  # Change file extension if necessary-
    frame = viewer.screenshot(path=save_image, size=[2016, 2016])  # Take a screenshot of the current view
    viewer.layers.remove(layer1)
    i += 1

# first image, zoomed out
# viewer.camera.center = (0, 400, 530)
# viewer.camera.zoom = 0.8