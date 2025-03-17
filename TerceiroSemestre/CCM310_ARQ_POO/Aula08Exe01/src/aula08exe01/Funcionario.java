package aula08exe01;

/**
 *
 * @author unifgdias
 */
public class Funcionario extends Pessoa{

    private Data admissao;
    private double salario;

    public Funcionario(String nome, long cpf, Data nascimento, Data admissao, 
            double salario) {
        super(nome, cpf, nascimento);
        this.admissao = admissao;
        this.salario = salario;
    }

    public Funcionario() {
    }
    
    public double getSalario() {
        return salario;
    }

    @Override
    public String toString() {
        
        return super.toString() + "\nAdmissao: " + admissao + "\nsalario: " + salario;
    }
}
