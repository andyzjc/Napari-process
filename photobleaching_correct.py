import os
import json
import tifffile
import glob
import os
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

    i += 1

# Function to calculate correction curve
def calculate_correction_curve(image_stack):
    # Assume photobleaching correction is based on the average intensity of each frame
    mean_intensities = image_stack.mean(axis=(1, 2))
    # Use linear regression for simplicity; you might need a more complex model
    slope, intercept, _, _, _ = linregress(range(len(mean_intensities)), mean_intensities)
    return slope, intercept


# Loop through all tiff files
for filename in os.listdir(tiff_directory):
    if filename.endswith(".tif") or filename.endswith(".tiff"):
        file_path = os.path.join(tiff_directory, filename)

        # Read the 3D stack file
        with tifffile.TiffFile(file_path) as tif:
            image_stack = tif.asarray()

        # Calculate correction curve
        slope, intercept = calculate_correction_curve(image_stack)

        # Save the correction curve parameters
        correction_info = {
            'slope': slope,
            'intercept': intercept
        }
        with open(os.path.join(correction_directory, filename.replace('.tif', '_correction.json')), 'w') as json_file:
            json.dump(correction_info, json_file)

        # Apply correction and save corrected image
        corrected_stack = np.zeros_like(image_stack)
        for i in range(image_stack.shape[0]):
            # Adjust based on the correction curve, ensuring no negative values
            corrected_stack[i] = np.clip(image_stack[i] - (slope * i + intercept), 0, None)

        # Save the corrected stack
        corrected_filename = filename.replace('.tif', '_corrected.tif')
        tifffile.imwrite(os.path.join(tiff_directory, corrected_filename), corrected_stack)

print("Photobleaching correction completed.")