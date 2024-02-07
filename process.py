from skimage.io import imread
from dask import delayed
import dask.array as da
from glob import glob
import napari
from napari_animation import Animation
from scipy import ndimage as ndi

# do something like this:
nchannels = [488, 560]
file_pattern = "/Users/andyzjc/Downloads/Test/{}/*.tif"
channels = [imread(file_pattern.format(i)) for i in nchannels]
# stack[0, 0].compute()  # incurs a single file read

# Load into napari, loop through time, create video
i = 0
for channel_488, channel_560 in zip(channels[0], channels[1]):
    i += 1
    # Load one stack of image
    viewer = napari.Viewer()
    animation = Animation(viewer)

    viewer.add_image(
        channel_488,
        name="488",
        colormap="bop blue",
        multiscale=False,
        contrast_limits=[0, 2000],
        opacity=0.8,
    )

    viewer.add_image(
        channel_560,
        name="560",
        colormap="bop orange",
        multiscale=False,
        contrast_limits=[0, 3000],
        opacity=0.8,
    )

    # create video
    viewer.dims.ndisplay = 3
    viewer.camera.angles = (0, 0, 90)
    animation.capture_keyframe()
    # viewer.camera.zoom = 1
    animation.capture_keyframe()
    # viewer.camera.angles = (-7.0, 15.7, 62.4)
    # animation.capture_keyframe(steps=30)
    # viewer.camera.angles = (2.0, -24.4, -36.7)
    # animation.capture_keyframe(steps=60)
    # viewer.reset_view()
    # viewer.camera.angles = (0.0, 0.0, 90.0)
    # animation.capture_keyframe()

    animation.animate(f"animate3D{i}.mp4", canvas_only=True)
