#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int myAtoi(char *s);

int main() {
    char *s = malloc(256);
    printf("Enter your atoi input: ");
    scanf("%255s", s);

    int atoiNum = myAtoi(s);
    free(s);
    printf("%d is your atoi number\n", atoiNum);
    return 0;
}

int myAtoi(char *s) {

    int sum = 0;
    int currDigit;
    for (int i = strlen(s) - 1, magnitude = 1; i >= 0 ; --i, magnitude *= 10) {
        sum += (s[i] - '0') * magnitude;
    }
    printf("%d\n", sum);

    return sum;
}
