# Quick Start Guide

This guide will help you get started with creating and testing CTF challenges for CTF UQO.

## 🎯 For Challenge Creators

### 1. Setup Your Environment

```bash
# Fork the repository on GitHub
# Clone your fork
git clone https://github.com/YOUR_USERNAME/ctfuqo.git
cd ctfuqo

# Add upstream remote
git remote add upstream https://github.com/AverageGoldenRetrieverEnjoyer/ctfuqo.git
```

### 2. Create a New Challenge

```bash
# Create a new branch
git checkout -b feature/web-my-challenge

# Create challenge directory structure
mkdir -p web/my-challenge/{src,solution,deploy}

# Copy the template
cp CHALLENGE_TEMPLATE.md web/my-challenge/README.md
```

### 3. Develop Your Challenge

Edit the files in your challenge directory:

- `README.md` - Challenge description, solution, and documentation
- `src/` - Your challenge source code
- `solution/` - Solution scripts and exploit code
- `deploy/Dockerfile` - Container configuration
- `deploy/docker-compose.yml` - Deployment configuration

### 4. Test Locally

```bash
cd web/my-challenge/deploy

# Build and start the challenge
docker compose up -d

# Check logs
docker compose logs -f

# Test your solution
cd ../solution
python exploit.py

# Stop the challenge
cd ../deploy
docker compose down
```

### 5. Submit Your Challenge

```bash
# Stage your files
git add web/my-challenge/

# Commit with a clear message
git commit -m "feat(web): add SQL injection challenge"

# Push to your fork
git push origin feature/web-my-challenge

# Create a Pull Request on GitHub
```

## 🧪 For Testers

### Test a Challenge

```bash
# Navigate to challenge directory
cd category/challenge-name/deploy

# Start the challenge
docker compose up -d

# View the challenge port
docker compose ps

# Access the challenge (adjust port as needed)
curl http://localhost:PORT
# or
nc localhost PORT

# Stop when done
docker compose down
```

### Test Multiple Challenges

```bash
# Start all challenges in a category
for dir in web/*/deploy; do
  echo "Starting challenge in $dir"
  (cd "$dir" && docker compose up -d)
done

# Stop all
for dir in web/*/deploy; do
  (cd "$dir" && docker compose down)
done
```

## 📚 Common Commands

### Git Workflow

```bash
# Update your fork
git fetch upstream
git checkout main
git merge upstream/main
git push origin main

# Create feature branch
git checkout -b feature/category-challenge-name

# Check status
git status

# View changes
git diff

# Commit changes
git add .
git commit -m "descriptive message"

# Push to your fork
git push origin feature/category-challenge-name
```

### Docker Commands

```bash
# Build and start
docker compose up -d

# Build with no cache
docker compose build --no-cache

# View logs
docker compose logs -f

# Stop services
docker compose down

# Stop and remove volumes
docker compose down -v

# List running containers
docker compose ps

# Execute command in container
docker compose exec service-name bash
```

## 🎓 Challenge Categories

Choose the right category for your challenge:

- **web/** - Web application vulnerabilities
- **pwn/** - Binary exploitation
- **crypto/** - Cryptography and encryption
- **reverse/** - Reverse engineering
- **forensics/** - Digital forensics and steganography
- **misc/** - Everything else (OSINT, scripting, etc.)

## 📖 Resources

- **Main README**: Full documentation and best practices
- **CHALLENGE_TEMPLATE.md**: Template for new challenges
- **CONTRIBUTING.md**: Detailed contribution guidelines
- **Category README**: Specific info for each category

## 💡 Tips

1. **Start Simple**: Begin with easier challenges before complex ones
2. **Test Thoroughly**: Make sure your challenge works and has no unintended solutions
3. **Document Well**: Write clear descriptions and complete solutions
4. **Security First**: Ensure challenges are properly sandboxed
5. **Be Creative**: Make challenges engaging and educational

## ❓ Getting Help

- Read the documentation in README.md and CONTRIBUTING.md
- Check existing examples in each category
- Open an issue for questions
- Ask maintainers for guidance

## 🚀 Next Steps

1. Browse existing challenges in different categories
2. Read the CONTRIBUTING.md for detailed guidelines
3. Review example challenges to understand the structure
4. Start creating your own challenge!

---

**Ready to create your first challenge? Start with the template and follow the examples!**
