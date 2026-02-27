#include <stdio.h>
#include <stdlib.h>

int main()
{
    char sexo;
    int idade;
    float peso, altura;


    printf("digite seu sexo (f, F, m ou M), idade, peso e altura: \n");
    scanf("%c%d%f%f", &sexo, &idade, &peso, &altura);

    printf("\nsexo: %c\nIdade: %d\nPeso: %.1f\naltura: %.2f", sexo, idade, peso, altura);

    return 0;
}