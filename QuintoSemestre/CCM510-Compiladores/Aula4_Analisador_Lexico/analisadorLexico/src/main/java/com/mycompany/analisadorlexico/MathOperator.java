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

public class MathOperator extends AFD{

    @Override
    public Token evaluate(CharacterIterator code) {
        switch(code.current()){
            
            case '+':
                return new Token("PLUS", "+");
            case '-':
                return new Token("SUB", "-");
            case '*':
                return new Token("MUL", "*");
            case '/':
                return new Token("DIV", "/");
//            case '(':
//                return new Token("AP", "(");
//            case ')':
//                return new Token("FP", ")"); 
            case '\n':
                return new Token("NEW_LINE", "\n");
            case CharacterIterator.DONE:
                return new Token("EOF","$");
            default:
                return null;
        
        }
    }
}
