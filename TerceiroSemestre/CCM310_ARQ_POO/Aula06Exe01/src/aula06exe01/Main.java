package aula06exe01;

import java.util.ArrayList;
import java.util.Scanner;

public class Main {

    static ArrayList<Pessoa> agenda = new ArrayList<>();
    
    public static void cadastraContato(){
        
        Scanner sc = new Scanner(System.in);
        System.out.println("Digite o nome da pessoa: ");
        String name = sc.nextLine();
        System.out.println("Digite o telefone: ");
        String phoneNumber = sc.nextLine();
        
        Pessoa novaPessoa = new Pessoa(name, phoneNumber);
        
        agenda.add(novaPessoa);
    }
    
    public static void deletaContato(){
        
        Scanner sc = new Scanner(System.in);
        
        System.out.println("Digite o nome: ");
        String name = sc.nextLine();
       
        for(int i = 0; i < agenda.size(); i++)
        {
            if(agenda.get(i).getName().equalsIgnoreCase(name)){
                agenda.remove(i);
            }    
        }
    }
    
    public static void imprimeAgenda(){
    
        System.out.println("=====AGENDA=====");
        for(Pessoa p: agenda){
            System.out.println(p);
        }   
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        char menu;
        while(true){
            System.out.println("Entre com uma das seguintes opções:\n");
            System.out.println("n [nova entrada]");
            System.out.println("d [apaga registro da agenda]");
            System.out.println("p [imprime toda a agenda]");
            System.out.println("q [sai do programa]\n");
            menu = sc.nextLine().charAt(0);
            
            if(menu == 'q') break;
            else if(menu == 'n'){cadastraContato();}
            else if(menu == 'd'){deletaContato();}
            else{imprimeAgenda();}
        }
  
        sc.close();
    }
    
}
