#include <stdio.h>

int main(void){
    float hrs, sal, salfin, porc;
    printf("Valor da hora trabalhada: ");
    scanf("%f", &sal);
    printf("Horas Trabalhadas do Funcionário: ");
    scanf("%f", &hrs);


    salfin = sal * hrs;
    printf("Salário final: ");
    printf("%.2f\n", salfin);
    if(hrs >= 200){
        porc = salfin / 100;
        porc = porc * 5;
        salfin = salfin + porc;
        printf("Salário final com bônus de 5%: ");
        printf("%.2f\n", salfin);
    }
}

