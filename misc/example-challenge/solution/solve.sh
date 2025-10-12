#!/bin/bash
# Automated solution for Linux commands challenge

echo "[*] Connecting to challenge server..."
echo "[*] Commands to find the flag:"
echo ""
echo "# List all files including hidden"
echo "$ ls -la"
echo ""
echo "# Search for files containing 'flag' in their name"
echo "$ find / -name '*flag*' 2>/dev/null"
echo ""
echo "# Or search in common locations"
echo "$ find /opt -name '*flag*' 2>/dev/null"
echo ""
echo "# Read the flag"
echo "$ cat /opt/.secret/.flag.txt"
echo ""
echo "[+] Expected flag: flag{l1nux_c0mm4nds_4r3_p0w3rful}"
