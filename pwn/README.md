# Binary Exploitation (Pwn) Challenges

This directory contains binary exploitation challenges focusing on vulnerabilities in compiled programs.

## Common Challenge Types

- **Buffer Overflow**: Overwriting memory to control execution
- **Format String Vulnerabilities**: Exploiting printf-style functions
- **Return-Oriented Programming (ROP)**: Code reuse attacks
- **Heap Exploitation**: Use-after-free, double-free, heap overflow
- **Integer Overflow**: Exploiting integer arithmetic vulnerabilities
- **Stack Canaries Bypass**: Defeating stack protection
- **ASLR/PIE Bypass**: Defeating address randomization
- **Shellcode Injection**: Injecting and executing machine code

## Tools & Resources

- **pwntools**: Python library for exploit development
- **GDB**: GNU Debugger with pwndbg/gef/peda
- **ROPgadget**: Finding ROP gadgets
- **checksec**: Check binary security properties
- **radare2**: Reverse engineering framework
- **objdump**: Display binary information

## Getting Started

Most challenges require:
- Basic understanding of assembly (x86/x64)
- C programming knowledge
- Linux command-line familiarity
- Debugging skills

Browse the subdirectories to find challenges!
