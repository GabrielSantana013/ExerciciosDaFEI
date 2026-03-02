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
        return switch (code.current()) {
            case '+' -> {
                code.next();
                yield new Token("PLUS", "+");
            }
            case '-' -> {
                code.next();
                yield new Token("SUB", "-");
            }
            case '*' -> {
                code.next();
                yield new Token("MUL", "*");
            }
            case '/' -> {
                code.next();
                yield new Token("DIV", "/");
            }
//            case '(':
//                return new Token("AP", "(");
//            case ')':
//                return new Token("FP", ")");
            case '\n' -> {
                code.next();
                yield new Token("NEW_LINE", "\n");
            }
            case CharacterIterator.DONE -> {
                code.next();
                yield new Token("EOF", "$");
            }
            default -> null;
        };
    }
}
