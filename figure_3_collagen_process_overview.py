import napari
import glob
import os
from skimage import io
import imageio
import numpy as np
import cmap


#some parameter
output = "/Users/andyzjc/Princeton Dropbox/Andy Zhang/Polarizatino Engineered Aberration Robust Adaptive Light Sheet Microscope/Figures/Figure 3/Fig3_3/Data/Panel A/Panel B/"
#color_map = cmap.Colormap('cet_cbl4').lut()
viewer = napari.Viewer()

file = "/Users/andyzjc/Dropbox (Princeton)/Polarizatino Engineered Aberration Robust Adaptive Light Sheet Microscope/Figures/Figure 3/Fig3_3/Data/Panel A/Panel B/take2_Collagen_200nmXStep_PEARLS_NBessel_NA0P6_na0p5_2p5mW_100ms_decon.tif"
image_1 = io.imread(file)
print(file)
# image_1[:,600:1600,:]
layer1 = viewer.add_image(image_1,
                          colormap='inferno',
                          contrast_limits=[15212.796788194444, 136915.17109375], # manually determined
                          opacity=1, gamma=1.2,
                          rendering='attenuated_mip',
                          scale=(1.98, 1, 1),
                          blending='translucent',
                          attenuation=0.11)

viewer.dims.ndisplay = 3
viewer.camera.center =(494.01, 899.5, 514.0)
viewer.camera.angles = (145,-70, 35)
viewer.camera.zoom = 0.37

# bounding box
viewer.layers[0].bounding_box.visible = True
viewer.layers[0].bounding_box.opacity = 0.5
viewer.layers[0].bounding_box.line_color = [1, 1, 1, 1]
viewer.layers[0].bounding_box.points = False

napari.run()