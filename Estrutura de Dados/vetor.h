typedef struct {
  int position1; // Primeira posição
  int position2; // Segunda posição
} Vet2dim;

Vet2dim atribuiPosition();
void imprimeVetor(Vet2dim vetor);
Vet2dim somaVetor(Vet2dim vet1, Vet2dim vet2);
Vet2dim subtraiVetor(Vet2dim vet1, Vet2dim vet2);
double moduloVetorial(Vet2dim vet);
double produtoInterno(Vet2dim vet);