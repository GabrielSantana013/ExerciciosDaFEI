package com.mycompany.aula02exe02;

import java.util.Scanner;
public class Main {
    
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        
        double p1 = 0, p2 = 0;
        
        System.out.println("Informe as notas de P1 e P2: ");
        p1 = sc.nextFloat();
        p2 = sc.nextFloat();
        
        double media = (p1+p2)/2;
        
        if(media < 3){
            System.out.println("Reprovado direto");
        }
        else if(media >=7){
            System.out.println("Aprovado direto");
        }
        else{
            System.out.println("Digite a nota da P3: ");
            double p3;
            p3 = sc.nextFloat();
            
            media = (media+p3)/2;
            
            if(media >=5){
                System.out.println("Aprovado na P3");
            }
            else{
                System.out.println("Reprovado na P3");
            }
        }
        sc.close();
    }
    
    
}
