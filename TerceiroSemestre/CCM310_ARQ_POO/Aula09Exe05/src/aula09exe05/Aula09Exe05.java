/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package aula09exe05;

/**
 *
 * @author unifgdias
 */

class ExcecaoA extends Exception{

    public ExcecaoA(String mensagem){
        super(mensagem);
    }
}

class ExcecaoB extends Exception{

    public ExcecaoB(String mensagem){
        super(mensagem);
    }
}

class ExcecaoC extends Exception{
    public ExcecaoC(String mensagem){
        super(mensagem);
    }
}

class LancaExcecao {
    public static void lancar(int tipo)throws ExcecaoA, ExcecaoB, ExcecaoC{
        switch(tipo){
            case 1:
                throw new ExcecaoA("Erro A");
                
            case 2:
                throw new ExcecaoB("Erro B");
                
            case 3:
                throw new ExcecaoC("Erro C");
                
        }
    }  
}

public class Aula09Exe05 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        
        try{
            LancaExcecao.lancar(3);        
        }catch(Exception e){
            System.err.printf("%s\n", e.getMessage());        
        }
        
    }
    
}
