/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package lab05;

/**
 *
 * @author unifgdias
 */
public class Exemplo4 {
    
    public static void main(String[] args) {
        
        int[] vetor = {1,2,3,4,5,6,7,8,9,10};
        int sum = 0;
        
        long inicio = System.nanoTime();
        
        for(int i=0; i<10; i++){
            sum +=vetor[i];
            try{
                Thread.sleep(1000);
            }catch(Exception e){
                System.out.println("Erro: "+ e.getMessage());
            }
            
        }
        
        long fim = System.nanoTime();
        long duracao = fim - inicio;
        
        System.out.println("Tempo de execucão em ms: " + duracao);
    }
    
}
