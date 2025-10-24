##Alunos: Gustavo da Fonseca Roza 2211100074 & Henrique Ribeiro Rodrigues 2211100005 

.data
MSG_bemvindo:		        .string     "Bem vindo ao BlackJack!\n"
MSG_totalDeCartas: 	        .string     "Total de Cartas: "
MSG_pontuacao:		        .string     "\nPontuacao:\n"
MSG_dealer:		            .string     "   Dealer: "
MSG_jogador:		        .string     "   Jogador: "
MSG_desejaJogar:            .string     "Deseja jogar? (1 - Sim, 2 - Não): "
MSG_cartas_jogador:         .string     "\n\nO jogador recebe: "
MSG_dealerMostrarCartas:    .string     "O dealer revela: "
MSG_quebraLinha:            .string     "\n"
MSG_cartaOculta:            .string     " e uma carta oculta\n"
MSG_mao:                    .string     "Sua mao: "
MSG_igual:                  .string     " = "   
MSG_mais:                   .string     " + "
MSG_perguntarAcao:          .string     "O que voce deseja fazer? (1 - Hit, 2 - Stand): "
MSG_maoDoDealer:            .string     "O dealer revela sua mao: "
MSG_dealerRecebe:           .string     "O dealer recebe: "
MSG_dealerTem:              .string     "O dealer tem: "
MSG_dealerContinua:         .string     "O dealer deve continuar pedindo cartas...\n"
MSG_jogadorEstourou:        .string     "Você estourou! O dealer venceu!\n"
MSG_dealerEstourou:         .string     "O dealer estourou! Você venceu!\n"
MSG_jogadorGanhou:          .string     "Voce venceu com uma pontuacao maior!\n"
MSG_dealerGanhou:           .string     "O dealer venceu com uma pontuação maior!\n"
MSG_empate:                 .string     "Empate!\n"
MSG_baralhoResetado:        .string     "\n\nO baralho foi resetado e embaralhado!"



# Array para controlar quantas cartas de cada valor foram distribuídas (1-13)
#                             Ás, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K
contador_cartas:        .word    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

cartas_jogador:        .space 40        # Espaço para até 10 cartas
cartas_dealer:         .space 40        # Espaço para até 10 cartas

.text
.globl main 
main:
    # Inicializar pontuações
    li s0, 0       # Pontuação do dealer
    li s1, 0       # Pontuação do jogador
    li s2, 52      # Total de cartas no baralho

    # Exibir mensagem de boas-vindas
    la a0, MSG_bemvindo
    li a7, 4
    ecall   
    

breckJacquiLoop:
    la a0, MSG_totalDeCartas 
    li a7, 4
    ecall

    mv a0, s2
    li a7, 1
    ecall

    la a0, MSG_quebraLinha
    li a7, 4
    ecall

    # Exibe a pontuação antes de perguntar se deseja jogar
    jal exibePontuacao

    #pergunta se deseja jogar
    la a0, MSG_desejaJogar 
    li a7, 4
    ecall

    li a7, 5
    ecall

    li t0, 1 
    bne a0, t0, finaliza # Se não for 1, finaliza o jogo

    #reinicia o baralho
    li t0, 12
    bgt s2, t0, NaoResetaBaralho  # Se s2 > 12, não reseta o baralho
    li a7, 4
    la a0, MSG_baralhoResetado
    ecall

    # Reseta o baralho
    la t0, contador_cartas
    li t1, 0
    li t2, 13
    jal embaralha
    j NaoResetaBaralho 


# Função: exibePontuacao
# Exibe a pontuação atual do dealer e do jogador
# Usa s0 (dealer) e s1 (jogador)
# Não altera s0/s1

exibePontuacao:
    # Exibe "Pontuacao:\n"
    la a0, MSG_pontuacao
    li a7, 4
    ecall

    # Exibe "   Dealer: "
    la a0, MSG_dealer
    li a7, 4
    ecall

    # Exibe valor do dealer (s0)
    mv a0, s0
    li a7, 1
    ecall

    # Exibe quebra de linha
    la a0, MSG_quebraLinha
    li a7, 4
    ecall

    # Exibe "   Jogador: "
    la a0, MSG_jogador
    li a7, 4
    ecall

    # Exibe valor do jogador (s1)
    mv a0, s1
    li a7, 1
    ecall

    # Exibe quebra de linha
    la a0, MSG_quebraLinha
    li a7, 4
    ecall

    ret

