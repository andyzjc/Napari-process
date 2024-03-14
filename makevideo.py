import napari
import glob
import os
from skimage import io
import imageio
import numpy as np
import cmap
import json

# Function to save the current view as a video
def save_video(tiff_files_1, tiff_files_2, path, fps=30):
    # writer = imageio.get_writer(path, fps=fps)
    #
    # i = 0
    # for tiff_file_1, tiff_file_2 in zip(tiff_files_1, tiff_files_2):
    #     # Read the TIFF files
    #     image_1 = io.imread(tiff_file_1)
    #     image_2 = io.imread(tiff_file_2)
    #
    #     # Start a Napari viewer
    #     viewer = napari.Viewer()
    #
    #     viewer.dims.set_point(0, i)
    #     viewer.add_image(image_1, name='488', colormap='bop blue', contrast_limits=[0, 2000], opacity=0.8)
    #     viewer.add_image(image_2, name='560', colormap='bop orange', contrast_limits=[0, 3000], opacity=0.8)
    #
    #     viewer.dims.ndisplay = 3
    #     viewer.camera.angles = (0, 20 + i * len(tiff_files_1)/180, 90)
    #     frame = viewer.screenshot()  # Take a screenshot of the current view
    #     writer.append_data(frame)  # Add the screenshot to the video
    #     print(i)
    #     i += 1
    #     viewer.close()
    # writer.close()

    writer = imageio.get_writer(path, fps=fps)
    # Start a Napari viewer
    viewer = napari.Viewer()
    viewer.dims.ndisplay = 3

    i = 0
    for tiff_file_1, tiff_file_2 in zip(tiff_files_1, tiff_files_2):
        # Read the TIFF files
        image_1 = io.imread(tiff_file_1)
        image_2 = io.imread(tiff_file_2)

        layer1 = viewer.add_image(image_1, name='488', colormap='bop blue', contrast_limits=[0, 3000], opacity=0.8)
        layer2 = viewer.add_image(image_2, name='560', colormap='bop orange', contrast_limits=[0, 3000], opacity=0.8)

        # viewer.dims.set_point(0, i)
        viewer.camera.angles = (0, 20 + i * len(tiff_files_1) / 180, 90)
        frame = viewer.screenshot()  # Take a screenshot of the current view
        writer.append_data(frame)  # Add the screenshot to the video
        viewer.layers.remove(layer1)
        viewer.layers.remove(layer2)
        print(i)
        i += 1
    writer.close()

def load_bleaching_curve(curve_path):
    with open(curve_path, 'r') as file:
        loaded_data = json.load(file)
        para1 = loaded_data['488']
        para2 = loaded_data['560']
    return para1, para2

# fps = 30
# output_path = 'Z:\Tian-Ming_Fu\Files_from_Janelia\LLS/20201209_LLS\LLCPK1_ER-mEmerald-H2B-mCherry/output_video_cell3_2.mp4'
# writer = imageio.get_writer(output_path, fps=fps)
# photobleaching_curve_path = 'Z:\Tian-Ming_Fu\Files_from_Janelia\LLS/20201209_LLS\LLCPK1_ER-mEmerald-H2B-mCherry\Cell3_Cont\GPUdecon/bleach_curve.json'
# para1, para2 = load_bleaching_curve(photobleaching_curve_path)
# nucleus_cmap = cmap.Colormap('hot').lut()
# membrane_cmap = cmap.Colormap('cyan').lut()
# viewer = napari.Viewer()
# viewer.dims.ndisplay = 3
#
# # show then rotate, then back
# view_angle = np.linspace(start=0, stop=45, num=120)
# view_angle = np.concatenate((view_angle, np.linspace(start=45, stop=0, num=120)), axis=0)

