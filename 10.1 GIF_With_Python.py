import imageio.v3 as imageio
import os

folder_path = r"C:\Users\erikm\Pictures\PythonGifCodedex"

filenames = [
    os.path.join(folder_path, f)
    for f in os.listdir(folder_path)
    if f.lower().endswith(('.png', '.jpg', '.jpeg'))
]

filenames.sort()

images = [imageio.imread(f) for f in filenames]

imageio.imwrite(
    os.path.join(folder_path, 'animatsioon.gif'),
    images,
    duration=500,  
    loop=0
)

print("✅ GIF loodud:", os.path.join(folder_path, 'animatsioon.gif'))

