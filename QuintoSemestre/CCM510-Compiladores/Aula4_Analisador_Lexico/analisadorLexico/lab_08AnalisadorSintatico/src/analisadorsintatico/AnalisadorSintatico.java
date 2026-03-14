
/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package analisadorsintatico;

import java.util.ArrayList;
import java.util.List;

/**
 *
 * @author unifgdias
 */
public class AnalisadorSintatico {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        List<Token> tokens = new ArrayList<>();
//        tokens.add(new Token("reservada_if", "if"));
//        tokens.add(new Token("id", "soma"));
//        tokens.add(new Token("operador_condicional", ">"));
//        tokens.add(new Token("num", "5"));
//        tokens.add(new Token("reservada_then", "then"));
//        tokens.add(new Token("id", "soma"));
//        tokens.add(new Token("operador_atribuicao", "="));
//        tokens.add(new Token("num", "3"));
//        tokens.add(new Token("reservada_else", "else"));
//        tokens.add(new Token("id", "soma"));
//        tokens.add(new Token("operador_atribuicao", "="));
//        tokens.add(new Token("num", "2"));
        
        tokens.add(new Token("reservada_enquanto", "enquanto"));
        tokens.add(new Token("id", "x"));
        tokens.add(new Token("operador_condicional", ">"));
        tokens.add(new Token("num", "5"));
        tokens.add(new Token("reservada_terminacao", ":"));
        tokens.add(new Token("id", "x"));
        tokens.add(new Token("operador_atribuicao", "="));
        tokens.add(new Token("num", "1"));
        
        tokens.add(new Token("EOF", "$"));
        Parser parser = new Parser(tokens);
        parser.principal();
        
//        if soma > 5 then;
//                soma = 3
//        else
//            soma = 2 $
        
    }
    
}
