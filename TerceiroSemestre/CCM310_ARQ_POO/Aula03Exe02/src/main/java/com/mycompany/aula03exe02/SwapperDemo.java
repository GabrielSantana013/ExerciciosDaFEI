package com.mycompany.aula03exe02;

import java.util.Scanner;

public class SwapperDemo {
    
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        
        Swapper troca = new Swapper();
        
        double x, y;
        
        System.out.println("Digite o primeiro número: ");
        x = sc.nextDouble();
        troca.setX(x);
       
        System.out.println("Digite o segundo número");
        y = sc.nextDouble();
        troca.setY(y);
        
        System.out.println("Antes da troca:");
        System.out.printf("X: %.2f Y: %.2f\n", troca.getX(), troca.getY());
        System.out.println("Depois da troca:");
        troca.swap();
        System.out.printf("X: %.2f Y: %.2f\n", troca.getX(), troca.getY());
       
        
        sc.close();
        
    }
    
}
