import random
import time

class Processo:
    def __init__(self, pid, tempo_execucao):
        self.pid = pid
        self.tempo_execucao_total = tempo_execucao
        self.tempo_executado = 0
        self.cp = 0
        self.estado = "PRONTO"
        self.nes = 0
        self.n_cpu = 0

    def executar(self):
        # Verifica se o processo está bloqueado e decide se ele sai do estado de bloqueio.
        if self.estado == "BLOQUEADO":
            if random.random() < 0.3:
                self.estado = "PRONTO"
                print(f"Processo {self.pid} saiu do estado BLOQUEADO para PRONTO.")

        # Se o processo não está bloqueado, executa o quantum.
        if self.estado != "BLOQUEADO":
            self.n_cpu += 1
            self.tempo_executado += 1
            self.cp += 1

            # Verifica se o processo realiza uma operação de E/S.
            if random.random() < 0.05:
                self.estado = "BLOQUEADO"
                self.nes += 1
                print(f"Processo {self.pid} realizou uma operação de E/S e entrou no estado BLOQUEADO.")
            elif self.cp >= 1000:
                self.estado = "PRONTO"
                self.cp = 0
                print(f"Processo {self.pid} encerrou seu quantum e voltou para o estado PRONTO.")

            # Verifica se o processo terminou sua execução.
            if self.tempo_executado >= self.tempo_execucao_total:
                self.estado = "TERMINADO"
                print(f"Processo {self.pid} terminou sua execução.")

class TabelaDeProcessos:
    def __init__(self):
        self.processos = []

    def adicionar_processo(self, processo):
        self.processos.append(processo)

    def trocar_contexto(self, processo_atual):
        processo_atual.estado = "PRONTO"
        processo_atual.cp = 0
        print(f"Processo {processo_atual.pid} trocou de contexto: EXECUTANDO >>> PRONTO.")

        with open(f"processo_{processo_atual.pid}_dados.txt", "a") as arquivo:
            arquivo.write(f"PID: {processo_atual.pid}\n")
            arquivo.write(f"Tempo Executado: {processo_atual.tempo_executado}\n")
            arquivo.write(f"CP: {processo_atual.cp}\n")
            arquivo.write(f"Estado: {processo_atual.estado}\n")
            arquivo.write(f"Número de E/S: {processo_atual.nes}\n")
            arquivo.write(f"Número de vezes que usou a CPU: {processo_atual.n_cpu}\n")
            arquivo.write("\n")

    def executar_processos(self):
        while any(processo.estado != "TERMINADO" for processo in self.processos):
            for processo in self.processos:
                if processo.estado == "PRONTO":
                    print(f"Processo {processo.pid} entrou no estado EXECUTANDO.")
                    processo.estado = "EXECUTANDO"
                    processo.cp = 0

                processo.executar()

                if processo.estado == "PRONTO":
                    self.trocar_contexto(processo)

if __name__ == "__main__":
    tabela_processos = TabelaDeProcessos()

    # Criar e adicionar os processos à tabela.
    tempos_execucao = [10000, 5000, 7000, 3000, 3000, 8000, 2000, 5000, 4000, 10000]
    for pid, tempo_execucao in enumerate(tempos_execucao):
        processo = Processo(pid, tempo_execucao)
        tabela_processos.adicionar_processo(processo)

    # Executar os processos até que todos terminem.
    tabela_processos.executar_processos()
