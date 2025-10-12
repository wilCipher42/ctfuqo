# Example Forensics Challenge - Image Steganography

**Category:** forensics  
**Difficulty:** easy  
**Points:** 100  
**Author:** CTF Team

## Description

We found this image at a crime scene. There seems to be more to it than meets the eye...

Download: `image.png`

## Solution

### Overview
The flag is hidden in the image using LSB (Least Significant Bit) steganography.

### Steps
1. Download the image file
2. Use `strings` command: `strings image.png | grep flag`
3. Or use steganography tools like `steghide`, `zsteg`, or `stegsolve`
4. The flag is embedded in the image metadata or LSB

### Flag
`flag{h1dd3n_1n_pl41n_s1ght}`

## Deployment

No server deployment needed - distribute the image file.

## Files

- `src/create_challenge.py` - Script to create the challenge image
- `src/image.png` - Challenge image (not committed to avoid spoilers)
- `solution/` - Solution scripts and tools

## Learning Objectives

- Understanding image file formats
- Basic steganography concepts
- Using forensics tools
- Metadata analysis
