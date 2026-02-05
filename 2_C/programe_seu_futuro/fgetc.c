#include <stdio.h>
#include <stdlib.h>

int main()
{
    char letra;

    printf("Digite um caracter: ");
    letra = fgetc(stdin);

    printf("caracter lido: %c\n", letra);

    return 0;
}