# nchannels = [488, 560]
# file_pattern = "Z:\Tian-Ming_Fu\Files_from_Janelia\LLS/20201209_LLS\LLCPK1_ER-mEmerald-H2B-mCherry\Cell3_Cont\GPUdecon/{}/*.tif"
# channels = [file_pattern.format(i) for i in nchannels]
# tiff_files_1 = glob.glob(channels[0])
# tiff_files_1[1:400] = reversed(tiff_files_1[1:400])
# tiff_files_2 = glob.glob(channels[1])
# tiff_files_2[0:3] = reversed(tiff_files_2[0:3])
# tiff_files_2[3:400] = reversed(tiff_files_2[3:400])
# assert len(tiff_files_1) == len(tiff_files_2), "The number of TIFF files in each folder must be the same."
# # for some bizarre reason, cell3_cont is read-in in reverse order
#
# # set angle, shift center while zooming in
# zoom = np.linspace(start=0.5, stop=2.5, num=120)
# zoom = np.concatenate((zoom, np.linspace(start=2.5, stop=2.5, num=300)), axis=0)
# xcenter = np.linspace(start=500, stop=530, num=120)
# xcenter = np.concatenate((xcenter, np.linspace(start=530, stop=530, num=300)), axis=0)
# ycenter = np.linspace(start=500, stop=300, num=120)
# ycenter = np.concatenate((ycenter, np.linspace(start=300, stop=300, num=300)), axis=0)
#
# load_bleaching_curve()
# i = 0
# for tiff_file_1, tiff_file_2 in zip(tiff_files_1, tiff_files_2):
#     image_1 = io.imread(tiff_file_1)
#     image_2 = io.imread(tiff_file_2)
#     print(tiff_file_1)
#     print(tiff_file_2)
#
#     # Photobleach correction
#     expected_decay1 = para1[0] * np.exp(-para1[1] * i) + para1[2]
#     correction_factor = image_1.mean() / expected_decay1
#     image_1 = image_1 * correction_factor
#
#     expected_decay2 = para2[0] * np.exp(-para2[1] * i) + para2[2]
#     correction_factor = image_2.mean() / expected_decay2
#     image_2 = image_2 * correction_factor
#
#     layer1 = viewer.add_image(image_1, name='488', colormap=membrane_cmap, contrast_limits=[0, 2000], opacity=1)
#     layer2 = viewer.add_image(image_2, name='560', colormap=nucleus_cmap, contrast_limits=[0, 3000], opacity=0.6)
#     napari.run()
#     if i == 0:
#         viewer.dims.ndisplay = 3
#         viewer.camera.center = (0, 500, 500)
#         viewer.camera.angles = (0, 0, 90)
#         viewer.camera.zoom = 0.5
#         frame = viewer.screenshot(size=[1000, 1000])  # Take a screenshot of the current view
#         writer.append_data(frame)  # Add the screenshot to the video
#
#         for one_angle in view_angle:
#             print(one_angle)
#             viewer.camera.angles = (0, one_angle, 90)
#             frame = viewer.screenshot(size=[1000, 1000])  # Take a screenshot of the current view
#             writer.append_data(frame)  # Add the screenshot to the video
#         viewer.layers.remove(layer1)
#         viewer.layers.remove(layer2)
#         i += 1
#     else:
#         viewer.dims.ndisplay = 3
#         viewer.camera.angles = (0, 0, 90)
#         viewer.camera.center = (0, ycenter[i], xcenter[i])
#         viewer.camera.zoom = zoom[i]
#
#         frame = viewer.screenshot(size=[1008, 1008])  # Take a screenshot of the current view
#         writer.append_data(frame)  # Add the screenshot to the video
#         viewer.layers.remove(layer1)
#         viewer.layers.remove(layer2)
#         i += 1
# writer.close()

# test
output_path = 'Z:\Tian-Ming_Fu\Files_from_Janelia\LLS/20201209_LLS\LLCPK1_ER-mEmerald-H2B-mCherry/output_video_cell3_2.mp4'
image_path = 'Z:\Tian-Ming_Fu\Files_from_Janelia\LLS/20201209_LLS\LLCPK1_ER-mEmerald-H2B-mCherry\Cell3_Cont\GPUdecon\dual-color-process/photobleach_test/'
fps = 1
writer = imageio.get_writer(output_path, fps=fps)
photobleaching_curve_path = 'Z:\Tian-Ming_Fu\Files_from_Janelia\LLS/20201209_LLS\LLCPK1_ER-mEmerald-H2B-mCherry\Cell3_Cont\GPUdecon/bleach_curve.json'
para1, para2 = load_bleaching_curve(photobleaching_curve_path)
nucleus_cmap = cmap.Colormap('hot').lut()
membrane_cmap = cmap.Colormap('cyan').lut()
viewer = napari.Viewer()
viewer.dims.ndisplay = 3

nchannels = [488, 560]
file_pattern = "Z:\Tian-Ming_Fu\Files_from_Janelia\LLS/20201209_LLS\LLCPK1_ER-mEmerald-H2B-mCherry\Cell3_Cont\GPUdecon/dual-color-process/{}/*.tif"
channels = [file_pattern.format(i) for i in nchannels]
tiff_files_1 = glob.glob(channels[0])
tiff_files_2 = glob.glob(channels[1])

i = 0
for tiff_file_1, tiff_file_2 in zip(tiff_files_1, tiff_files_2):
    # Read the TIFF files
    image_1 = io.imread(tiff_file_1)
    image_2 = io.imread(tiff_file_2)
    print(tiff_file_1)
    print(tiff_file_2)

    # Photobleach correction
    expected_decay1 = para1['a'] * np.exp(-para1['b'] * i) + para1['c']
    correction_factor1 = image_1.mean() / expected_decay1
    image_1 = image_1 * correction_factor1
    print(correction_factor1)

    expected_decay2 = para2['a'] * np.exp(-para2['b'] * i) + para2['c']
    correction_factor2 = image_2.mean() / expected_decay2
    image_2 = image_2 * correction_factor2
    print(correction_factor2)

    layer1 = viewer.add_image(image_1, name='488', colormap=membrane_cmap, contrast_limits=[0, 2000], opacity= 1)
    layer2 = viewer.add_image(image_2, name='560', colormap=nucleus_cmap, contrast_limits=[0, 3000], opacity= 0.6)

    # viewer.dims.set_point(0, i)
    viewer.camera.center = (0, 300, 530)
    viewer.camera.angles = (0, 0, 90)
    viewer.camera.zoom = 2.5

    save_image = image_path + f'image_{i}.png'  # Change file extension if necessary

    frame = viewer.screenshot(path=save_image, size=[1008, 1008])  # Take a screenshot of the current view
    writer.append_data(frame)  # Add the screenshot to the video
    viewer.layers.remove(layer1)
    viewer.layers.remove(layer2)
    i += 1
writer.close()
