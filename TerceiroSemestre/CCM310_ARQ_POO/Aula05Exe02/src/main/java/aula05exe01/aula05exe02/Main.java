package aula05exe01.aula05exe02;

import java.util.ArrayList;

public class Main {

    public static void main(String[] args) {
        
    ArrayList<String> l1 = new ArrayList<>();
    ArrayList<String> l2 = new ArrayList<>();
    
    l1.add("Amarelo");
    l1.add("Verde");
    l1.add("Vermelho");
    
    l2.add("Verde");
    l2.add("Amarelo"); 
    l2.add("Vermelho"); 
    
    for(int i = 0; i < l1.size(); i++)
    {
        // .equals() é case sensitive, equalsIgnoreCase() ñ.
        if(l1.get(i).equalsIgnoreCase(l2.get(i)))
            System.out.printf("Iguais em %d\n", i);
        else
            System.out.printf("Diferentes em %d\n", i);
    }
    
    System.out.println(l1.containsAll(l2));
    System.out.println(l2.containsAll(l1));
         
    
  }
    
}
