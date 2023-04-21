#include "vetor.h"
#include <stdio.h>

int main(void) {
  Vet2dim vetor, vetor2, resulSoma, resulSubtra;
  double modulo, prodinter;
  vetor = atribuiPosition(2, 3);
  vetor2 = atribuiPosition(4, 3);
  printf("Imprindo vetor: \n");
  imprimeVetor(vetor);
  printf("\n");
  printf("Somando os vetores: \n");
  resulSoma = somaVetor(vetor, vetor2);
  imprimeVetor(resulSoma);
  printf("\n");
  printf("Subtraindo vetores: \n");
  resulSubtra = subtraiVetor(vetor, vetor2);
  imprimeVetor(resulSubtra);
  printf("\n");
  printf("Módulo: ");
  modulo = moduloVetorial(vetor);
  printf("%.2lf\n", modulo);
  printf("\n");
  printf("Produto interno: ");
  prodinter = produtoInterno(vetor);
  printf("%.2lf\n", prodinter);
}