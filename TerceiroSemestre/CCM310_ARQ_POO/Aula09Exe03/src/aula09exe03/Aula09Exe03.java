/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package aula09exe03;

/**
 *
 * @author unifgdias
 */
public class Aula09Exe03 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        
        try{
            throw new Exception("Oia o erro\n");
        }
        catch(Exception e){
            System.err.printf("%s", e.getMessage());
        }
        finally{        
            System.out.println("Seila");
        }
        
        
    }
    
}
