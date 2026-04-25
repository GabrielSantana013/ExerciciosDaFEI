/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package traducaopsintaxe;

import java.util.ArrayList;
import java.util.List;

/**
 *
 * @author unifgdias
 */
public class Main {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        List<Token> tokens = new ArrayList<>();
        tokens.add(new Token("se","reservada_if"));
        tokens.add(new Token("soma","id"));
        tokens.add(new Token("<","operador_condicional"));
        tokens.add(new Token("5","num"));
        tokens.add(new Token("entao","reservada_then"));
        tokens.add(new Token("soma","id"));
        tokens.add(new Token("=","operador_atribuicao"));
        tokens.add(new Token("3","num"));
        tokens.add(new Token("senao","reservada_else"));
        tokens.add(new Token("soma","id"));
        tokens.add(new Token("=","operador_atribuicao"));
        tokens.add(new Token("2","num"));
        tokens.add(new Token("$","EOF"));
        Parser parser = new Parser(tokens);
        parser.main();
        
    }
    
}
