# Example Web Challenge - Authentication Bypass

**Category:** web  
**Difficulty:** meduim  
**Points:** 100  
**Author:** CTF Team

## Description

Can you bypass the login page and get the flag?

Connect to the challenge at: `http://SERVER_IP_ADDRESS:8180`

## Solution

### Overview
This challenge demonstrates a classic bruteforcing application in a vulnerable login page with tools like Hydra.

### Steps
1. Navigate to the home page
2. Check the page source and notice at the end the brainfck langage message
3. Decode the message to get the hint. Which basically suggest you to use cewl tool
4. Generate your wordlist from the home page with cewl: `cewl -d 2 -m 3 http://SERVER_IP_ADDRESS:8081 -w wordlist.txt`
5. Open the new generated wordlist and make sure you have multiple words to use.
6. Then navigate to the login page. This is the page we need to bruteforce to get access
7. Use Hydra for this purpose: 
`hydra -V -s 8180 -L wordlist.txt_PATH -P wordlists.txt_PATH SERVER_IP_ADDRESS http-post-form "/check-auth.php:username=^USER^&password=^PASS^:F=Username ou Mot de passe incorrect. Essayez encore"`
8. Wait a few minutes till he gets valid credentials. Should be : 
```
- tom/piscing
- jerry/parturient
```
9. Login with tom. There is another hint: `Pauvre Tom, toujours à courrir derrière Jerry. Peut-être qu'il devrait su jerry pour tous les tracas causés lol`
10. Login with jerry and get the flag. That's it ! The flag will be displayed after successful bypass

### Flag
`flag{login_success_jerry}`

## Deployment

### Local Testing
```bash
cd deploy
docker compose up -d
```

Access at: `http://localhost:8180`

### Stop the Challenge
```bash
docker compose down
```

## Files

- `src/index.php` - Home page
- `src/login.php` - Vulnerable login page to bruteforce
- `src/check-auth.php` - Server side authentication checking
- `src/tom.php` - Tom home page
- `src/jerry.php` - Jerry home page with the flag
- `src/style1.css` - Css style of the pages
- `solution/exploit.py` - Automated exploit script
- `deploy/docker-compose.yaml` - Docker deployment configuration
- `deploy/Dockerfile` - Container image definition

## Learning Objectives

- Understanding how a bruteforce works
- Getting familiar with some penTesting tools such as Hydra and cewl
