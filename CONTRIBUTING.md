# Contributing to CTF UQO

Thank you for your interest in contributing to CTF UQO! This document provides guidelines for creating high-quality CTF challenges.

## 🎯 Challenge Creation Guidelines

### Challenge Quality

Every challenge should:

1. **Be Educational**: Teach a specific technique, vulnerability, or concept
2. **Be Fair**: Solvable with documented tools and reasonable effort
3. **Be Original**: Not a direct copy from other CTFs (references are okay with attribution)
4. **Be Tested**: Thoroughly tested before submission
5. **Be Well-Documented**: Include clear description and complete solution

### Challenge Difficulty Levels

- **Easy (100-150 pts)**: Introductory concepts, minimal steps, basic tools
- **Medium (200-300 pts)**: Intermediate techniques, multiple steps, common tools
- **Hard (350-500 pts)**: Advanced concepts, complex exploitation, custom tools

### Flag Format

All flags must follow this format:
```
flag{lowercase_with_underscores_or_numbers}
```

Examples:
- ✅ `flag{sql_injection_ftw}`
- ✅ `flag{buff3r_0v3rfl0w}`
- ❌ `FLAG{UPPERCASE}` (incorrect)
- ❌ `ctf{different_prefix}` (incorrect)

## 📝 Required Documentation

### Challenge README.md

Every challenge must include a complete README.md with:

1. **Metadata**
   - Category
   - Difficulty
   - Points
   - Author

2. **Description**
   - Clear problem statement
   - Connection information
   - Any provided files

3. **Solution**
   - Step-by-step walkthrough
   - Commands and code snippets
   - Explanation of the vulnerability/technique
   - The flag

4. **Deployment**
   - How to build/deploy locally
   - How to test
   - Production deployment notes

5. **Learning Objectives**
   - What participants will learn
   - Related concepts

## 🐳 Docker Requirements

### Dockerfile Best Practices

```dockerfile
# Use specific version tags, not 'latest'
FROM ubuntu:20.04

# Minimize layers
RUN apt-get update && apt-get install -y \
    package1 \
    package2 \
    && rm -rf /var/lib/apt/lists/*

# Run as non-root user when possible
RUN useradd -m ctfuser
USER ctfuser

# Expose only necessary ports
EXPOSE 8080

# Use exec form for CMD
CMD ["./app"]
```

### docker-compose.yml Template

```yaml
version: '3.8'

services:
  challenge:
    build:
      context: ..
      dockerfile: deploy/Dockerfile
    ports:
      - "PORT:PORT"  # Use uncommon ports to avoid conflicts
    restart: unless-stopped
    # Resource limits
    mem_limit: 512m
    cpus: 0.5
    # Environment variables
    environment:
      - FLAG=flag{your_flag_here}
    # Security options
    security_opt:
      - no-new-privileges:true
    cap_drop:
      - ALL
    cap_add:
      - NET_BIND_SERVICE  # Only if needed
```

## 🔒 Security Considerations

### What to Avoid

- **Container Escapes**: Ensure proper isolation
- **Resource Exhaustion**: Set memory/CPU limits
- **Unintended Solutions**: Test thoroughly
- **Real Credentials**: Never commit real passwords or keys
- **Privilege Escalation**: Unless it's the intended challenge

### What to Include

- **Proper Sandboxing**: Use Docker security features
- **Input Validation**: Even if it's vulnerable, validate unexpected inputs
- **Resource Limits**: Prevent DoS attacks
- **Logging**: Help with debugging and monitoring

## 📋 Pull Request Process

### Before Submitting

1. **Test locally**
   ```bash
   cd category/challenge-name/deploy
   docker-compose up -d
   # Test the challenge
   # Verify flag is obtainable
   docker-compose down
   ```

2. **Review checklist**
   - [ ] Challenge deploys successfully
   - [ ] Flag is obtainable via documented solution
   - [ ] No unintended solutions
   - [ ] README is complete
   - [ ] Solution is documented
   - [ ] No sensitive data committed
   - [ ] Docker images build successfully
   - [ ] Resource limits are set

3. **Clean up**
   - Remove debug code
   - Remove test files
   - Ensure .gitignore is working

### Submitting

1. **Create a feature branch**
   ```bash
   git checkout -b feature/web-new-challenge
   ```

2. **Commit with clear messages**
   ```bash
   git add category/challenge-name/
   git commit -m "feat(web): add XSS challenge with CSP bypass"
   ```

3. **Push to your fork**
   ```bash
   git push origin feature/web-new-challenge
   ```

4. **Create Pull Request**
   - Use descriptive title
   - Fill in the PR template
   - Link any related issues
   - Request review from maintainers

### PR Review Process

Maintainers will review:
- Challenge quality and originality
- Documentation completeness
- Security considerations
- Code quality
- Testing thoroughness

You may be asked to:
- Adjust difficulty/points
- Improve documentation
- Fix security issues
- Add/modify tests

## 🎨 Code Style

### Python
```python
# Use type hints
def encrypt(plaintext: str, key: int) -> str:
    pass

# Document functions
def solve_challenge(target: str) -> str:
    """
    Solve the challenge by exploiting the vulnerability.
    
    Args:
        target: URL or connection string
        
    Returns:
        The captured flag
    """
    pass
```

### Shell Scripts
```bash
#!/bin/bash
# Brief description of the script

set -e  # Exit on error
set -u  # Error on undefined variables

# Use functions
deploy_challenge() {
    echo "[*] Deploying challenge..."
    docker-compose up -d
}

# Call main function
main() {
    deploy_challenge
}

main "$@"
```

### C/C++
```c
// Clear comments
// Intentional vulnerability marker
// VULN: Buffer overflow in gets()
void vulnerable_function() {
    char buffer[64];
    gets(buffer);  // Dangerous!
}
```

## 📚 Challenge Categories

### Web Exploitation
- SQL Injection
- Cross-Site Scripting (XSS)
- Cross-Site Request Forgery (CSRF)
- Server-Side Request Forgery (SSRF)
- Authentication/Authorization bypasses
- File upload vulnerabilities
- Path traversal
- Command injection

### Binary Exploitation (Pwn)
- Buffer overflows
- Format string vulnerabilities
- Return-oriented programming (ROP)
- Heap exploitation
- Use-after-free
- Integer overflows

### Cryptography
- Classical ciphers
- RSA challenges
- AES/DES
- Hash functions
- Random number generators
- Known-plaintext attacks

### Reverse Engineering
- Binary analysis
- Decompilation
- Debugging techniques
- Obfuscation/packing
- Anti-debugging
- Code analysis

### Forensics
- Steganography
- File carving
- Memory forensics
- Network packet analysis
- Disk imaging
- Log analysis

### Miscellaneous
- OSINT
- Scripting/automation
- Programming challenges
- Linux system administration
- Trivia/research

## ❓ Questions?

- Open an issue for general questions
- Use discussions for ideas and brainstorming
- Contact maintainers directly for sensitive matters

## 🙏 Thank You!

Your contributions make this CTF better for everyone. We appreciate your time and effort in creating educational and engaging challenges!
