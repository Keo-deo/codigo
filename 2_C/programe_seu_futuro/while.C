#include <stdio.h>
#include <stdlib.h>

int main()
{
    char l1 = 'o', l2 = 'i';
    int contador = 0;
    while (contador <=10)
    {
        printf("%c", l1);
        printf("%c", l2);
        printf("\n");

        contador = contador+1;
        }
    return 0;
}