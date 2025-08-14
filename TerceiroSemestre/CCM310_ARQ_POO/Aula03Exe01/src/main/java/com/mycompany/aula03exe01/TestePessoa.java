package com.mycompany.aula03exe01;

import java.util.Scanner;

public class TestePessoa {
    
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        
        System.out.println("Digite seu CPF: ");
        String CPF = sc.nextLine();
        
        System.out.println("Digite seu Nome: ");
        String name = sc.nextLine();
        
        System.out.println("Digite sua Idade: ");
        int age = sc.nextInt();
        sc.nextLine();
        
        Pessoa p1 = new Pessoa(CPF, name, age); 
        
        System.out.println("Digite seu CPF: ");
        CPF = sc.nextLine();
        
        System.out.println("Digite seu Nome: ");
        name = sc.nextLine();
        
        System.out.println("Digite sua Idade: ");
        age = sc.nextInt();
        sc.nextLine();
        
        Pessoa p2 = new Pessoa(CPF, name, age); 
        
        System.out.println("Digite seu CPF: ");
        CPF = sc.nextLine();
        
        System.out.println("Digite seu Nome: ");
        name = sc.nextLine();
        
        System.out.println("Digite sua Idade: ");
        age = sc.nextInt();
        sc.nextLine();
        
        Pessoa p3 = new Pessoa(CPF, name, age); 
        
        System.out.println(p1);
        System.out.println(p2);
        System.out.println(p3);
        sc.close();
    }
    
}
