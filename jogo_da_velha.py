import random

# Função que cria um tabuleiro de jogo da velha
def criar_tabuleiro():
    return [["-","-","-"],["-","-","-"],["-","-","-"]]

# Função que valida se um jogador ganhou
def verificar_vitoria(jogador, tabuleiro):
    # Verificar linhas
    for lin in range(3):
        if tabuleiro[lin][0] == tabuleiro[lin][1] == tabuleiro[lin][2] == jogador:
            return True
    # Verificar colunas
    for col in range(3):
        if tabuleiro[0][col] == tabuleiro[1][col] == tabuleiro[2][col] == jogador:
            return True
    # Verificar diagonais
    if (tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador) or (tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador):
        return True
    return False

# Função que realiza uma jogada aleatória
def jogada_aleatoria(jogador, tabuleiro):
    # Encontrar posições vazias no tabuleiro
    posicoes_vazias = []
    for lin in range(3):
        for col in range(3):
            if tabuleiro[lin][col] == "-":
                posicoes_vazias.append((lin,col))
    # Selecionar jogada aleatória
    jogada = random.choice(posicoes_vazias)
    tabuleiro[jogada[0]][jogada[1]] = jogador
    return jogada

# Função que implementa o SMA*
def jogada_SMA_estrela(jogador, tabuleiro, jogador_oponente):
    pontuacao_maior = -float("inf")
    melhor_jogada = None
    # Percorrer todas as posições vazias
    for lin in range(3):
        for col in range(3):
            if tabuleiro[lin][col] == "-":
                # Copiar o tabuleiro e realizar a jogada
                tabuleiro_copia = [list(linha) for linha in tabuleiro]
                tabuleiro_copia[lin][col] = jogador
                # Verificar se há vitória
                if verificar_vitoria(jogador, tabuleiro_copia):
                    return (lin,col)
                # Verificar se há derrota
                if verificar_vitoria(jogador_oponente, tabuleiro_copia):
                    pontuacao = -1
                else:
                    # Realizar chamada recursiva
                    pontuacao = -jogada_SMA_estrela(jogador_oponente, tabuleiro_copia, jogador)[1]
                # Selecionar a melhor jogada
                if pontuacao > pontuacao_maior:
                    pontuacao_maior = pontuacao
                    melhor_jogada = (lin,col)
    return melhor_jogada, pontuacao_maior

# Função que implementa o IDS*
def jogada_IDS_estrela(jogador, tabuleiro, jogador_oponente):
    # Definir limite de profundidade
    limite_profundidade = 0
    # Definir melhor jogada e melhor pontuação
    melhor_jogada = None
    pontuacao_maior = -float("inf")
    # Enquanto não for encontrada uma jogada
    while melhor_jogada == None:
        # Aumentar o limite de profundidade
        limite_profundidade += 1
        # Realizar chamada recursiva
        melhor_jogada, pontuacao_maior = jogada_IDS_estrela_aux(jogador, tabuleiro, jogador_oponente, limite_profundidade)
    return melhor_jogada

# Função auxiliar para o IDS*
def jogada_IDS_estrela_aux(jogador, tabuleiro, jogador_oponente, limite_profundidade):
    # Verificar se já foi atingido o limite de profundidade
    if limite_profundidade == 0:
        return None, 0
    # Percorrer todas as posições vazias
    pontuacao_maior = -float("inf")
    melhor_jogada = None
    for lin in range(3):
        for col in range(3):
            if tabuleiro[lin][col] == "-":
                # Copiar o tabuleiro e realizar a jogada
                tabuleiro_copia = [list(linha) for linha in tabuleiro]
                tabuleiro_copia[lin][col] = jogador
                # Verificar se há vitória
                if verificar_vitoria(jogador, tabuleiro_copia):
                    return (lin,col), 1
                # Verificar se há derrota
                if verificar_vitoria(jogador_oponente, tabuleiro_copia):
                    pontuacao = -1
                else:
                    # Realizar chamada recursiva
                    pontuacao = -jogada_IDS_estrela_aux(jogador_oponente, tabuleiro_copia, jogador, limite_profundidade-1)[1]
                # Selecionar a melhor jogada
                if pontuacao > pontuacao_maior:
                    pontuacao_maior = pontuacao
                    melhor_jogada = (lin,col)
    return melhor_jogada, pontuacao_maior

# Função que simula duas jogadas
def simular_jogadas(jogador, jogada_funcao):
    # Definir jogador oponente
    if jogador == "X":
        jogador_oponente = "O"
    else:
        jogador_oponente = "X"
    # Criar tabuleiro
    tabuleiro = criar_tabuleiro()
    # Realizar jogadas alternadas
    vez_jogador = True
    while True:
        if vez_jogador:
            jogada = jogada_funcao(jogador, tabuleiro, jogador_oponente)
        else:
            jogada = jogada_aleatoria(jogador_oponente, tabuleiro)
            tabuleiro[jogada[0]] [jogada[1]] = jogador if vez_jogador else jogador_oponente
        # Verificar se há vitória
        if verificar_vitoria(jogador if vez_jogador else jogador_oponente, tabuleiro):
            return jogador if vez_jogador else jogador_oponente
        # Verificar se há empate
        if not any("-" in linha for linha in tabuleiro):
            return "empate"
        # Alternar jogador
        vez_jogador = not vez_jogador

# Definir jogador
jogador = "X"
# Realizar simulações
num_simulacoes = 1000
vitorias = 0
derrotas = 0
empates = 0
for _ in range(num_simulacoes):
    resultado = simular_jogadas(jogador, jogada_SMA_estrela)
    if resultado == jogador:
        vitorias += 1
    elif resultado == "empate":
        empates += 1
    else:
        derrotas += 1
# Mostrar resultados
print("Vitórias: {} ({:.2f}%)".format(vitorias, 100*vitorias/num_simulacoes))
print("Derrotas: {} ({:.2f}%)".format(derrotas, 100*derrotas/num_simulacoes))
print("Empates: {} ({:.2f}%)".format(empates, 100*empates/num_simulacoes))
