#include <iostream>        
#include "AutomatoPilha.h"

using namespace std;

int main(void) {
    AutomatoPilha automato;
    
    cout << "Digite o DNA, para ser analisado: ";
    string entrada;
    cin >> entrada; 
    
    bool resultado = automato.processaString(entrada);

    if (resultado == true) {
        cout << "Eh um Acido Desoxirribonucleico valido" << endl; 
    } else {
        cout << "Nao eh um Acido Desoxirribonucleico valido" << endl; 
    }
}