#!/usr/bin/env python3
"""
Caesar cipher encryption
"""

def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result

if __name__ == '__main__':
    flag = "flag{caesar_cipher_is_easy}"
    shift = 13  # ROT13
    
    encrypted = caesar_encrypt(flag, shift)
    print(f"Original: {flag}")
    print(f"Encrypted: {encrypted}")