embaralha:
    sw zero, 0(t0)              # Zera o contador de cartas
    addi t0, t0, 4              # Avança para o próximo contador
    addi t1, t1, 1              # Incrementa o contador de cartas
    blt t1, t2, embaralha 
    li s2, 52

NaoResetaBaralho:
    jal novaRodada              # Iniciar nova rodada
    j breckJacquiLoop           # Verificar se deseja jogar novamente

finaliza: 
    jal exibePontuacaoFinal
    li a7, 10
    ecall

novaRodada:
    # Salvar registradores na pilha
    addi sp, sp, -4
    sw ra, 0(sp)    

    # Inicializar contadores de cartas
    li s3, 0       # Número de cartas do jogador
    li s4, 0       # Número de cartas do dealer

    # Distribuir 2 cartas para o jogador
    jal distribuiCartaDealer
    la t0, cartas_jogador
    sb a0, 0(t0)
    addi s3, s3, 1
    addi s2, s2, -1

    jal distribuiCartaDealer
    la t0, cartas_jogador 
    sb a0, 1(t0)
    addi s3, s3, 1
    addi s2, s2, -1

    # Distribuir 2 cartas para o dealer
    jal distribuiCartaDealer
    la t0, cartas_dealer
    sb a0, 0(t0)
    addi s4, s4, 1
    addi s2, s2, -1
    
    jal distribuiCartaDealer
    la t0, cartas_dealer
    sb a0, 1(t0)
    addi s4, s4, 1
    addi s2, s2, -1
    
    # Mostrar cartas do jogador
    la a0, MSG_cartas_jogador
    li a7, 4
    ecall
    
    la t0, cartas_jogador
    lb a0, 0(t0)
    li a7, 1
    ecall
    
    la a0, MSG_mais
    li a7, 4
    ecall
    
    la t0, cartas_jogador
    lb a0, 1(t0)
    li a7, 1
    ecall
    
    la a0, MSG_quebraLinha
    li a7, 4
    ecall
    
    # Mostrar primeira carta do dealer
    la a0, MSG_dealerMostrarCartas
    li a7, 4
    ecall
    
    la t0, cartas_dealer
    lb a0, 0(t0)
    li a7, 1
    ecall
    
    la a0, MSG_cartaOculta
    li a7, 4
    ecall

    # Turno do jogador
    jal turnoJogador
    
    # Se o jogador não estourou, é a vez do dealer
    beqz a0, turnoDoDealer
    
    # Jogador estourou
    la a0, MSG_jogadorEstourou
    li a7, 4
    ecall
    
    # Incrementar pontuação do dealer
    addi s0, s0, 1
    j fimRodada
    
turnoDoDealer:
    # Mostrar mão do dealer
    la a0, MSG_maoDoDealer
    li a7, 4
    ecall
    
    la t0, cartas_dealer
    lb a0, 0(t0)
    li a7, 1
    ecall
    
    la a0, MSG_mais
    li a7, 4
    ecall
    
    la t0, cartas_dealer
    lb a0, 1(t0)
    li a7, 1
    ecall
    
    # Calcular valor da mão do dealer
    la a0, cartas_dealer
    mv a1, s4      # Usa o número real de cartas do dealer
    jal calcularMao
    mv s5, a0
    
    la a0, MSG_igual
    li a7, 4
    ecall
    
    mv a0, s5
    li a7, 1
    ecall
    
    la a0, MSG_quebraLinha
    li a7, 4
    ecall
    
    # Verificar se o dealer precisa pedir mais cartas
    li t0, 17
    bge s5, t0, comparaMao
    
    la a0, MSG_dealerContinua
    li a7, 4
    ecall   

dealerEstouraLoop:
    # Verificar se o dealer precisa pedir mais cartas
    li t0, 17
    bge s5, t0, comparaMao
    
    # Dealer pede mais uma carta
    jal distribuiCartaDealer
    la t0, cartas_dealer
    add t0, t0, s4
    sb a0, 0(t0)
    mv t1, a0 #aqui salva em um temporaio a carta que o dealer recebe, para podermos printar dps
    addi s4, s4, 1
    addi s2, s2, -1
    
    # Mostrar carta recebida
    la a0, MSG_dealerRecebe
    li a7, 4
    ecall
    
    mv a0, t1
    li a7, 1
    ecall
    
    la a0, MSG_quebraLinha
    li a7, 4
    ecall
    
    # Recalcular valor da mão do dealer
    la a0, cartas_dealer
    mv a1, s4
    jal calcularMao
    mv s5, a0
    
    # Mostrar mão atual do dealer
    la a0, MSG_dealerTem
    li a7, 4
    ecall
    
    # Mostrar todas as cartas do dealer
    la t0, cartas_dealer
    li t1, 0
    
