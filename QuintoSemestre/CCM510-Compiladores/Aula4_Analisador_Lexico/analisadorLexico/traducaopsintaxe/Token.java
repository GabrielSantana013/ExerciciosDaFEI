/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package traducaopsintaxe;

/**
 *
 * @author unifgdias
 */
public class Token {

    protected String tipo;    
    protected String lexema;

    public Token(String lexema, String tipo) {
        this.tipo = tipo;
        this.lexema = lexema;
    }    

    @Override
    public String toString() {
        return "<" + tipo + "," + lexema + ">";
    }
}
