import napari
import glob
import os
from skimage import io
import imageio
import numpy as np
import cmap

output_path = '/Users/andyzjc/Dropbox (Princeton)/Polarizatino Engineered Aberration Robust Adaptive Light Sheet Microscope/Figures/Figure 6/Fig6_2/data/fly/dual color/processed/onecolor_z/'
nucleus_cmap = cmap.Colormap('magenta').lut()
membrane_cmap = cmap.Colormap('yellow').lut()

nchannels = ['CamA', 'CamB']
file_pattern = "/Users/andyzjc/Dropbox (Princeton)/Polarizatino Engineered Aberration Robust Adaptive Light Sheet Microscope/Figures/Figure 6/Fig6_2/data/fly/dual color/{}/z/*.tif"
channels = [file_pattern.format(i) for i in nchannels]
tiff_files_1 = glob.glob(channels[0])
tiff_files_1.sort()
tiff_files_2 = glob.glob(channels[1])
tiff_files_2.sort()

first_image_488 = io.imread(tiff_files_1[0])
first_mean488 = np.mean(first_image_488.reshape(-1))
first_max488 = np.max(first_image_488.reshape(-1))
bg488 = 50

first_image_560 = io.imread(tiff_files_2[0])
first_mean560 = np.mean(first_image_560.reshape(-1))
first_max560 = np.max(first_image_560.reshape(-1))
bg560 = 225

viewer = napari.Viewer()
i = 0
for tiff_file_1,tiff_file_2 in zip(tiff_files_1,tiff_files_2):

    # image_1 = io.imread(tiff_file_1)
    # frame488_corrected = (first_mean488 ) / (np.mean(image_1.reshape(-1))) * (image_1 )
    # print(tiff_file_1)

    image_2 = io.imread(tiff_file_2)
    frame560_corrected = (first_mean560) / (np.mean(image_2.reshape(-1)) ) * (image_2 )
    print(tiff_file_2)

    # layer1 = viewer.add_image(frame488_corrected,
    #                           colormap=nucleus_cmap,
    #                           contrast_limits=[50, 1000], # manually determined
    #                           opacity=1, gamma=0.4,
    #                           rendering='mip',
    #                           blending='translucent')

    layer2 = viewer.add_image(frame560_corrected,
                              colormap=membrane_cmap,
                              contrast_limits=[225, 1300], # manually determined
                              opacity=1, gamma=0.5,
                              rendering='mip',
                              blending='additive')
    viewer.dims.ndisplay = 2
    viewer.camera.center = (0, 900, 2300) # y and z
    #viewer.camera.center = (0, 500, 1000) # x
    viewer.camera.zoom = 0.3

    save_image = output_path + f'z_mip{i}.png'  # Change file extension if necessary-
    frame = viewer.screenshot(path=save_image, size=[1008, 1008])  # Take a screenshot of the current view
    # viewer.layers.remove(layer1)
    viewer.layers.remove(layer2)
    i += 1