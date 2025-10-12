# CTF UQO - Challenge Repository

This repository contains all the challenges for the CTF UQO (Capture The Flag) competition, organized by category.

## 📁 Repository Structure

```
ctfuqo/
├── web/                    # Web exploitation challenges
├── pwn/                    # Binary exploitation challenges
├── crypto/                 # Cryptography challenges
├── reverse/                # Reverse engineering challenges
├── forensics/              # Digital forensics challenges
├── misc/                   # Miscellaneous challenges
├── CHALLENGE_TEMPLATE.md   # Template for creating new challenges
└── README.md              # This file
```

Each challenge follows this structure:
```
challenge-name/
├── README.md              # Challenge description and solution
├── src/                   # Source code and challenge files
├── solution/              # Solution scripts and writeups
└── deploy/                # Docker deployment configuration
    ├── Dockerfile
    └── docker-compose.yml
```

## 🚀 Getting Started

### Prerequisites

- **Docker** and **Docker Compose** (V2 recommended, V1 also supported) for running challenges
- **Git** for version control
- **Python 3** (for many challenges and scripts)
- **GCC** (for pwn/reverse challenges)

### Setting Up Your Development Environment

1. **Fork the repository**
   ```bash
   # Go to GitHub and click "Fork" on the main repository
   ```

2. **Clone your fork**
   ```bash
   git clone https://github.com/YOUR_USERNAME/ctfuqo.git
   cd ctfuqo
   ```

3. **Add upstream remote**
   ```bash
   git remote add upstream https://github.com/AverageGoldenRetrieverEnjoyer/ctfuqo.git
   ```

4. **Keep your fork synchronized**
   ```bash
   git fetch upstream
   git checkout main
   git merge upstream/main
   ```

## 🛠️ Creating a New Challenge

### Step 1: Create Challenge Branch

```bash
# Create and checkout a new branch for your challenge
git checkout -b feature/web-xss-challenge
```

### Step 2: Choose Category and Create Directory

```bash
# Create your challenge directory
mkdir -p web/my-challenge/{src,solution,deploy}
```

### Step 3: Use the Template

```bash
# Copy the template
cp CHALLENGE_TEMPLATE.md web/my-challenge/README.md
# Edit the README with your challenge details
```

### Step 4: Develop Your Challenge

Create the necessary files:

- **Source code** in `src/`
- **Solution scripts** in `solution/`
- **Docker deployment** in `deploy/`

Example `deploy/docker-compose.yml`:
```yaml
version: '3.8'

services:
  challenge:
    build:
      context: ..
      dockerfile: deploy/Dockerfile
    ports:
      - "PORT:PORT"
    restart: unless-stopped
    environment:
      - FLAG=flag{your_flag_here}
```

### Step 5: Test Your Challenge

```bash
cd web/my-challenge/deploy
docker-compose up -d

# Test the challenge
# ... verify flag is obtainable ...

# Clean up
docker-compose down
```

### Step 6: Document Everything

Ensure your `README.md` includes:
- Clear description
- Complete solution writeup
- Deployment instructions
- Learning objectives

### Step 7: Commit and Push

```bash
git add web/my-challenge/
git commit -m "Add web XSS challenge"
git push origin feature/web-xss-challenge
```

### Step 8: Create Pull Request

1. Go to GitHub
2. Click "New Pull Request"
3. Select your branch
4. Fill in the PR template
5. Request review from maintainers

## 📋 Development Workflow Best Practices

### Branching Strategy

- **main**: Production-ready challenges only
- **feature/[category]-[challenge-name]**: New challenges
- **fix/[category]-[challenge-name]**: Bug fixes
- **docs/[what]**: Documentation updates

### Commit Messages

Follow conventional commits format:
```
feat(web): add SQL injection challenge
fix(pwn): correct buffer overflow offset
docs(crypto): update RSA challenge solution
chore(misc): update docker-compose version
```

### Code Review Checklist

Before submitting a PR, ensure:
- [ ] Challenge deploys successfully with `docker-compose up`
- [ ] Flag is obtainable following the solution steps
- [ ] No unintended solutions exist
- [ ] README is complete with all sections filled
- [ ] Solution is properly documented
- [ ] No sensitive information (passwords, API keys) committed
- [ ] Docker images are properly configured
- [ ] Challenge difficulty is appropriate

## 🐳 Docker Commands Reference

### Basic Commands

**Note**: Use `docker compose` (Docker Compose V2) or `docker-compose` (V1) based on your installation.

