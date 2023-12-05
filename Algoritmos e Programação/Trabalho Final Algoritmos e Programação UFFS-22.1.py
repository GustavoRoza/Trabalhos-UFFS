#Alunos:
#Gustavo da Fonseca Roza
#Lucas Hohn
l = []
d = []
print('Bem vindo ao NerdFlix! Estamos felizes em te ver por aqui!')
login = str(input('Coloque aqui o seu login: '))
l.append(login)

import time
datahr= time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())


filmes = ['Batman', 'Gente Grande', 'Até o Último Homem']
filmescod = ['101010', '121212', '131313']
filmesgeneros = ['Ação', 'Comédia', 'Guerra']
filmesdispo = ['False', 'True', 'True']
filmespreco = [18.60, 12.88, 19.99]

series = ['Supernatural', 'Teen Wolf', 'Game of Thrones']
seriescod = ['202020', '212121', '232323']
seriesgeneros = ['Terror', 'Ação', 'Ficção']
seriesdispo = ['True', 'False', 'True']
seriespreco = [30.50, 32.99, 55.50]

docs = ['Democracia em Vertigem', 'Terra Viva', 'O dilema da Redes']
docscod = ['303030', '313131', '323232']
docsgeneros = ['Política', 'Natureza', 'Docudrama']
docsdispo = ['True', 'True', 'True']
docspreco = [20.00, 18.60, 25.50]

################################# Cadastrar os produtos ################################
print('Deseja cadastrar um produto? (S/N)')
cadastro = str(input(': '))
if cadastro == 's' or cadastro == 'S':
    print('Vamos cadastrar produtos!')
    cadastramento = str(input('Que tipo de produto você deseja cadastrar?\n0- Filme...\n1- Série...\n2- Documentário...\n:'))
    if cadastramento == '0':
        a = int(input('Quantos Filmes deseja cadastrar?: '))
        for i in range(a):
            nome = str(input('Nome do Filme: '))
            code = str(input('Código, até 6 dígitos: '))
            generos = str(input('Gênero: '))
            dispo = str(input('Disponibilidade, True ou False: '))
            preco = float(input('Preço: '))
            filmes.append(nome)
            filmescod.append(code)
            filmesgeneros.append(generos)
            filmesdispo.append(dispo)
            filmespreco.append(preco)
            print('-'*30)

    if cadastramento == '1':
        a = int(input('Quantas Séries deseja cadastrar?: '))
        for i in range(a):
            nome = str(input('Nome da Série: '))
            code = str(input('Código, até 6 dígitos: '))
            generos = str(input('Gênero: '))
            dispo = str(input('Disponibilidade, True ou False: '))
            preco = float(input('Preço: '))
            series.append(nome)
            seriescod.append(code)
            seriesgeneros.append(generos)
            seriesdispo.append(dispo)
            seriespreco.append(preco)
            print('-' * 30)

    if cadastramento == '2':
        a = int(input('Quantos documentários deseja cadastrar?: '))
        for i in range(a):
            nome = str(input('Nome do documentário: '))
            code = str(input('Código, até 6 dígitos: '))
            generos = str(input('Gênero: '))
            dispo = str(input('Disponibilidade, True ou False: '))
            preco = float(input('Preço: '))
            docs.append(nome)
            docscod.append(code)
            docsgeneros.append(generos)
            docsdispo.append(dispo)
            docspreco.append(preco)
            print('-' * 30)
