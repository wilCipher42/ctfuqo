#!/bin/bash
# Setup script for Linux commands challenge

# Create user
useradd -m -s /bin/bash ctf
echo "ctf:welcome123" | chpasswd

# Create flag in a hidden location
mkdir -p /opt/.secret
echo "flag{l1nux_c0mm4nds_4r3_p0w3rful}" > /opt/.secret/.flag.txt
chmod 644 /opt/.secret/.flag.txt

# Add some decoy files
echo "This is not the flag" > /home/ctf/readme.txt
mkdir -p /home/ctf/.config
echo "Still not the flag" > /home/ctf/.config/notes.txt

# Create a hint file
echo "The flag is somewhere in /opt..." > /home/ctf/hint.txt

echo "Setup complete!"
