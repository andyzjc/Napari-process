import napari
import glob
import os
from skimage import io
import imageio

# Function to save the current view as a video
def save_video(tiff_files_1, tiff_files_2, path, fps=10):
    writer = imageio.get_writer(path, fps=fps)

    i = 0
    for tiff_file_1, tiff_file_2 in zip(tiff_files_1, tiff_files_2):
        # Read the TIFF files
        image_1 = io.imread(tiff_file_1)
        image_2 = io.imread(tiff_file_2)

        # Start a Napari viewer
        viewer = napari.Viewer()

        viewer.dims.set_point(0, i)
        viewer.add_image(image_1, name='488', colormap='bop blue', contrast_limits=[0, 3000], opacity=0.8)
        viewer.add_image(image_2, name='560', colormap='bop orange', contrast_limits=[0, 3000], opacity=0.8)

        viewer.dims.ndisplay = 3
        viewer.camera.angles = (0, 20 + i * len(tiff_files_1)/180, 90)
        frame = viewer.screenshot()  # Take a screenshot of the current view
        writer.append_data(frame)  # Add the screenshot to the video
        print(i)
        i += 1
    writer.close()

# Example data (replace these with your actual datasets)
nchannels = [488, 560]
file_pattern = "/Users/andyzjc/Downloads/Test/{}/*.tif"
channels = [file_pattern.format(i) for i in nchannels]

# Get sorted lists of TIFF files for each wavelength/color
tiff_files_1 = glob.glob(channels[0])
tiff_files_2 = glob.glob(channels[1])

# Check if the number of files in both folders is the same
assert len(tiff_files_1) == len(tiff_files_2), "The number of TIFF files in each folder must be the same."

# Save the video (adjust path and filename as necessary)
save_video(tiff_files_1, tiff_files_2, 'output_video4.mp4')


