import random #usa a tabela_processos.txt

class Processo:
    def __init__(self, PID, TP):
        self.PID = PID
        self.TP = TP
        self.CP = 0
        self.EP = "PRONTO"
        self.NES = 0
        self.N_CPU = 0

    def executar(self):
        quantum = 1000
        while self.CP < self.TP:
            if random.random() < 0.05:  # 5% de chance de E/S
                self.EP = "BLOQUEADO"
                self.NES += 1
                break
            self.CP += 1
            self.N_CPU += 1
            if self.CP == self.TP:
                self.EP = "TERMINADO"
                break
            if self.N_CPU == quantum:
                self.EP = "PRONTO"
                break

    def salvar_estado(self):
        with open("tabela_processos.txt", "a") as arquivo:
            arquivo.write(f"PID: {self.PID}, TP: {self.TP}, CP: {self.CP}, EP: {self.EP}, NES: {self.NES}, N_CPU: {self.N_CPU}\n")

def main():
    processos = [Processo(PID, TP) for PID, TP in enumerate([10000, 5000, 7000, 3000, 3000, 8000, 2000, 5000, 4000, 10000])]

    while any(processo.EP != "TERMINADO" for processo in processos):
        for processo in processos:
            if processo.EP == "PRONTO":
                processo.EP = "EXECUTANDO"
                processo.executar()
                processo.salvar_estado()
                if processo.EP != "TERMINADO":
                    processo.EP = "PRONTO"

if __name__ == "__main__":
    main()