dealerMostraCartas:
    lb a0, 0(t0)
    li a7, 1
    ecall
    
    addi t1, t1, 1
    beq t1, s4, fimExibicaoCartasDealer
    
    la a0, MSG_mais
    li a7, 4
    ecall
    
    addi t0, t0, 1
    j dealerMostraCartas
    
fimExibicaoCartasDealer:
    la a0, MSG_igual
    li a7, 4
    ecall
    
    mv a0, s5
    li a7, 1
    ecall
    
    la a0, MSG_quebraLinha
    li a7, 4
    ecall
    
    # Verificar se o dealer estourou
    li t0, 21
    ble s5, t0, dealerEstouraLoop
    
    # Dealer estourou
    la a0, MSG_dealerEstourou
    li a7, 4
    ecall
    
    # Incrementar pontuação do jogador
    addi s1, s1, 1
    j fimRodada
    
    

turnoJogador:
    # Salvar registradores na pilha
    addi sp, sp, -4
    sw ra, 0(sp)
    
turnoJogadorLoop:
    # Mostrar mão atual do jogador
    la a0, MSG_mao
    li a7, 4
    ecall
    
    # Mostrar todas as cartas do jogador
    la t0, cartas_jogador
    li t1, 0 


jogadorMostraCartas:
    lb a0, 0(t0)
    li a7, 1
    ecall
    
    addi t1, t1, 1
    beq t1, s3, fimExibicaoCartasJogador
    
    la a0, MSG_mais
    li a7, 4
    ecall
    
    addi t0, t0, 1
    j jogadorMostraCartas

    
fimExibicaoCartasJogador:
    # Calcular valor da mão do jogador
    la a0, cartas_jogador
    mv a1, s3
    jal calcularMao
    mv s6, a0  # Salvar valor da mão do jogador
    
    la a0, MSG_igual
    li a7, 4
    ecall
    
    mv a0, s6
    li a7, 1
    ecall
    
    la a0, MSG_quebraLinha
    li a7, 4
    ecall
    
    # Verificar se o jogador estourou
    li t0, 21
    bgt s6, t0, jogadorEstourou
    
    # Perguntar ação do jogador
    la a0, MSG_perguntarAcao
    li a7, 4
    ecall
    
    li a7, 5
    ecall
    
    li t0, 1
    bne a0, t0, jogadorStand
    
    # Jogador pede mais uma carta (Hit)
    jal distribuiCartaDealer
    la t0, cartas_jogador
    add t0, t0, s3
    sb a0, 0(t0)
    mv t1, a0 # salva a carta que o jogador recebe em t1 para poder printar dps (linha 453)
    addi s3, s3, 1
    addi s2, s2, -1
    
    # Mostrar carta recebida
    la a0, MSG_cartas_jogador
    li a7, 4
    ecall
    
    mv a0, t1
    li a7, 1
    ecall
    
    la a0, MSG_quebraLinha
    li a7, 4
    ecall
    
    j turnoJogadorLoop
    
jogadorStand:
    # Jogador para (Stand)
    li a0, 0  # Não estourou
    j turnoJogadorFim
    
jogadorEstourou:
    # Jogador estourou
    li a0, 1  # Estourou
    
turnoJogadorFim:
    # Restaurar registradores da pilha
    lw ra, 0(sp)
    addi sp, sp, 4
    ret

###############################################################################################################

# Função para calcular o valor da mão
# a0 = endereço do array de cartas
# a1 = número de cartas
# Retorna o valor da mão em a0

calcularMao:
    li t0, 0       # Contador
    li t1, 0       # Soma
    li t2, 0       # Número de Ases
    j LoopParaCalcularCarta    # Adicionado jump para o loop correto

# Função para comparar as mãos e determinar o vencedor
comparaMao:
    # Calcular valor da mão do jogador
    la a0, cartas_jogador
    mv a1, s3
    jal calcularMao
    mv s6, a0  # Salvar valor da mão do jogador
    
    # Comparar mãos
    bgt s6, s5, jogadorGanha
    bgt s5, s6, dealerGanha
    
    # Empate
    la a0, MSG_empate
    li a7, 4
    ecall 
    j fimRodada   

