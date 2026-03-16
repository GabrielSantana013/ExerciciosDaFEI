/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package lab05;

/**
 *
 * @author unifgdias
 */
public class Main {
    public static void main(String[] args) throws InterruptedException{
        
        //EXERCICIO 1 e 2 
        
//        ExemploThread ext = new ExemploThread("Ola", 1000);
//        ExemploThread ext2 = new ExemploThread("Bem-vindo", 2000);
//        Thread t1 = new Thread(ext);
//        Thread t2 = new Thread(ext2);
//
//        System.out.println("Iniciando a Thread");
//        
//        t1.start(); //inicia a thread
//        t2.start(); //inicia a thread
//        t1.join(); //espera a thread iniciar a execução  
//        t2.join(); //espera a thread iniciar a execução        
//        System.out.println("Finalizando a Thread");

        //EXERCICIO 3 e 4
        
//        int[] vetor = {1,2,3,4,5,6,7,8,9,10};
//        
//        System.out.println("Inicio Thread");
//        
//        ExemploThread ext = new ExemploThread(vetor,0,4);
//        ExemploThread ext2 = new ExemploThread(vetor,5,9);
//        Thread t1 = new Thread(ext);
//        Thread t2 = new Thread(ext2);
//        
//        long inicio = System.nanoTime();
//        
//        t1.start(); //inicia a thread
//        t2.start(); //inicia a thread
//        t1.join(); //espera a thread iniciar a execução  
//        t2.join(); //espera a thread iniciar a execução                
//        System.out.println("Soma = " + (ext.sum + ext2.sum));
//
//        long fim = System.nanoTime();
//        long duracao = fim - inicio;
//        
//        System.out.println("Tempo de execucão em ms: " + duracao);

          //EXERCICIO 5

        int[][] vetor = new int[2][10];
        
        for(int i = 0; i < 2; i++){
            for(int j = 0; j < 10; j++){
                vetor[i][j] = j+i;
            }
        }
        
        System.out.println("Inicio Thread");
        
        ExemploThread ext = new ExemploThread(vetor,0,0,5);
        ExemploThread ext2 = new ExemploThread(vetor,0,5,9);
        ExemploThread ext3 = new ExemploThread(vetor,1,0,5);
        ExemploThread ext4 = new ExemploThread(vetor,1,5,9);
        Thread t1 = new Thread(ext);
        Thread t2 = new Thread(ext2);
        Thread t3 = new Thread(ext3);
        Thread t4 = new Thread(ext4);
        
        long inicio = System.nanoTime();
        
        t1.start(); //inicia a thread
        t2.start(); //inicia a thread
        t3.start(); //inicia a thread
        t4.start(); //inicia a thread
        t1.join(); //espera a thread iniciar a execução  
        t2.join(); //espera a thread iniciar a execução                
        t3.join(); //espera a thread iniciar a execução                
        t4.join(); //espera a thread iniciar a execução                
        System.out.println("Soma = " + (ext.sum + ext2.sum + ext3.sum + ext4.sum));

        long fim = System.nanoTime();
        long duracao = fim - inicio;
        
        System.out.println("Tempo de execucão em ms: " + duracao);          
          
        
    }    
}