```bash
# Build and start a challenge
docker compose up -d

# View logs
docker compose logs -f

# Stop a challenge
docker compose down

# Rebuild after changes
docker compose up -d --build

# Remove all containers and volumes
docker compose down -v
```

### Managing Multiple Challenges

```bash
# Start all challenges in a category
for dir in web/*/deploy; do
  (cd "$dir" && docker compose up -d)
done

# Stop all challenges
for dir in web/*/deploy; do
  (cd "$dir" && docker compose down)
done
```

### Cleaning Up

```bash
# Remove unused Docker resources
docker system prune -a

# Remove all stopped containers
docker container prune

# Remove all unused images
docker image prune -a
```

## 🧪 Testing Challenges

### Local Testing

1. **Deploy the challenge**
   ```bash
   cd category/challenge-name/deploy
   docker-compose up -d
   ```

2. **Verify accessibility**
   ```bash
   # For web challenges
   curl http://localhost:PORT
   
   # For network services
   nc localhost PORT
   ```

3. **Run the solution**
   ```bash
   cd ../solution
   python exploit.py
   ```

4. **Verify the flag**
   - Ensure the flag matches the expected format
   - Confirm no unintended solutions exist

### Automated Testing

Create a `test.sh` script in your challenge directory:
```bash
#!/bin/bash
set -e

echo "[*] Starting challenge..."
docker-compose up -d

echo "[*] Waiting for service..."
sleep 5

echo "[*] Running solution..."
cd ../solution
python exploit.py | grep -q "flag{"

echo "[+] Test passed!"

cd ../deploy
docker-compose down
```

## 🔒 Security Guidelines

### Flag Format

- Use format: `flag{descriptive_text_here}`
- Make flags unique per challenge
- Avoid using offensive language
- Keep flags between 20-50 characters

### Sensitive Information

**Never commit:**
- Private keys (unless intentionally part of challenge)
- Real credentials
- Production secrets
- Personal information

Use environment variables for deployment:
```yaml
environment:
  - FLAG=${FLAG:-flag{default_flag_for_testing}}
```

### Challenge Security

- Ensure challenges are properly sandboxed
- Limit resource usage (CPU, memory, disk)
- Prevent container escapes
- Validate all user input
- Avoid privilege escalation vulnerabilities (unless intended)

## 📚 Resources

### CTF Challenge Creation

- [CTFd Documentation](https://docs.ctfd.io/)
- [CTF Field Guide](https://trailofbits.github.io/ctf/)
- [Awesome CTF](https://github.com/apsdehal/awesome-ctf)

### Docker & Containerization

- [Docker Documentation](https://docs.docker.com/)
- [Docker Compose Reference](https://docs.docker.com/compose/)
- [Docker Security Best Practices](https://docs.docker.com/develop/security-best-practices/)

### Challenge Categories

- **Web**: OWASP Top 10, Web Security Academy
- **Pwn**: CTF Wiki, Pwn College
- **Crypto**: CryptoHack, Cryptopals
- **Reverse**: Crackmes.one, Reverse Engineering for Beginners
- **Forensics**: Digital Forensics Discord, ForensicsWiki
- **Misc**: Various Linux/scripting resources

## 🤝 Contributing

We welcome contributions! To contribute:

1. Fork the repository
2. Create a feature branch
3. Develop your challenge following the guidelines
4. Test thoroughly
5. Submit a pull request

### Quality Standards

Challenges should be:
- **Educational**: Teach a specific concept or technique
- **Fair**: Solvable with reasonable effort and skill
- **Original**: Not copied from other CTFs (unless properly attributed)
- **Well-documented**: Clear description and complete solution
- **Tested**: Verified to work as intended

## 📞 Support

- **Issues**: Report bugs or problems with challenges
- **Discussions**: Ask questions or discuss ideas
- **Discord**: [Join our community](#) (if available)

## 📜 License

This repository is for educational purposes. Individual challenges may have their own licenses.

## 🎯 Challenge Categories Overview

### Web Exploitation
SQL injection, XSS, CSRF, authentication bypasses, server-side vulnerabilities

### Binary Exploitation (Pwn)
Buffer overflows, format string vulnerabilities, ROP, heap exploitation

### Cryptography
Classical ciphers, modern cryptography, hash functions, RSA, AES

### Reverse Engineering
Binary analysis, decompilation, debugging, obfuscation, anti-reversing

### Forensics
Steganography, file carving, memory forensics, network analysis, disk imaging

### Miscellaneous
OSINT, scripting, Linux commands, programming challenges, trivia

---

**Happy Hacking! 🚩**
