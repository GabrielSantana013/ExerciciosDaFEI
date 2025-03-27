/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package aula09exe06;

/**
 *
 * @author unifgdias
 */
public class Pessoa {
    
    private String nome, sobrenome, CPF;
    private int idade;

    public Pessoa(String nome, String sobrenome, String CPF, int idade) {
        this.nome = nome;
        this.sobrenome = sobrenome;
        this.CPF = CPF;
        this.idade = idade;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getSobrenome() {
        return sobrenome;
    }

    public void setSobrenome(String sobrenome) {
        this.sobrenome = sobrenome;
    }

    public String getCPF() {
        return CPF;
    }

    public void setCPF(String CPF) throws Exception{
        CpfException.validaCpf(CPF);
    }

    public int getIdade() {
        return idade;
    }

    public void setIdade(int idade) {
        this.idade = idade;
    }
    
    
    class CpfException extends Exception{
    
        public static void validaCpf(String cpf) throws Exception{
            for(int i = 0; i < cpf.length(); i++){            
                if(cpf.charAt(i) == '.' || cpf.charAt(i) == '-')
                {                    
                    
                }
            
            }          
        }
    }   
}
