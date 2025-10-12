# Example Pwn Challenge - Buffer Overflow

**Category:** pwn  
**Difficulty:** medium  
**Points:** 200  
**Author:** CTF Team

## Description

Can you exploit this simple program to get a shell?

`nc challenge.ctf PORT`

## Solution

### Overview
Classic buffer overflow vulnerability that allows overwriting the return address.

### Steps
1. Analyze the binary to find the buffer size and overflow potential
2. Create a payload that overwrites the return address
3. Point execution to the `win()` function
4. Get the flag from the shell or direct function call

### Flag
`flag{buff3r_0v3rfl0w_pwn3d}`

## Deployment

### Build
```bash
cd src
make
```

### Local Testing
```bash
cd deploy
docker-compose up -d
nc localhost 9999
```

## Files

- `src/vuln.c` - Vulnerable C program
- `src/Makefile` - Build configuration
- `solution/exploit.py` - Pwntools exploit script
- `deploy/` - Docker deployment

## Learning Objectives

- Understanding buffer overflows
- Stack manipulation
- Return address overwriting
- Basic binary exploitation
