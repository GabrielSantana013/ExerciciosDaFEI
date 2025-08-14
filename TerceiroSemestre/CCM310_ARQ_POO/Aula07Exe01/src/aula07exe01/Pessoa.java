package aula07exe01;

/**
 *
 * @author unifgdias
 */
public class Pessoa {
    
    protected String name, lastName;
    protected int age;

    public Pessoa(){}
    
    public Pessoa(String name, String lastName, int age) {
        this.name = name;
        this.lastName = lastName;
        this.age = age;
    }

    public String getName() {
        return name;
    }

    public String getLastName() {
        return lastName;
    }

    public int getAge() {
        return age;
    }
    
    
    
}
