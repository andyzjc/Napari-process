import os
import subprocess

# Directory containing MP4 files
directory = '/Users/andyzjc/Downloads/Research/Simualtion/Napari-process'

# Output file
output_file = 'output.mp4'

# Create a list of MP4 files in the directory
mp4_files = [f for f in os.listdir(directory) if f.endswith('.mp4')]

# Create a temporary file listing all MP4 files for FFmpeg
list_file_path = os.path.join(directory, 'file_list.txt')
with open(list_file_path, 'w') as list_file:
    for mp4_file in mp4_files:
        list_file.write(f"file '{mp4_file}'\n")

# Build the FFmpeg command
ffmpeg_command = [
    'ffmpeg',
    '-f', 'concat',
    '-safe', '0',
    '-i', list_file_path,
    '-c', 'copy',
    output_file
]

# Run the FFmpeg command
subprocess.run(ffmpeg_command)

# Optional: Remove the temporary list file
os.remove(list_file_path)

print(f"Finished. The output file is {output_file}")
