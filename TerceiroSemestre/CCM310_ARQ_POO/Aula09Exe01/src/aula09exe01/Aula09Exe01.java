/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package aula09exe01;

import java.util.InputMismatchException;
import java.util.Scanner;

/**
 *
 * @author unifgdias
 */
public class Aula09Exe01 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        
        while(true){
            try{
                System.out.println("Digite um numero inteiro:");
                int num = sc.nextInt();
                break;
            }
            catch(InputMismatchException e){
                sc.next();
                System.out.println("Número invalido, tente novamente");            
            }                        
        }
        
        sc.close();
    }
}