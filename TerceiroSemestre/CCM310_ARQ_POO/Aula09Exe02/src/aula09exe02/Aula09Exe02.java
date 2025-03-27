/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package aula09exe02;

/**
 *
 * @author unifgdias
 */
public class Aula09Exe02 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        
        String obj = null;
        
        try{
            obj.charAt(0);
        }
        catch(NullPointerException e){
            System.out.println("Erro! Ponteiro nulo");
        }
        
    }
    
}
