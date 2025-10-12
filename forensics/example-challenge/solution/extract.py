#!/usr/bin/env python3
"""
Extract flag from steganography challenge
"""

from PIL import Image

def extract_flag(image_path):
    """Extract flag from image metadata"""
    try:
        img = Image.open(image_path)
        
        # Check PNG metadata
        if hasattr(img, 'text'):
            for key, value in img.text.items():
                print(f"Metadata - {key}: {value}")
                if 'flag{' in value:
                    print(f"\n[+] Flag found: {value}")
                    return value
        
        print("[-] No flag found in metadata")
        
    except Exception as e:
        print(f"[-] Error: {e}")

def extract_with_strings():
    """Alternative: use strings command"""
    print("\nAlternative method using strings:")
    print("$ strings image.png | grep flag")

if __name__ == '__main__':
    import sys
    
    if len(sys.argv) > 1:
        extract_flag(sys.argv[1])
    else:
        print("Usage: python extract.py <image_path>")
        extract_with_strings()
