/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package aula09exe04;

import java.util.Scanner;

/**
 *
 * @author unifgdias
 */
public class Aula09Exe04 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        try{
            throw new ClasseExcecao("Super erro");            
        }catch(ClasseExcecao e){
            System.err.println("Erro maluco");
        }
        finally{
            System.out.println("Batatas");
        }
        
        sc.close();
    }
    
}
