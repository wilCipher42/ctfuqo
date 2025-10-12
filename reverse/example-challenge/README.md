# Example Reverse Engineering Challenge

**Category:** reverse  
**Difficulty:** easy  
**Points:** 150  
**Author:** CTF Team

## Description

Analyze this binary to find the secret flag!

Download: `challenge.bin`

## Solution

### Overview
Simple password checking program that can be reversed by analyzing strings or using a debugger.

### Steps
1. Run `strings challenge` to look for interesting strings
2. Or use a decompiler like Ghidra or IDA
3. Find the hardcoded flag in the binary
4. Alternative: Run the program and input the correct password found in the binary

### Flag
`flag{r3v3rs3_3ng1n33r1ng_fun}`

## Deployment

No server deployment needed - distribute the binary file.

## Files

- `src/challenge.c` - Original source code
- `src/Makefile` - Build configuration
- `solution/` - Analysis notes and solution steps

## Learning Objectives

- Basic reverse engineering techniques
- Using tools like strings, objdump, Ghidra
- Understanding compiled binaries
- Static analysis
