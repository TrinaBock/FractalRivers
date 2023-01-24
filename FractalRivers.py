import noise
import numpy as np
from PIL import Image
import random

# Define the size of the terrain
width = 800
height = 800

# Create a numpy array to hold the fractal terrain
terrain = np.zeros((height, width))

# Define the properties of the fractal terrain
octaves = 8
persistence = 0.5
lacunarity = 2.0
scale = 100.0

# Generate the fractal terrain
for y in range(height):
    for x in range(width):
        terrain[y][x] = noise.pnoise2(x / scale, y / scale, octaves=octaves, persistence=persistence, lacunarity=lacunarity)

# Normalize the fractal terrain
terrain = (terrain + 1) / 2

# Apply a curve to the terrain to create river-like shapes
terrain = terrain * np.exp(-(((x/width - 0.5)**2 + (y/height - 0.5)**2))/(width/8)**2)

# Generate a random color map
color_map = np.zeros((256, 3))
for i in range(256):
    color_map[i] = [random.random(), random.random(), random.random()]

# Create an image from the fractal terrain
image = Image.fromarray((terrain * 255).astype(np.uint8))
image.putpalette(color_map.ravel())
image = image.convert("P")

# Save the image
image.save("fractal_rivers.png")
