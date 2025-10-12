#!/usr/bin/env python3
"""
Caesar cipher decryption - tries all possible shifts
"""

def caesar_decrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
        else:
            result += char
    return result

def brute_force_caesar(encrypted_text):
    """Try all 26 possible shifts"""
    print("Trying all possible shifts:\n")
    
    for shift in range(26):
        decrypted = caesar_decrypt(encrypted_text, shift)
        print(f"Shift {shift:2d}: {decrypted}")
        
        # Check if it looks like a flag
        if decrypted.startswith('flag{'):
            print(f"\n[+] Found the flag: {decrypted}")
            return decrypted
    
    return None

if __name__ == '__main__':
    encrypted = "synf{pnrfne_pvcure_vf_rnfl}"
    print(f"Encrypted message: {encrypted}\n")
    brute_force_caesar(encrypted)
