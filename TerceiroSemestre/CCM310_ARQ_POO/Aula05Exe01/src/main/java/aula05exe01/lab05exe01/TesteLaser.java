package aula05exe01.lab05exe01;

import java.util.Scanner;


public class TesteLaser {

    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        Laser l[] = new Laser[10];
        
        for(int i = 0; i < 10; i ++){
        
            l[i] = new Laser("Xiaomi", 10*i, 20/(i+1), Math.pow(2,i));
        
        }
                
        for(int i = 0; i < 10; i ++){
        
            System.out.println(l[i]);
        
        }
        
        sc.close();
    }
    
}
