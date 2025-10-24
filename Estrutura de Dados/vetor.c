#include "vetor.h"

Vet2dim atribuiPosition(int a, int b) {
  Vet2dim v;
  v.position1 = a;
  v.position2 = b;
  return v;
}
void imprimeVetor(Vet2dim vetor) {
  printf("posição 1: %d\n", vetor.position1);
  printf("posição 2: %d\n", vetor.position2);
}
Vet2dim somaVetor(Vet2dim vet1, Vet2dim vet2) {
  Vet2dim result;
  result.position1 = vet1.position1 + vet2.position1;
  result.position2 = vet1.position2 + vet2.position2;
  return result;
}
Vet2dim subtraiVetor(Vet2dim vet1, Vet2dim vet2) {
  Vet2dim result;
  result.position1 = vet1.position1 - vet2.position1;
  result.position2 = vet1.position2 - vet2.position2;
  return result;
}
double moduloVetorial(Vet2dim vet) {
  double modulo;
  modulo = pow(
      (vet.position1 * vet.position1) + (vet.position2 * vet.position2), 0.5);
  return modulo;
}
double produtoInterno(Vet2dim vet) {
  double prodinter;
  prodinter =
      ((vet.position1 * vet.position1) + (vet.position2 * vet.position2));
  return prodinter;
}