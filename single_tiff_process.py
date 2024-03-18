import napari
import glob
import os
from skimage import io
import imageio
import numpy as np
import cmap


#some parameter
color_map = cmap.Colormap('hot').lut()

viewer = napari.Viewer()
viewer.dims.ndisplay = 3

file = "/Users/andyzjc/Downloads/Fig4_3/Data/single-color/decon/560_5_CamB_ch0_CAM1_stack0299_560nm_3941829msec_0026035961msecAbs_000x_000y_000z_0000t_decon.tif"
image_1 = io.imread(file)
print(file)

layer1 = viewer.add_image(image_1,
                          colormap=color_map,
                          contrast_limits=[0, np.max(image_1)],
                          opacity=1, gamma=0.85,
                          rendering='iso',
                          iso_threshold=55,
                          scale=[1.85, 1, 1])
viewer.scale_bar.visible = True
viewer.scale_bar.position = 'bottom_left'
viewer.scale_bar.unit = "um"


viewer.camera.angles = (90, 0, 90)
viewer.camera.center = (0, 500, 700)
viewer.camera.zoom = 0.9
napari.run()

# XY
# viewer.camera.center = (0,500,700)
# viewer.camera.zoom = 0.85
# viewer.camera.angles = (-82,4.5,78)

#YZ
# viewer.camera.center = (0,500,700)
# viewer.camera.zoom =0.88
# viewer.camera.angles = (-100, 57, 77)
