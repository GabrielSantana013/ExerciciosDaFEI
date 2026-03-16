/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package lab05;

/**
 *
 * @author unifgdias
 */
public class ExemploThread implements Runnable{


    //EXERCÍCIO 1 e 2
//    public String mensagem;
//    public int delay;
//
//    public ExemploThread(String mensagem, int delay) {
//        this.mensagem = mensagem;
//        this.delay = delay;
//    }
//  
//    @Override
//    public void run() {
//         for(int i = 0; i < 10; i++){
//            
//            System.out.println(this.mensagem);
//            
//            try{
//                Thread.sleep(this.delay);
//            }catch(InterruptedException e){
//                System.out.println("Error: " + e.getMessage());
//            }           
//        }
//        
//    }
    
    //EXERCÍCIO 3 e 4   
    
//    public int[] vetor;
//    public int start;
//    public int end;
//    public int sum;
//    public long delay = 0;
//
//    public ExemploThread(int[] vetor, int start, int end) {
//        this.vetor = vetor;
//        this.start = start;
//        this.end = end;
//    }   
//    
//    @Override
//    public void run() {        
//        for(int i= start; i< end; i++){
//            this.sum += vetor[i];
//            try{
//                Thread.sleep(1000);
//                System.out.println("Index:" + i);
//            }catch(InterruptedException e){
//                System.out.println("Error: " + e.getMessage());
//            }            
//        }
//    }
    
    public int[][] vetor;
    int coluna;
    public int start;
    public int end;
    public int sum;    

    public ExemploThread(int[][] vetor, int coluna, int start, int end) {
        this.vetor = vetor;
        this.coluna = coluna;
        this.start = start;
        this.end = end;
    }  
    
    @Override
    public void run() {
        System.out.println("Somando de: " + start + " até " + end);        
        for(int i= start; i< end; i++){            
                this.sum += vetor[this.coluna][i];                
                try{
                    Thread.sleep(1000);
                }catch(InterruptedException e){
                    System.out.println("Error: " + e.getMessage());
                }
            }                        
        }
}
    
  
