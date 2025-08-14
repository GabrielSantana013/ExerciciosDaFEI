/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package aula08exe01;

/**
 *
 * @author unifgdias
 */
public class Gerente extends Funcionario{
    
    private int departamento;
    private Data promocaoGerente;

    public Gerente(String nome, long cpf, Data nascimento, Data admissao, 
            double salario, int departamento, Data promocaoGerente) {
        super(nome, cpf, nascimento, admissao, salario);
        this.departamento = departamento;
        this.promocaoGerente = promocaoGerente;
    }

    public int getDepartamento() {
        return departamento;
    }

    @Override
    public String toString() {
        
        return super.toString() + "\nDepartamento: " + departamento
                + "\nPromocaoGerente: " + promocaoGerente;
    }

    
}
