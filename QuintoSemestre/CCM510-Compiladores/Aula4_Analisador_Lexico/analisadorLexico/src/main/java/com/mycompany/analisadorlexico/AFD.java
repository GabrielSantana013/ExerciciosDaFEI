/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.analisadorlexico;
import java.text.CharacterIterator;
/**
 *
 * @author unifgdias
 */
public abstract class AFD {
    
    public abstract Token evaluate(CharacterIterator code);
    
    public boolean isTokenSeparator(CharacterIterator code){
        return code.current() == ' ' ||
            code.current() == '+' ||
            code.current() == '-' ||
            code.current() == '*' ||
            code.current() == '/' ||
            code.current() == '(' ||
            code.current() == ')' ||
            code.current() == '\n' ||
            code.current() == CharacterIterator.DONE;
    }   
}
