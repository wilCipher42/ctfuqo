# Example Misc Challenge - Linux Commands

**Category:** misc  
**Difficulty:** easy  
**Points:** 50  
**Author:** CTF Team

## Description

Connect to our server and find the hidden flag!

`ssh ctf@challenge.ctf`

Password: `welcome123`

## Solution

### Overview
Navigate through a Linux system to find hidden files and the flag.

### Steps
1. Connect via SSH
2. List all files including hidden: `ls -la`
3. Find the flag file: `find / -name "*flag*" 2>/dev/null`
4. Or search in common locations: `/home`, `/tmp`, `/opt`
5. Read the flag: `cat /path/to/flag.txt`

### Flag
`flag{l1nux_c0mm4nds_4r3_p0w3rful}`

## Deployment

### Local Testing
```bash
cd deploy
docker compose up -d
ssh -p 2222 ctf@localhost
# Password: welcome123
```

## Files

- `src/setup.sh` - Setup script for the challenge environment
- `deploy/Dockerfile` - Container with SSH server
- `deploy/docker-compose.yml` - Deployment configuration

## Learning Objectives

- Basic Linux command line navigation
- File system exploration
- Finding hidden files
- Using common Linux utilities
