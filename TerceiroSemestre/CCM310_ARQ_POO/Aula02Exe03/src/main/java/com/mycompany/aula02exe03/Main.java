package com.mycompany.aula02exe03;

import java.util.Scanner;

public class Main {
    
    public static void main(String[] args) {
        
        
        Scanner sc = new Scanner(System.in);
        int contPessoas = 0;
        double somaAlturas = 0;
        
        while(contPessoas < 5)
        {
            System.out.println("Informe sua altura: ");
            double altura;
            altura = sc.nextDouble();
            somaAlturas += altura;
            contPessoas++;
        }
        
        double mediaAlturas = somaAlturas/contPessoas;
        System.out.printf("Media das alturas: %.2f", mediaAlturas);
              
        sc.close();
    }
}