################################# Consultar produtos ################################
print('-'*30)
print('Deseja consultar um produto? Ok, vamos lá! Oque deseja consultar?\n0- Todos os produtos...\n1- Filmes...\n2- Séries...\n3- Documentários...')
consulta = int(input('Digite um número: '))
print('-' * 30)
if consulta == 0:
    print('Filmes e Seus respectivos códigos: ')
    print(*filmes, sep=", ")
    print(*filmescod, sep=', ')
    print('-' * 30)
    print('Séries e Seus respectivos códigos: ')
    print(*series, sep=', ')
    print(*seriescod, sep=', ')
    print('-' * 30)
    print('Documentários e Seus respectivos códigos: ')
    print(*docs, sep=', ')
    print(*docscod, sep=', ')
    print('-' * 30)
    print('Deseja consultar os dados de quantos produtos?')
    prod= int(input(':'))
    for i in range(prod):
        codigo = str(input('Qual o código?: '))
        if codigo in filmescod:
            codef = filmescod.index(codigo)
            print(f'Nome: {filmes[codef]}')
            print(f'Gênero: {filmesgeneros[codef]}')
            print(f'Preço: {filmespreco[codef]}')
            print(f'Disponibilidade: {filmesdispo[codef]}')
            print('-'*30)
        if codigo in seriescod:
            codef = seriescod.index(codigo)
            print(f'Nome: {series[codef]}')
            print(f'Gênero: {seriesgeneros[codef]}')
            print(f'Preço: {seriespreco[codef]}')
            print(f'Disponibilidade: {seriesdispo[codef]}')
            print('-' * 30)
        if codigo in docscod:
            codef = docscod.index(codigo)
            print(f'Nome: {docs[codef]}')
            print(f'Gênero: {docsgeneros[codef]}')
            print(f'Preço: {docspreco[codef]}')
            print(f'Disponível: {docsdispo[codef]}')
            print('-' * 30)

if consulta == 1:
    print('Filmes e Seus respectivos códigos: ')
    print(*filmes, sep=", ")
    print(*filmescod, sep=', ')
    print('Deseja consultar os dados de quantos filmes?')
    prod = int(input(':'))
    for i in range(prod):
        codigo = str(input('Qual o código?: '))
        codef = filmescod.index(codigo)
        print(f'Nome: {filmes[codef]}')
        print(f'Gênero: {filmesgeneros[codef]}')
        print(f'Preço: {filmespreco[codef]}')
        print(f'Disponibilidade: {filmesdispo[codef]}')
        print('-' * 30)

if consulta == 2:
    print('Séries e Seus respectivos códigos: ')
    print(*series, sep=', ')
    print(*seriescod, sep=', ')
    print('Deseja consultar os dados de quantas séries?')
    prod = int(input(':'))
    for i in range(prod):
        codigo = str(input('Qual o código?: '))
        codef = seriescod.index(codigo)
        print(f'Nome: {series[codef]}')
        print(f'Gênero: {seriesgeneros[codef]}')
        print(f'Preço: {seriespreco[codef]}')
        print(f'Disponibilidade: {seriesdispo[codef]}')
        print('-' * 30)

if consulta == 3:
    print('Documentários e Seus respectivos códigos: ')
    print(*docs, sep=', ')
    print(*docscod, sep=', ')
    print('Deseja consultar os dados de quantos documentários?')
    prod = int(input(':'))
    for i in range(prod):
        codigo = str(input('Qual o código?: '))
        codef = docscod.index(codigo)
        print(f'Nome: {docs[codef]}')
        print(f'Gênero: {docsgeneros[codef]}')
        print(f'Preço: {docspreco[codef]}')
        print(f'Disponível: {docsdispo[codef]}')
        print('-' * 30)

################################# Atualizar produtos ################################

print('-' * 30)
print('Deseja atualizar o cadastro de algum produto? (S/N)')
atualização = str(input(':'))
if atualização == 's' or atualização == 'S':
    print('Atualização cadastral de um produto!')
    quantidade= int(input('Quantos produtos você deseja atualizar o cadastro?: '))
    for i in range(quantidade):
        recadastramento = str(input('Digite aqui o código do produto que deseja Recadastras: '))
        if recadastramento in filmescod:
            codef = filmescod.index(recadastramento)
            print(f'Nome: {filmes[codef]}')
            print(f'Gênero: {filmesgeneros[codef]}')
            print(f'Preço: {filmespreco[codef]}')
            print(f'Disponibilidade: {filmesdispo[codef]}')
            print('-'*30)
            nome = str(input('Nome do Filme: '))
            code = str(input('Código, até 6 dígitos: '))
            generos = str(input('Gênero: '))
            dispo = str(input('Disponibilidade, True ou False: '))
            preco = float(input('Preço: '))
            filmes[codef] = nome
            filmescod[codef] = code
            filmesgeneros[codef] = generos
            filmesdispo[codef] = dispo
            filmespreco[codef] = preco


        if recadastramento in seriescod:
            codef = seriescod.index(recadastramento)
            print(f'Nome: {series[codef]}')
            print(f'Gênero: {seriesgeneros[codef]}')
            print(f'Preço: {seriespreco[codef]}')
            print(f'Disponibilidade: {seriesdispo[codef]}')
            print('-' * 30)
            nome = str(input('Nome da Série: '))
            code = str(input('Código, até 6 dígitos: '))
            generos = str(input('Gênero: '))
            dispo = str(input('Disponibilidade, True ou False: '))
            preco = float(input('Preço: '))
            series[codef] = nome
            seriescod[codef] = code
            seriesgeneros[codef] = generos
            seriesdispo[codef] = dispo
            seriespreco[codef] = preco

        if recadastramento in docscod:
            codef = docscod.index(recadastramento)
            print(f'Nome: {docs[codef]}')
            print(f'Gênero: {docsgeneros[codef]}')
            print(f'Preço: {docspreco[codef]}')
            print(f'Disponível: {docsdispo[codef]}')
            print('-' * 30)
            nome = str(input('Nome do documentário: '))
            code = str(input('Código, até 6 dígitos: '))
            generos = str(input('Gênero: '))
            dispo = str(input('Disponibilidade, True ou False: '))
            preco = float(input('Preço: '))
            docs[codef] = nome
            docscod[codef] = code
            docsgeneros[codef] = generos
            docsdispo[codef] = dispo
            docspreco[codef] = preco

