/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Controller;

import Model.Operacoes;
import View.Janela;

/**
 *
 * @author unifgdias
 */
public class Control {
    
    public Janela visor;
    public double numero, resultado = 0;
    private String operacao;
    Operacoes o;
    
    public Control(Janela visor){    
        this.visor = visor;
    }
   
    
    public void controlLimpar(){
        visor.getVisor().setText(" ");
    }
    
    public void controlSomar(){
        this.numero = Double.parseDouble(visor.getVisor().getText());          
        resultado += numero;
        this.operacao = "soma";
        Operacoes o = new Operacoes(); 
        this.resultado = o.soma();
        visor.getVisor().setText(String.valueOf(this.resultado));
    }
    
    public void controlSubtrair(){}
    
    public void controlDividir(){}
    
    public void controlMultiplicar(){}
    
}
