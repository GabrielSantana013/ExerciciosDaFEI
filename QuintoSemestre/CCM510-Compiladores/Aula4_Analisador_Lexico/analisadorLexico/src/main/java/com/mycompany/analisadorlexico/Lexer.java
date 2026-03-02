/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.analisadorlexico;
import java.text.CharacterIterator;
import java.text.StringCharacterIterator;
import java.util.ArrayList;

import java.util.List;

/**
 *
 * @author unifgdias
 */
public class Lexer {
    
    private List<Token> tokens;
    private List<AFD> afds;
    private CharacterIterator code;

    public Lexer(String code) {
        tokens = new ArrayList<>();
        this.code = new StringCharacterIterator(code);
        afds = new ArrayList<>();
        afds.add(new MathOperator());
        afds.add(new Number());
    }
    
    public void skipWhiteSpaces(){
        while(code.current() == ' ' || code.current() == '\n'){code.next();}        
    }
    
    public List<Token> getTokens(){
        Token t;
        do{
            skipWhiteSpaces();
            t = searchNextToken();
            if(t == null) error();
            tokens.add(t);
        }while(!t.tipo.equals("EOF"));
        return tokens;        
    }
    
    private Token searchNextToken(){
        int pos = code.getIndex();
        for(AFD afd: afds){
            Token t = afd.evaluate(code);
            if(t != null) return t;
            code.setIndex(pos);
        }
        return null;
    }
    
    private void error(){
        throw new RuntimeException("Error: token not recognized!" +
                code.current());
    }
    
}
