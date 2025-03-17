package aula08exe01;

import java.util.ArrayList;
import java.util.Scanner;

/**
 *
 * @author unifgdias
 */
public class Main {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        ArrayList<Funcionario> funcionarios = new ArrayList<>();
        ArrayList<Gerente> gerentes = new ArrayList<>();
        
        System.out.println("==== Cadastro de  2 funcionarios ====");
        for(int i = 0; i < 2; i ++){
        
            System.out.printf("Digite o nome do funcionario %d\n", i+1);
            String nome = sc.nextLine();
            System.out.printf("Digite o cpf do funcionario %d\n", i+1);
            long cpf = sc.nextInt();            
            System.out.printf("Digite a data de nascimento do funcionario (dd mm yyyy)"
                    + " %d\n", i+1);
            int dia = sc.nextInt(); 
            int mes = sc.nextInt(); 
            int ano = sc.nextInt(); 
            Data nascimento = new Data(dia,mes,ano);
            System.out.printf("Digite a data de admissao do funcionario (dd mm yyyy)"
                    + " %d\n", i+1);
            dia = sc.nextInt(); 
            mes = sc.nextInt(); 
            ano = sc.nextInt(); 
            Data admissao = new Data(dia,mes,ano);
            System.out.printf("Digite o salario do funcionario %d\n", i+1);
            double salario = sc.nextDouble();
            sc.nextLine();
            
            funcionarios.add(new Funcionario(nome, cpf, nascimento, admissao, 
                    salario));
            
        }
        
        System.out.println("==== Cadastro de 2 Gerentes ====");
        for(int i = 0; i < 2; i ++){
        
            System.out.printf("Digite o nome do gerente %d\n", i+1);
            String nome = sc.nextLine();
            System.out.printf("Digite o cpf do gerente %d\n", i+1);
            long cpf = sc.nextInt();            
            System.out.printf("Digite a data de nascimento do gerente (dd mm yyyy)"
                    + " %d\n", i+1);
            int dia = sc.nextInt(); 
            int mes = sc.nextInt(); 
            int ano = sc.nextInt(); 
            Data nascimento = new Data(dia,mes,ano);
            System.out.printf("Digite a data de admissao do gerente (dd mm yyyy)"
                    + " %d\n", i+1);
            dia = sc.nextInt(); 
            mes = sc.nextInt(); 
            ano = sc.nextInt(); 
            Data admissao = new Data(dia,mes,ano);
            System.out.printf("Digite o salario do gerente %d\n", i+1);
            double salario = sc.nextDouble();
            System.out.printf("Digite o departamento do gerente %d\n", i+1);
            int departamento = sc.nextInt();
            System.out.printf("Digite a data de promocao do gerente (dd mm yyyy)"
                    + " %d\n", i+1);
            dia = sc.nextInt();
            mes = sc.nextInt(); 
            ano = sc.nextInt();
            sc.nextLine();
            Data promocao = new Data(dia,mes,ano);
            gerentes.add(new Gerente(nome, cpf, nascimento, admissao, 
                    salario, departamento, promocao));
            
        }
        
        int contaP = 1;
        for(Funcionario f: funcionarios){
            System.out.printf("\nFuncionario %d: \n", contaP);
            System.out.println(f);
            contaP++;
        }
        
        contaP = 1;
        for(Gerente g: gerentes){
            System.out.printf("\nGerente %d: \n", contaP);
            System.out.println(g);
            contaP++;
        }
       
        sc.close();
    }
    
}
