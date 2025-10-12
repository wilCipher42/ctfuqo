# Example Web Challenge - SQL Injection Login

**Category:** web  
**Difficulty:** easy  
**Points:** 100  
**Author:** CTF Team

## Description

Can you bypass the login page and get the admin's flag?

Connect to the challenge at: `http://challenge.ctf:PORT`

## Solution

### Overview
This challenge demonstrates a classic SQL injection vulnerability in a login form.

### Steps
1. Navigate to the login page
2. Try basic SQL injection payloads in the username field:
   ```
   admin' OR '1'='1
   ```
3. Leave the password field empty or enter any value
4. The flag will be displayed after successful bypass

### Flag
`flag{sql_1nj3ct10n_1s_d4ng3r0us}`

## Deployment

### Local Testing
```bash
cd deploy
docker compose up -d
```

Access at: `http://localhost:8080`

### Stop the Challenge
```bash
docker compose down
```

## Files

- `src/app.py` - Vulnerable Flask application
- `src/templates/` - HTML templates
- `solution/exploit.py` - Automated exploit script
- `deploy/docker-compose.yml` - Docker deployment configuration
- `deploy/Dockerfile` - Container image definition

## Learning Objectives

- Understanding SQL injection vulnerabilities
- Recognizing insecure database queries
- Learning proper input validation and parameterized queries
