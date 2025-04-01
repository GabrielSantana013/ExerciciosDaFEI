/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Controller;

import Model.Soma;
import View.Janela;

/**
 *
 * @author unifgdias
 */
public class Control {
    
    private Janela view;

    public Control(Janela view) {
        this.view = view;
    }
    
    public void controlSomar(){
    
        double n1 = Double.parseDouble(view.getTxt_Num1().getText());
        double n2 = Double.parseDouble(view.getTxt_Num1().getText());
        Soma s = new Soma();
        double res = s.somar(n1,n2);
        view.getTxt_Num3().setText(String.valueOf(res));
    }
    
    public void controlLimpar(){
        view.getTxt_Num1().setText(" ");
        view.getTxt_Num2().setText(" ");
        view.getTxt_Num3().setText(" ");        
    }
   
}
