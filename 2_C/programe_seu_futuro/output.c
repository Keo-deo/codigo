#include <stdio.h>
#include <stdlib.h>

// caractere de escape para saltar uma linha --> \n

int main()
{
    //printf é uma funcao de saida
    printf("\n-----------------------------------------\n\n");
    printf("1 - logar   2 - cadastar  3 - imprimir\n");
    printf("\n-----------------------------------------\n");

    printf("\nvalor retornado :%d", printf("bom"));

    printf("\nPressione qualquer tecla para finalizar.");
    getchar();

    return 0;
}