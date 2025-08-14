/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.aula02exe01;

import java.util.Scanner;

/**
 *
 * @author unifgdias
 */
public class Main {
  
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        int anoAtual = 0, anoNasc = 0;
        
        System.out.println("Digite o ano atual: ");
        anoAtual = sc.nextInt();
        System.out.println("Informe o ano de nascimento: ");
        anoNasc = sc.nextInt();
        
        System.out.printf("Sua idade é: %d", anoAtual - anoNasc);
        
        sc.close();
    }
    
}
