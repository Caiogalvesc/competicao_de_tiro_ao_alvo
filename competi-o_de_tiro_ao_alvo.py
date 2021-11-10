qtePertic = qtePerticM = qtePerticF = atiradoresDeElite = distPior = qtePerticMqAcertou = somaDistMulheres = 0
distMelhor = 9999999999
nome = sexo = nomeMelhor = nomePior = sexoMelhor = sexoPior = ''

print(9 * '-=')
print(' ATIRADORES COPE')
print(9 * '-=')
print('UTILIZE "ADM" QUANDO NÃO HOUVER MAIS COMPETIDORES.')

while nome != 'ADM':

    nome = input('Digite o nome do atirador: ').strip().upper()
    if nome == 'ADM':
        break
    qtePertic = qtePertic + 1
    while sexo != 'M' or 'F':
        sexo = input('Qual o sexo dessa pessoa? (Use M ou F) ').strip().upper()
        if sexo == 'M':
            qtePerticM += 1
            break
        if sexo == 'F':
            qtePerticF += 1
            break
    distancia = float(input('Qual foi a distãncia(em centímetros) em relação ao alvo? '))
    if sexo == 'F':
        somaDistMulheres += distancia
    if distancia < distMelhor:
        distMelhor = distancia
        nomeMelhor = nome
        sexoMelhor = sexo
    if distancia > distPior:
        distPior = distancia
        nomePior = nome
        sexoPior = sexo
    if distancia < 1:
        atiradoresDeElite = atiradoresDeElite + 1
    if distancia == 0 and sexo == 'M':
        qtePerticMqAcertou += 1

print(f'\nO percentual de atiradores de elite foi de {atiradoresDeElite * 100 / qtePertic}%\n')

print(f'''Melhor atirador(a): 
Nome = {nomeMelhor}
Sexo = {sexoMelhor}
Distância = {distMelhor}\n''')

print(f'''Pior atirador(a): 
Nome = {nomePior}
Sexo = {sexoPior}
Distância = {distPior}\n''')

print(f'Ao todo {qtePerticMqAcertou} policiais do sexo masculino acertaram o alvo.\n')

print(f'A média da distância ao alvo obtida pelas atiradoras foi de {somaDistMulheres / qtePerticF}cm do alvo.')
