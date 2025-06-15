#ifndef AUTOMATOPILHA_H  
#define AUTOMATOPILHA_H  

#include <stack> 
#include <string>
#include <vector> 

using namespace std;

class AutomatoPilha {
private:
    stack<char> pilha;  
    int estadoAtual;    
    
    // Estrutura que define uma transicao
    struct Transicao {
        int estadoOrigem;   
        int estadoDestino;  
        char simboloEntrada;   
        char simboloDesempilhado;    
        char simboloEmpilhado;    
        
        // Construtor da transicao
        Transicao(int from, int to, char input, char pop, char push);
    };
    
    vector<Transicao> transicoes; 
    

    void executaTransicoesEpsilon(); 
    bool executaTransicao(char inputChar);
    void inicializaTransicoes();

public:
    AutomatoPilha();
    bool processaString(const string& inputStr);

};

#endif 