import napari
import glob
import os
from skimage import io
import imageio
import numpy as np
import cmap


#some parameter
output = "/Users/andyzjc/Downloads/cell4/"
color_map = cmap.Colormap('cyan').lut()
viewer = napari.Viewer()

file = "/Users/andyzjc/Downloads/cell4/*.tif"
tiff_files_1 = glob.glob(file)
tiff_files_1.sort()

print(file)

i = 0
for tiff_file_1 in tiff_files_1:
    image_1 = io.imread(tiff_file_1)
    layer1 = viewer.add_image(image_1,
                              colormap=color_map,
                              contrast_limits=[50, 3000], # manually determined
                              opacity=1, gamma=0.5,
                              rendering='mip',
                              blending='translucent')

    viewer.dims.ndisplay = 3
    viewer.scale_bar.visible = False
    viewer.scale_bar.position = 'bottom_left'
    viewer.scale_bar.unit = "pixel"

    save_image = output + f'xz_mip{i}.png'  # Change file extension if necessary-
    frame = viewer.screenshot(path=save_image, size=[1008, 1008])  # Take a screenshot of the current view
    viewer.layers.remove(layer1)
    i += 1

