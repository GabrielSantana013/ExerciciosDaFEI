package com.mycompany.aula02exe06;

import java.util.Scanner;

public class Main {
    
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        int A, B, C;
        
        System.out.println("Digite os valores A, B e C: ");
        A = sc.nextInt();
        B = sc.nextInt();
        C = sc.nextInt();
        
        int temp;
        if(A > B)
        {
            temp = A;
            A = B;
            B = temp;
        }       
        if(B > C)
        {
            temp = B;
            B = C;
            C = temp;
        }
        if(A>B){
            temp = A;
            A = B;
            B = temp;
        }
        
        System.out.printf("Numeros ordenados crescentemente: %d, %d, %d", A,B,C);
        sc.close();
    }
}
