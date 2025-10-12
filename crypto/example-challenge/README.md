# Example Crypto Challenge - Caesar Cipher

**Category:** crypto  
**Difficulty:** easy  
**Points:** 100  
**Author:** CTF Team

## Description

We intercepted an encrypted message. Can you decrypt it?

Encrypted message: `synf{pnrfne_pvcure_vf_rnfl}`

## Solution

### Overview
This is a classic Caesar cipher (ROT13 variant) encryption.

### Steps
1. Recognize the pattern - the message starts with what looks like "flag" encoded
2. Try different Caesar cipher shifts
3. ROT13 (shift of 13) reveals the flag

### Flag
`flag{caesar_cipher_is_easy}`

## Deployment

No deployment needed - this is a static challenge.

## Files

- `src/encrypt.py` - Script used to create the challenge
- `solution/decrypt.py` - Decryption solution

## Learning Objectives

- Understanding classical ciphers
- Pattern recognition in cryptography
- Frequency analysis basics
- Brute force approach for small keyspaces
