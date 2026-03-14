/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package analisadorsintatico;

import java.util.List;

/**
 *
 * @author unifgdias
 */
public class Parser {
    
    List<Token> tokens;
    Token token;

    public Parser(List<Token> tokens) {
        this.tokens = tokens;
    }
    
    public Token getNextToken(){
        if(tokens.size() > 0)
            return tokens.remove(0);
        return null;
    }
    
    public void erro(String regra){
        System.out.println("ERRO");
        System.out.println("============================");
        System.out.println("Regra " + regra);
        System.out.println("Token inválido: " + token.lexema);
        System.out.println("============================");
    }
    
    public void sucesso(){
        System.out.println("****************************");
        System.out.println("Todos os tokens são válidos!");
        System.out.println("Programa finalizado com sucesso");
        System.out.println("****************************");
    }
    
    /*
    ifelse: 'if' condicao 'then' expressao
    condicao: id operador num
    expressao: id '=' num
    operador '>' | '<' | '='
    enquanto: 'enquanto' id operador num
    
    id: [a-z]+
    num: [0-9]+
    
    */
    
    /*Métodos pra validar a gramática*/
    
    public boolean ifelse(){
        if(token.tipo.equals("reservada_if")){
            token = getNextToken();
            if(condicao()){         
                if(token.tipo.equals("reservada_then")){
                    token = getNextToken();
                    if(expressao()){
                        if(token.tipo.equals("reservada_else")){
                            token = getNextToken();
                            if(expressao()){
                                return true;
                            }
                        }
                        
                    }
                    
                }
            }
        }
       erro("ifelse");
        return false; 
    }
    
    public boolean condicao(){
        if(id()){            
            if(operador()){                
                if(num()){                    
                    return true;
                }
            }
        }
        erro("condicao");
        return false;
    }
    public boolean expressao(){
        if(id()){            
            if(token.tipo.equals("operador_atribuicao")){
                token = getNextToken();
                if(num()){                                       
                    return true;
                }                     
            }           
        }
        erro("expressao");
        return false;
    }
    public boolean operador(){
        if(token.lexema.equals(">")){
            token = getNextToken();
            return true;
        }                  
        else if(token.lexema.equals("<")){
            token = getNextToken();
            return true;}
        else if(token.lexema.equals("=")){
                token = getNextToken();
            return true;}
        
        erro("operador");
        return false;
    }
    public boolean id(){
        
        String palavra = token.lexema;
        int i = 0;
        
        //JEITO CORRETO DE FAZER
        //if(token.tipo.equals("id"))...
        
        
        //Responsabilidade do analisador léxico NÃO FAZER!!!!!!!
        while(i < palavra.length() && palavra.charAt(i) <= 122 && palavra.charAt(i) >= 96){
            i++;            
        }
        if(i != palavra.length()){
            erro("id");
            return false;
        }
        token = getNextToken();
        return true;
    }
    public boolean num(){
        String numero = token.lexema;
        int i = 0;        
        while(i < numero.length() && numero.charAt(i) <= 57 && numero.charAt(i) >= 48){
            i++;            
        }
        if(i != numero.length()){
            erro("num");
            return false;
        }
        token = getNextToken();        
        return true;
    }
    
    //enquanto: 'enquanto' id operador num
    
    public boolean enquanto(){
        if(token.lexema.equals("enquanto")){
            token = getNextToken();
            if(condicao()){                                
                if(token.lexema.equals(":")){
                    token = getNextToken();
                    if(expressao()){
                        return true;
                    }
               }                                  
            }           
        }
        erro("enquanto");
        return false;
    }
    
    public void principal(){
        token = getNextToken();
        if(/*ifelse()*/enquanto()){
            if (token.tipo.equals("EOF")){
                sucesso();
                return;
            }
            else{
                //erro("ifelse");
                erro("enquanto");
            }
        }
    }    
}
