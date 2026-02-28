/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.analisadorlexico;

/**
 *
 * @author unifgdias
 */
import java.util.List;
public class Main {
    
    public static void main(String[] args) {
        
        List<Token> tokens = null;
        
        String data = "+++";
        Lexer lexer = new Lexer(data);
        tokens = lexer.getTokens();
        for(Token token : tokens){
            System.out.println(token);
        }                
    }
    
}