################################# Registrando as compras! ################################
carrinhonomeFilme = []
carrinhopreçoFilme = []
carrinhonomeSerie = []
carrinhopreçoSerie = []
carrinhonomeDoc = []
carrinhopreçoDoc = []
print('-' * 30)
print('Depois de olhar todo nosso catálogo, vamos registrar sua compra!')
quantidade = int(input('Quantos produtos você deseja adicionar ao carrinho?: '))
for i in range(quantidade):
    registrando = str(input('Digite o código do seu produto desejado: '))
    if registrando in filmescod:
        codef = filmescod.index(registrando)
        carrinhonomeFilme.append(filmes[codef])
        carrinhopreçoFilme.append(filmespreco[codef])
    if registrando in seriescod:
        codef = seriescod.index(registrando)
        carrinhonomeSerie.append(series[codef])
        carrinhopreçoSerie.append(seriespreco[codef])
    if registrando in docscod:
        codef = docscod.index(registrando)
        carrinhonomeDoc.append(docs[codef])
        carrinhopreçoDoc.append(docspreco[codef])

print(f'Você adicionou ao carrinho {len(carrinhonomeFilme)} Filmes.\nSendo ele(s):')
print(*carrinhonomeFilme, sep=', ')
print(f'Você adicionou ao carrinho {len(carrinhonomeSerie)} Series.\nSendo ela(s):')
print(*carrinhonomeSerie, sep=', ')
print(f'Você adicionou ao carrinho {len(carrinhonomeDoc)} Documentários.\nSendo ele(s):')
print(*carrinhonomeDoc, sep=', ')

################################# Relatório de compras! ################################
print('-' * 60)
print('Lhe apresento o relatório de compras, com todos produtos selecionados, e alguns dados.')
print('compras no nome de: ')
print(*l, sep=', ')
print(f'Data e hora da compra: {datahr}')
print('-' * 30)
print(f'Você comprou {len(carrinhonomeFilme)} Filmes.\nSendo ele(s), e seus respectivos preços:')
print(*carrinhonomeFilme, sep=', ')
print(*carrinhopreçoFilme, sep=', ')
print('-' * 30)
print(f'Você comprou {len(carrinhonomeSerie)} Series.\nSendo ela(s) e seus respectivos preços:')
print(*carrinhonomeSerie, sep=', ')
print(*carrinhopreçoSerie, sep=', ')
print('-' * 30)
print(f'Você comprou {len(carrinhonomeDoc)} Documentários.\nSendo ele(s) e seus respectivos preços:')
print(*carrinhonomeDoc, sep=', ')
print(*carrinhopreçoDoc, sep=', ')

print('-'*30)
somadeitens = len(carrinhonomeSerie) + len(carrinhonomeFilme) + len(carrinhonomeDoc)
somadosprecos = sum(carrinhopreçoDoc) + sum(carrinhopreçoFilme) + sum(carrinhopreçoSerie)

print(f'Total de itens: {somadeitens}')
print(f'Total a pagar: {somadosprecos:.2f}')