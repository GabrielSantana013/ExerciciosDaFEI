/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Model;

/**
 *
 * @author unifgdias
 */
public class Operacoes {
 
    public double n1;
    public double n2;
    public String operacao;

    public Operacoes(){}
    
    public Operacoes(double n1, double n2, String operacao) {
        this.n1 = n1;
        this.n2 = n2;
        this.operacao = operacao;
    }
    
    public double soma(){
        return n1+n2;
    }
    
    public double subtracao(){
        return n1-n2;
    }
    
    public double multiplicacao(){
        return n1*2;
    }
    
    public double divisao(){
        if(n2 != 0){
            return n1/n2;
        } 
        return 0;
    }
    
    public double calcula(){
        if(this.operacao == "soma"){
            return this.soma();
        }
        else if(this.operacao == "subtracao"){
            return this.subtracao();
        }
        else if(this.operacao == "multiplicacao"){
            return this.multiplicacao();
        }
        else{
            return this.divisao();
        }
        
    }
    
}
