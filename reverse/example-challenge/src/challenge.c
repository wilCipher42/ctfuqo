#include <stdio.h>
#include <string.h>

int check_password(char *input) {
    char correct[] = "sup3r_s3cr3t_p4ssw0rd";
    return strcmp(input, correct) == 0;
}

void print_flag() {
    printf("Congratulations! Here's your flag:\n");
    printf("flag{r3v3rs3_3ng1n33r1ng_fun}\n");
}

int main() {
    char input[100];
    
    printf("===============================\n");
    printf("   Secret Password Checker\n");
    printf("===============================\n");
    printf("Enter the password: ");
    
    if (fgets(input, sizeof(input), stdin) != NULL) {
        // Remove newline
        input[strcspn(input, "\n")] = 0;
        
        if (check_password(input)) {
            print_flag();
        } else {
            printf("Wrong password!\n");
        }
    }
    
    return 0;
}
