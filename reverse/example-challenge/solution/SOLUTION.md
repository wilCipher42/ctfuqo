# Solution for Reverse Engineering Challenge

## Method 1: Using strings

```bash
strings challenge | grep flag
# Output: flag{r3v3rs3_3ng1n33r1ng_fun}
```

## Method 2: Using strings to find password

```bash
strings challenge | grep -i "password\|secret"
# Look for: sup3r_s3cr3t_p4ssw0rd
```

Then run the program:
```bash
./challenge
# Enter: sup3r_s3cr3t_p4ssw0rd
```

## Method 3: Using Ghidra/IDA

1. Open the binary in Ghidra
2. Analyze the main function
3. Look for the `check_password` function
4. Find the hardcoded password comparison
5. Find the `print_flag` function that contains the flag

## Method 4: Using ltrace/strace

```bash
ltrace ./challenge
# Enter any password and observe the strcmp comparison
# The correct password will be visible in the trace
```
