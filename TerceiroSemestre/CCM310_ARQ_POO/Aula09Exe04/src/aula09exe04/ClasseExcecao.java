/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package aula09exe04;

import java.util.InputMismatchException;

/**
 *
 * @author unifgdias
 */
public class ClasseExcecao extends InputMismatchException{
    
    private String argumento;
    
    public ClasseExcecao(String argumento){        
        this.argumento = argumento;        
    }    
    public void exibeString(){
        System.out.printf("%s", this.argumento);
    }
}
