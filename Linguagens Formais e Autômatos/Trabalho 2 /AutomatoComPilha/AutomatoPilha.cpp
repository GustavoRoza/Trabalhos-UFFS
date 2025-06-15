#include "AutomatoPilha.h" 
#include <iostream> 

// Construtor da Transicao
AutomatoPilha::Transicao::Transicao(int from, int to, char input, char pop, char push) 
    : estadoOrigem(from), estadoDestino(to), simboloEntrada(input), 
      simboloDesempilhado(pop), simboloEmpilhado(push) {}

// Construtor do AutomatoPilha
AutomatoPilha::AutomatoPilha() {
    estadoAtual = 0; 
    pilha.push('Z'); 
    inicializaTransicoes(); 

    cout << "Q = {q0, q1, q2, q3, q4, q5}; " << endl;
    cout << "Σ = {A, T, G, C, #}; " << endl;
    cout << "Γ = {A, T, Z}; " << endl;
    cout << "Δ = { " << endl;
    for (const auto& e : transicoes) {
        cout <<"(" << e.estadoOrigem << " -> " << e.estadoDestino << "): "
             << "(" << e.simboloEntrada << ", "
             <<  e.simboloDesempilhado << "; "
             <<  e.simboloEmpilhado << ")," << endl;
    };
    cout << "};" << endl;
    cout << "q0 = q0; " << endl;
    cout << "F = {q1}. " << endl;
    cout << endl; 

}


void AutomatoPilha::inicializaTransicoes() {
    // Transições do estado q0
    transicoes.push_back(Transicao(0, 0, 'T', 'A', '@')); // q0->q0: T,A;@
    transicoes.push_back(Transicao(0, 0, 'A', 'T', '@')); // q0->q0: A,T;@
    transicoes.push_back(Transicao(0, 0, 'G', '@', '@')); // q0->q0: G,@;@
    transicoes.push_back(Transicao(0, 0, 'C', '@', '@')); // q0->q0: C,@;@
    transicoes.push_back(Transicao(0, 3, 'A', 'Z', 'Z')); // q0->q3: A,Z;Z
    transicoes.push_back(Transicao(0, 2, 'A', 'A', 'A')); // q0->q2: A,A;A
    transicoes.push_back(Transicao(0, 5, 'T', 'Z', 'Z')); // q0->q5: T,Z;Z
    transicoes.push_back(Transicao(0, 4, 'T', 'T', 'T')); // q0->q4: T,T;T
    transicoes.push_back(Transicao(0, 1, '#', 'Z', '@')); // q0->q1: #,Z;@
    // Transições para q0
    transicoes.push_back(Transicao(3, 0, '@', '@', 'A')); // q3->q0: @,@;A
    transicoes.push_back(Transicao(2, 0, '@', '@', 'A')); // q2->q0: @,@;A
    transicoes.push_back(Transicao(5, 0, '@', '@', 'T')); // q5->q0: @,@;T
    transicoes.push_back(Transicao(4, 0, '@', '@', 'T')); // q4->q0: @,@;T
}

void AutomatoPilha::executaTransicoesEpsilon() {
    bool continuaExecutando = true; 
    
    while (continuaExecutando) {
        continuaExecutando = false; // Assume que nao tem mais transicoes epsilon
        
        char topoPilha = pilha.empty() ? 'Z' : pilha.top(); 
        
        for (const auto& trans : transicoes) {
            // Verifica se é transição epsilon do estado atual
            if (trans.estadoOrigem == estadoAtual && trans.simboloEntrada == '@') {
                
                bool podeExecutar = false; 
                
                // Verifica pilha
                if (trans.simboloDesempilhado == '@') {
                    podeExecutar = true; 
                } else if (trans.simboloDesempilhado == topoPilha) {
                    podeExecutar = true; 
                }
                

                if (podeExecutar) {
                    estadoAtual = trans.estadoDestino; 
                    
                    // remove da pilha (se nao for epsolon)
                    if (trans.simboloDesempilhado != '@' && !pilha.empty()) {
                        pilha.pop();
                    }
                    
                    // Adiciona simbolo na pilha (se nao for epsilon)
                    if (trans.simboloEmpilhado != '@') {
                        pilha.push(trans.simboloEmpilhado);
                    }
                    
                    continuaExecutando = true; // Continua procurando transições
                    break; // Sai do loop for para recomeçar busca
                }
            }
        }
    }
}

bool AutomatoPilha::executaTransicao(char inputChar) {
    executaTransicoesEpsilon(); 
    
    char topoPilha = pilha.top(); 
    
    // Procura transição válida para o caractere
    for (const auto& trans : transicoes) {
        if (trans.estadoOrigem == estadoAtual && trans.simboloEntrada == inputChar) {
            
            bool podeExecutar = false; // Flag para verificar condições
            
            // Verifica pilha
            if (trans.simboloDesempilhado == '@') {
                podeExecutar = true; 
            } else if (trans.simboloDesempilhado == topoPilha) {
                podeExecutar = true; 
            }
            
            if (podeExecutar) {
                estadoAtual = trans.estadoDestino; // Muda estado
                
                // Remove símbolo da pilha se nao for epsilon. 
                if (trans.simboloDesempilhado != '@' && trans.simboloDesempilhado != 'Z') {
                    if (!pilha.empty()) {
                        pilha.pop();
                    }
                }
                else if (trans.simboloDesempilhado == 'Z' && !pilha.empty() && pilha.top() == 'Z') {
                    pilha.pop();
                } 
                
                // Adiciona na pilha se for necessario 
                if (trans.simboloEmpilhado != '@') {
                    pilha.push(trans.simboloEmpilhado);
                }
                
                executaTransicoesEpsilon();
                return true; // transicao executata
            }
            
        }
    }
    
    return false; // Nenhuma transição valida encontrada, retorna falso e posteriormente rejeita a string.
}

bool AutomatoPilha::processaString(const string& inputStr) { 
    executaTransicoesEpsilon(); 

    // Processa cada caractere da string
    for (char c : inputStr) {
        if (!executaTransicao(c)) { // Se nao executar uma transicao valida, rejeita a string
            cout << "Estado final: " << estadoAtual << endl; 
            return false;
        }
    }

    executaTransicoesEpsilon(); 
    cout << "Estado final: " << estadoAtual << endl; 
    return (estadoAtual == 1); 
}
