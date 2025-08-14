package com.mycompany.aula02exe05;

import java.util.Scanner;

public class Main {
    
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        double salario = 0;
        int qttHoras = 0;
        
        System.out.println("Digite o valor do seu salário por hora: ");
        salario = sc.nextDouble();
        
        System.out.println("Digite a quantidade de horas: ");
        qttHoras = sc.nextInt();
        
        System.out.printf("Seu salário é: %.2f", salario * qttHoras);
        sc.close();
        
    }
}
