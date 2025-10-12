#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

void win() {
    printf("Congratulations!\n");
    printf("Flag: flag{buff3r_0v3rfl0w_pwn3d}\n");
    fflush(stdout);
}

void vuln() {
    char buffer[64];
    printf("Enter your name: ");
    fflush(stdout);
    gets(buffer);  // Vulnerable function
    printf("Hello, %s!\n", buffer);
}

int main() {
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
    
    printf("Welcome to the pwn challenge!\n");
    printf("Can you find the vulnerability?\n");
    fflush(stdout);
    
    vuln();
    
    printf("Goodbye!\n");
    return 0;
}
