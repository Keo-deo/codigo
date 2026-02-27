#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a = 10;
    
    printf("\nDigite um valor qualquer: ");
    scanf("%d", &a);
    
    // operador ternario
    a < 0 ? printf("\n\nValor negativo!\n") : printf("\n\tValor positivo ou igual a zaro!\n");

    // if else
    if(a < 0)
    printf("\n\t Valor negativo! (if)\n");
    else
        printf("\n\tValor positivo ou igual a zero (if)");
        
    printf("\nContinuando programa...\n");


    return 0;
   }
/*
true == 1 | False == 0
 ==
 !=
 <
 >
 <=
 >=
 || --> OU
*/