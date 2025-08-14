package aula07exe01;

import java.util.ArrayList;
import java.util.Scanner;

/**
 *
 * @author unifgdias
 */
public class Main {
    
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        
        ArrayList<Aluno> alunos = new ArrayList<>();
        

        alunos.add(new Aluno());
        
        System.out.println("Digite o nome do aluno: ");
        String name = sc.nextLine();
        
        System.out.println("Digite o sobrenome do aluno: ");
        String lastName = sc.nextLine();
        
        
        System.out.println("Digite a idade: ");
        int age = sc.nextInt();
        sc.nextLine();
        
        System.out.println("Digite o curso do aluno: ");
        String curso = sc.nextLine();

        alunos.add(new Aluno(name, lastName, age, curso));
        
        for(Aluno a: alunos){
            System.out.println(a);
        }
        
        sc.close();
    }
    
}
