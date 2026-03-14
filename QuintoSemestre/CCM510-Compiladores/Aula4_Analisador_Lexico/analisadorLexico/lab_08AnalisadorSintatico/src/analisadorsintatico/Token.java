/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package analisadorsintatico;

/**
 *
 * @author unifgdias
 */
public class Token {
    
    public String tipo;
    public String lexema;

    public Token(String tipo, String lexema) {
        this.tipo = tipo;
        this.lexema = lexema;
    }

    @Override
    public String toString() {
        return "<" + this.tipo + ", " + this.lexema + ">";
    }    
}
