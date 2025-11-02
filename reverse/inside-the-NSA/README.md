# Reverse Engeneering Challenge - Inside the NSA

**Category:** reverse  
**Difficulty:** meduim  
**Points:** 100  
**Author:** CTF Team

## Description

A simple homepage hides more than it seems — can you trace the digital breadcrumbs from code to image to uncover the flag?

Connect to the challenge at: `http://SERVER_IP_ADDRESS:8183`

## Solution

### Overview
This challenge demonstrates a multi-stage investigation that combines forensics, steganography, and reverse engineering concepts. 

### Steps
1. Navigate to the home page `http://SERVER_IP_ADDRESS:8183`
2. We see a flagrant binary code. Maybe a hidden message ?
3. Decode the binary code. We can use an online tool to convert binary code to ASCII
4. The text doesn't help. Let's go back to the home page.
5. There is an image: the NSA emblem
6. Download it and inspect it.
7. It seems normal at first glance but let's check the metada for hidden comments, messages, hint,..
8. We can use tools like exiftool or strings: <br>`exiftool IMG_NAME`
9. At the comment session, we can see: **/enc.zip** 
10. Seems to be a link to zip file. Let's try to download it and unzip it: `http://SERVER_IP_ADDRESS:8183/enc.zip`
11. The zip contains a python bytecode named **enc.pyc**
12. We need to uncompile it. We can do it with tools like uncompyle6 or with an online tool. Result: <br>
```
# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: ./tempdata/2fc6cc0e-1b27-40eb-8c45-d233c96af054.py
# Bytecode version: 3.6rc1 (3379)
# Source timestamp: 2025-11-01 19:13:27 UTC (1762024407)

DESC = 'C4N YOU 1D3N71FY 7H3 R3AL FL46?'
str0 = 'flag?:'
str1 = 'ZmxhZ'
str2 = '3tyM3'
str3 = 'YzNGx'
str4 = 'fdGgz'
str5 = 'X3MzY'
str6 = 'WxfaG'
str7 = 'lkZGV'
str8 = 'uX2lu'
str9 = 'X2J5d'
str10 = 'GVjb2'
str11 = 'RlXzl'
str12 = 'hNGMx'
str13 = 'byte'
str14 = 'code'
str15 = 'Mn0='
```
13. We have some indications: **REAL FLAG** and **flag?**. That means this might not be the flag we're looking for, or we have to do something extra.
14. Let's take a look at it: **ZmxhZ3tyM3YzNGxfdGgzX3MzYWxfaGlkZGVuX2luX2J5dGVjb2RlXzlhNGMxMn0=**
15. Looks like a bas64 format.
16. We decode it and we now get the real flag
17. Yay !!!

### Flag
`flag{r3v34l_th3_s3al_hidden_in_bytecode_9a4c12}`

## Deployment

### Local Testing
```bash
cd deploy
docker compose up -d
```

Access at: `http://localhost:8183`

### Stop the Challenge
```bash
docker compose down
```

## Files

- `src/index.html` - Home page
- `src/enc.zip` - Python bytecode to decompile
- `src/nsa_can.png` - Server side authentication checking
- `deploy/docker-compose.yml` - Docker deployment configuration

## Learning Objectives

- Recognize and decode common binary encodings
- Perform metadata forensics using tools like exiftool or strings
- Understand and reverse Python bytecode (e.g., with uncompyle6 or pycdc).