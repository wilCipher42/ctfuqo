#!/usr/bin/env python3
"""
Create a simple steganography challenge
Requires: pillow (pip install pillow)
"""

from PIL import Image
from PIL.PngImagePlugin import PngInfo

def create_challenge_image():
    # Create a simple image
    width, height = 800, 600
    img = Image.new('RGB', (width, height), color='blue')
    
    # Add flag to metadata
    metadata = PngInfo()
    metadata.add_text("Comment", "flag{h1dd3n_1n_pl41n_s1ght}")
    
    # Save with metadata
    img.save('image.png', pnginfo=metadata)
    print("[+] Challenge image created: image.png")
    print("[+] Flag hidden in PNG metadata")

if __name__ == '__main__':
    create_challenge_image()
