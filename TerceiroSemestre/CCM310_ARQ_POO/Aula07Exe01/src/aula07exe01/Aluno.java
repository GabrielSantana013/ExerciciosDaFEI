package aula07exe01;

/**
 *
 * @author unifgdias
 */
public class Aluno extends Pessoa{

    private String curso;

    public Aluno(){}
    
    public Aluno(String name, String lastName, int age) {
        super(name, lastName, age);
    }

    public Aluno(String name, String lastName, int age, String curso) {
        super(name, lastName, age);
        this.curso = curso;
    }

    public void setCurso(String curso) {
        this.curso = curso;
    }

    public String getCurso() {
        return curso;
    }

    @Override
    public String toString() {
        return "Aluno: " + getName() 
                + " " + getLastName() 
                + " Idade:  "
                + getAge()
                + " Curso: "
                + getCurso();
    }
    
    
    
    
    
    
    
}
