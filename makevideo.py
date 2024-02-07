import imageio
from skimage.io import imread
import napari

# Function to save the current view as a video
def save_video(viewer, path, fps=1):
    writer = imageio.get_writer(path, fps=fps)

    # Iterate through the time dimension (assumed to be axis 0)
    for i in range(data1.shape[0]):
        viewer.dims.set_point(0, i)  # Update the viewer to show the ith time point
        viewer.camera.angles = (0, 0, 90+5*i)
        viewer.dims.ndisplay = 3
        frame = viewer.screenshot()  # Take a screenshot of the current view
        writer.append_data(frame)  # Add the screenshot to the video
    writer.close()

# Example data (replace these with your actual datasets)
nchannels = [488, 560]
file_pattern = "/Users/andyzjc/Downloads/Test/{}/*.tif"
channels = [imread(file_pattern.format(i)) for i in nchannels]

data1 = channels[0]  # Simulated time series data for layer 1
data2 = channels[1]  # Simulated time series data for layer 2

# Start a Napari viewer
viewer = napari.Viewer()

# Add the datasets as layers to the viewer
# Adjust the colormap, blending, etc., as needed
viewer.add_image(data1, name='488', colormap='bop blue', contrast_limits=[0, 3000], opacity=0.8)
viewer.add_image(data2, name='560', colormap='bop orange', contrast_limits=[0, 3000], opacity=0.8)

# Save the video (adjust path and filename as necessary)
save_video(viewer, 'output_video.mp4')