jogadorGanha:
    la a0, MSG_jogadorGanhou
    li a7, 4
    ecall
    addi s1, s1, 1
    j fimRodada

dealerGanha:
    la a0, MSG_dealerGanhou
    li a7, 4
    ecall
    addi s0, s0, 1
    j fimRodada

fimRodada:
    # Restaurar registradores da pilha
    lw ra, 0(sp)
    addi sp, sp, 4
    ret


LoopParaCalcularCarta:
    beq t0, a1, calculaAses
    
    lb t3, 0(a0)   # Carregar carta
    
    # Verificar valor da carta
    li t4, 1
    beq t3, t4, calculaAs
    
    li t4, 11      # Valete
    beq t3, t4, calculaNaipe
    
    li t4, 12      # Dama
    beq t3, t4, calculaNaipe
    
    li t4, 13      # Rei
    beq t3, t4, calculaNaipe
    
    # Carta numerada (2-10)
    add t1, t1, t3
    j calculaProxima
    
calculaAs:
    # Ás (contabilizado depois)
    addi t2, t2, 1
    j calculaProxima
    
calculaNaipe:
    # Figura (vale 10)
    addi t1, t1, 10
    
calculaProxima:
    addi a0, a0, 1
    addi t0, t0, 1
    j LoopParaCalcularCarta
    
calculaAses:
    # Processar Ases
    beqz t2, calculaFim
    
    # Para cada Ás, decidir se vale 1 ou 11
    li t0, 0
    
LoopCalculaAs:
    beq t0, t2, calculaFim
    
    # Verificar se adicionar 11 estoura
    addi t3, t1, 11
    li t4, 21
    bgt t3, t4, asValeUm
    
    # Ás vale 11
    addi t1, t1, 11
    j incrementaAses
    
asValeUm:
    # Ás vale 1
    addi t1, t1, 1
    
incrementaAses: 
    addi t0, t0, 1
    j LoopCalculaAs
    
calculaFim:
    mv a0, t1
    ret


distribuiCartaDealer:
    # Salvar registradores na pilha
    addi sp, sp, -4
    sw ra, 0(sp)
    
    # Gerar número aleatório entre 1 e 13
pescaCarta:
    li a7, 42      # Syscall para número aleatório
    li a1, 13      # Limite superior (exclusivo)
    ecall
    addi a0, a0, 1 # Ajustar para 1-13
    
    # Verificar se já foram distribuídas 4 cartas desse valor
    la t0, contador_cartas
    addi t0, t0, -4
    slli t1, a0, 2  # Multiplicar por 4 para obter o offset
    add t0, t0, t1
    lw t1, 0(t0)
    
    li t2, 4
    bge t1, t2, pescaCarta  # Se já distribuiu 4, tenta outro número
    
    # Incrementar contagem dessa carta
    addi t1, t1, 1
    sw t1, 0(t0)
    
    # Restaurar registradores da pilha
    lw ra, 0(sp)
    addi sp, sp, 4
    ret
    
exibePontuacaoFinal:
    la a0, MSG_pontuacao
    li a7, 4
    ecall

    la a0, MSG_dealer
    li a7, 4
    ecall

    mv a0, s0
    li a7, 1
    ecall

    la a0, MSG_quebraLinha
    li a7, 4
    ecall

    la a0, MSG_jogador
    li a7, 4
    ecall

    mv a0, s1
    li a7, 1
    ecall

    la a0, MSG_quebraLinha
    li a7, 4
    ecall

    beq s0, s1, empateFinal
    bgt s0, s1, dealerGanhouFinal
    bgt s1, s0, jogadorGanhouFinal

empateFinal:
    la a0, MSG_quebraLinha
    li a7, 4
    ecall
    
    la a0, MSG_empate
    li a7, 4
    ecall
    ret 

dealerGanhouFinal:
    la a0, MSG_quebraLinha
    li a7, 4
    ecall
    
    la a0, MSG_dealerGanhou
    li a7, 4
    ecall
    ret

jogadorGanhouFinal:
    la a0, MSG_quebraLinha
    li a7, 4
    ecall
	
    la a0, MSG_jogadorGanhou
    li a7, 4
    ecall
    ret
