palavras_chave = ['se', 'senao', 'enquanto', 'para', 'retorne']

def e_operador_aritmetico(char):
    return char in '+-*/'

def e_delimitador(char):
    return char in ';{}()'

def e_letra(char):
    return char.isalpha()

def e_digito(char):
    return char.isdigit()

def analisador_lexico_simples(codigo_fonte):
    linha_atual = 1
    posicao_atual = 0
    tokens_encontrados = []
    erros_encontrados = []
    codigo_fonte = codigo_fonte.strip()

    while posicao_atual < len(codigo_fonte):
        char_atual = codigo_fonte[posicao_atual]

        # Ignorar espaços em branco e contar linhas
        if char_atual.isspace():
            if char_atual == '\n':
                linha_atual += 1
            posicao_atual += 1
            continue

        # Identificação de palavras (identificadores ou palavras-chave)
        if e_letra(char_atual):
            inicio = posicao_atual
            while posicao_atual < len(codigo_fonte) and (
                    e_letra(codigo_fonte[posicao_atual]) or e_digito(codigo_fonte[posicao_atual])):
                posicao_atual += 1
            palavra = codigo_fonte[inicio:posicao_atual]
            if palavra in palavras_chave:
                tokens_encontrados.append(('PALAVRA_CHAVE', palavra, linha_atual))
            else:
                tokens_encontrados.append(('IDENTIFICADOR', palavra, linha_atual))
            continue

        # Identificação de números inteiros
        if e_digito(char_atual):
            inicio = posicao_atual
            posicao_atual += 1

            # Caso seja seguido de letras, é um identificador inválido
            if posicao_atual < len(codigo_fonte) and e_letra(codigo_fonte[posicao_atual]):
                while posicao_atual < len(codigo_fonte) and (
                        e_letra(codigo_fonte[posicao_atual]) or e_digito(codigo_fonte[posicao_atual])):
                    posicao_atual += 1
                palavra = codigo_fonte[inicio:posicao_atual]
                erros_encontrados.append(
                    f"Erro léxico: '{palavra}' é um identificador inválido na linha {linha_atual}")
                tokens_encontrados.append(('ERRO', char_atual, linha_atual))
            else:
                # Se não for seguido de letras, é um número inteiro
                while posicao_atual < len(codigo_fonte) and e_digito(codigo_fonte[posicao_atual]):
                    posicao_atual += 1
                numero = codigo_fonte[inicio:posicao_atual]
                tokens_encontrados.append(('NUMERO_INTEIRO', numero, linha_atual))
            continue

        # Tratamento de comentários "//"
        if char_atual == '/' and posicao_atual + 1 < len(codigo_fonte) and codigo_fonte[posicao_atual + 1] == '/':
            while posicao_atual < len(codigo_fonte) and codigo_fonte[posicao_atual] != '\n':
                posicao_atual += 1
            continue

        # Operadores aritméticos
        if e_operador_aritmetico(char_atual):
            tokens_encontrados.append(('OPERADOR_ARITMETICO', char_atual, linha_atual))
            posicao_atual += 1
            continue

        # Delimitadores
        if e_delimitador(char_atual):
            tokens_encontrados.append(('DELIMITADOR', char_atual, linha_atual))
            posicao_atual += 1
            continue

        # Operadores de atribuição e relacionais
        if char_atual == '=':
            if posicao_atual + 2 < len(codigo_fonte) and codigo_fonte[posicao_atual + 1] == '=' and codigo_fonte[
                posicao_atual + 2] == '=':
                erros_encontrados.append(f"Erro léxico: '===' não reconhecido na linha {linha_atual}")
                tokens_encontrados.append(('ERRO', char_atual, linha_atual))
                posicao_atual += 3
            elif posicao_atual + 1 < len(codigo_fonte) and codigo_fonte[posicao_atual + 1] == '=':
                tokens_encontrados.append(('OPERADOR_RELACIONAL', '==', linha_atual))
                posicao_atual += 2
            else:
                tokens_encontrados.append(('OPERADOR_ATRIBUICAO', '=', linha_atual))
                posicao_atual += 1
            continue

        # Caracter não reconhecido (erro)
        erros_encontrados.append(f"Erro léxico: '{char_atual}' não reconhecido na linha {linha_atual}")
        tokens_encontrados.append(('ERRO', char_atual, linha_atual))
        posicao_atual += 1

    tokens_encontrados.append(('FIM', '$', linha_atual))
    return tokens_encontrados, erros_encontrados

def criar_teste_funcionalidade(tokens):
    fita = []
    for token in tokens:
        fita.append(f"{token[0]}({token[1]}) linha {token[2]}")  # Adiciona cada token formatado na fita
    return fita

def criar_fita_saída(tokens):
    fita = []
    for token in tokens:
        if token[0] == 'PALAVRA_CHAVE':
            fita.append('P')
        elif token[0] == 'IDENTIFICADOR':
            fita.append('I')
        elif token[0] == 'OPERADOR_RELACIONAL':
            fita.append('O')
        elif token[0] == 'DELIMITADOR':
            fita.append(token[1])
        elif token[0] == 'OPERADOR_ATRIBUICAO':
            fita.append('A')
        elif token[0] == 'OPERADOR_ARITMETICO':
            fita.append('opa')
        elif token[0] == 'ERRO':
            fita.append('E')
        elif token[0] == 'NUMERO_INTEIRO':  # Corrigido de NUMEROS_INTEIRO
            fita.append('N')
        elif token[0] == 'FIM':
            fita.append('$')
    return fita

# Exemplo de código fonte
codigo = '''
se (x === 10) {
  1y = 5;
  1z = 1y +- 3; | 
  x = 10 + 90
  // Isto é um comentário s
}
'''

# Analisando o código e gerando a fita de saída
tokens, erros = analisador_lexico_simples(codigo)
testes = criar_teste_funcionalidade(tokens)
fita = criar_fita_saída(tokens)
fita_como_string = ''.join(fita)

print("Verificação de funcionalidade\n")
for posicao, conteudo in enumerate(testes):
    print(conteudo)

print(codigo)

print("\nFita de saída")
print(fita_como_string)

# Exibindo erros
if erros:
    print("\nErros Léxicos Encontrados:\n")
    for erro in erros:
        print(erro)
else:
    print("\nNenhum erro léxico encontrado.")
