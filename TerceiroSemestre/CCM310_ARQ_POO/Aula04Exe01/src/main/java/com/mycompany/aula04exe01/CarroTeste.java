package com.mycompany.aula04exe01;

import java.util.Scanner;

public class CarroTeste {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        
        Carro c1 = new Carro();
        Carro c2 = new Carro("Corsa", "Amarelo", 2004);
        Carro c3 = new Carro("Uno", "Preto", 2002, 4950.0, 1.00);
        
        
        System.out.println("Carro 1");
        System.out.println(c1);
        
        System.out.println("Carro 2");
        System.out.println(c2);
        
        System.out.println("Carro 3");
        System.out.println(c3);
       
        sc.close();
    }
    
}
