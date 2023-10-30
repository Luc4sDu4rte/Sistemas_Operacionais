import random

MATRIZ_SWAP = [[i, i+1, random.randint(1, 50), 0, 0, random.randint(100, 9999)] for i in range(100)]
MATRIZ_RAM = [MATRIZ_SWAP[random.randint(0, 99)].copy() for _ in range(10)]

indice_fifo = 0
indice_relogio = 0

def print_matriz(matriz):
    print("N\tI\tD\tR\tM\tT")
    for linha in matriz:
        print("\t".join(str(x) for x in linha))

# Função para executar uma instrução
def executa_instrucao(instrucao):
    global MATRIZ_RAM
    for pagina in MATRIZ_RAM:
        if pagina[1] == instrucao:
            pagina[3] = 1
            if random.random() < 0.3:
                pagina[2] += 1
                pagina[4] = 1
            return
    # Se a instrução não está na RAM, substitua uma página
    substitui_pagina(instrucao)

# ALGORITMOS DE SUBSTITUICAO

# NRU
def substitui_pagina_nru():
    global MATRIZ_RAM, MATRIZ_SWAP
    # Encontre a página com o menor valor de R e M
    min_r_m = min(pagina[3:5] for pagina in MATRIZ_RAM)
    for i in range(len(MATRIZ_RAM)):
        if MATRIZ_RAM[i][3:5] == min_r_m:
            # Substitua a página
            MATRIZ_SWAP[MATRIZ_RAM[i][0]] = MATRIZ_RAM[i]
            MATRIZ_RAM[i] = MATRIZ_SWAP[random.randint(0, 99)].copy()
            return

# FIFO
def substitui_pagina_fifo():
    global MATRIZ_RAM, MATRIZ_SWAP, indice_fifo
    # Substitua a página no índice atual do FIFO
    MATRIZ_SWAP[MATRIZ_RAM[indice_fifo][0]] = MATRIZ_RAM[indice_fifo]
    MATRIZ_RAM[indice_fifo] = MATRIZ_SWAP[random.randint(0, 99)].copy()
    # Atualize o índice do FIFO
    indice_fifo = (indice_fifo + 1) % len(MATRIZ_RAM)

# RELÓGIO (clock)
def substitui_pagina_relogio():
    global MATRIZ_RAM, MATRIZ_SWAP, indice_relogio
    # Encontre a próxima página com R = 0
    while True:
        if MATRIZ_RAM[indice_relogio][3] == 0:
            # Substitua a página
            MATRIZ_SWAP[MATRIZ_RAM[indice_relogio][0]] = MATRIZ_RAM[indice_relogio]
            MATRIZ_RAM[indice_relogio] = MATRIZ_SWAP[random.randint(0, 99)].copy()
            return
        # Caso contrário, defina R = 0 e avance o índice
        MATRIZ_RAM[indice_relogio][3] = 0
        indice_relogio = (indice_relogio + 1) % len(MATRIZ_RAM)

# FIFO-SC
def substitui_pagina_fifo_sc():
    global MATRIZ_RAM, MATRIZ_SWAP, indice_fifo
    while True:
        if MATRIZ_RAM[indice_fifo][3] == 0:
            # Substitua a página no índice atual do FIFO
            MATRIZ_SWAP[MATRIZ_RAM[indice_fifo][0]] = MATRIZ_RAM[indice_fifo]
            MATRIZ_RAM[indice_fifo] = MATRIZ_SWAP[random.randint(0, 99)].copy()
            indice_fifo = (indice_fifo + 1) % len(MATRIZ_RAM)
            return
        else:
            # Segunda chance à página e avance o índice
            MATRIZ_RAM[indice_fifo][3] = 0
            indice_fifo = (indice_fifo + 1) % len(MATRIZ_RAM)

# WS-CLOCK
def substitui_pagina_ws_clock():
    global MATRIZ_RAM, MATRIZ_SWAP, indice_relogio
    EP = random.randint(100, 9999) # Envelhecimento da página
    while True:
        if MATRIZ_RAM[indice_relogio][3] == 0 and EP > MATRIZ_RAM[indice_relogio][5]:
            # Substitua a página no índice atual do relógio se ela não estiver no conjunto de trabalho
            MATRIZ_SWAP[MATRIZ_RAM[indice_relogio][0]] = MATRIZ_RAM[indice_relogio]
            MATRIZ_RAM[indice_relogio] = MATRIZ_SWAP[random.randint(0, 99)].copy()
            return
        else:
            # Avance o índice do relógio e continue procurando uma página para substituir
            indice_relogio = (indice_relogio + 1) % len(MATRIZ_RAM)

# Função para substituir uma página
def substitui_pagina(instrucao):
    # Chamando o algoritmo de substituição
    substitui_pagina_fifo()
    

# Execução do simulador
print("Início da execução")
print_matriz(MATRIZ_RAM)
print_matriz(MATRIZ_SWAP)
for _ in range(1000):
    executa_instrucao(random.randint(1, 100))
print("Fim da execução")
print_matriz(MATRIZ_RAM)
print_matriz(MATRIZ_SWAP)
