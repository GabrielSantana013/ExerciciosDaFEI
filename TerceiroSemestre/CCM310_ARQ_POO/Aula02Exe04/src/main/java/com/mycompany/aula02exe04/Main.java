/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.aula02exe04;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        
        double num = 1, soma = 0;
        
        while(num != 0){
            System.out.println("Digite um número: ");
            num = sc.nextDouble();
            soma += num;
        }
        
        System.out.printf("A soma de todos os números é: %.2f", soma);
        
        sc.close();
    }
}
