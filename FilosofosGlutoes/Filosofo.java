import java.util.concurrent.Semaphore;
import java.util.concurrent.locks.ReentrantLock;
/*
 * classe que fornece um mecanismo de sinalização para controlar o acesso a recursos compartilhados e ReentrantLock 
 * é uma classe que implementa um bloqueio reentrante.
 */

public class Filosofo extends Thread { // Esta linha define a classe Filosofo que estende a classe Thread, permitindo que cada filósofo seja executado em sua própria thread.
    private final Semaphore semaphore; // Limita o numero de filosofos que podem comer ao mesmo tempo
    private final ReentrantLock leftFork; // Garfo esquerda
    private final ReentrantLock rightFork; // Garfo direita

    public Filosofo(Semaphore semaphore, ReentrantLock leftFork, ReentrantLock rightFork) { // Construtor que inicializa os campos com os valores passados como argumentos
        this.semaphore = semaphore;
        this.leftFork = leftFork;
        this.rightFork = rightFork;
    }

    @Override
    public void run() { // Chamado quando a thread inicializa, define o "ciclo de vida do Filosofo" 
        try {
            while (true) {
                pensar();
                semaphore.acquire();
                comer();
                semaphore.release();
            }
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        } // Vao pensar, tentam comer se ter garfos disponiveis e liberam garfos quando terminam de comer
    }

    private void pensar() throws InterruptedException { // Chamado quando o Filosofo esta pensando
        System.out.println(Thread.currentThread().getName() + " pensando"); // Imprime a mensagem 
        Thread.sleep((long) (Math.random() * 1000)); // Faz a thread dormir por um tempo aleatorio
    }

    private void comer() throws InterruptedException { // Chamado quando o Filosofo esta comendo
        if (leftFork.tryLock()) { // Tenta pegar os bloqueios dos garfos
            try {
                if (rightFork.tryLock()) { // Se conseguir bloqueio ele imprime a mensagem e faz a thread dormir
                    try {
                        System.out.println(Thread.currentThread().getName() + " está comendo");
                        Thread.sleep((long) (Math.random() * 1000));
                    } finally { // Depois do tempo libera o bloqueio dos garfos
                        rightFork.unlock();
                    }
                }
            } finally {
                leftFork.unlock();
            }
        }
    }
    
    public static void main(String[] args) { // Inicializa as threads criando um semaforo com numero de permissoes
        int numFilosofos = 5;
        Semaphore semaphore = new Semaphore(numFilosofos  - 1); // Numero de permissoes do semaforo
        ReentrantLock[] forks = new ReentrantLock[numFilosofos ]; // Array para representar os garfos 
        for (int i = 0; i < numFilosofos ; i++) { // Cada Filosofo inicia com sua propria thread
            forks[i] = new ReentrantLock();
        }
        for (int i = 0; i < numFilosofos ; i++) {   
            new Filosofo(semaphore, forks[i], forks[(i + 1) % numFilosofos]).start();
        }
    }
}
