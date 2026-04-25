/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package traducaopsintaxe;

import java.util.List;

/**
 *
 * @author unifgdias
 */
public class Parser {
    
    List<Token> tokens;
    Token token;
    String traducao = "";

    public Parser(List<Token> tokens) {
        this.tokens = tokens;
    }
    
    public void main(){
        token = getNextToken();
        Node root = new Node("main");
        Tree tree = new Tree();
        tree.setRoot(root);
        header();
        
        if(ifelse(root)){            
            if(token.tipo == "EOF"){
                footer();
                System.out.println("\nSintaticamente correta\n");                
                System.out.println(traducao); 
                
                System.out.println("=============\n");
                tree.printTree();
                
                return;
            }
            else{
                erro();
            }
        }
        erro();
    }
    
    public Token getNextToken(){
        if(!tokens.isEmpty()){
            return tokens.remove(0);
        }else{
        return null;}
    }
    
    private void erro(){
        System.out.println("Token inválido" + token.lexema);
    }
    
    private boolean ifelse(Node node){
        Node ifelse = node.addNode("ifelse");
        if(matchL("se", "   if", ifelse) && condicao(ifelse) && matchL("entao", "    ") && bloco(ifelse) && 
                matchL("senao", "   else", ifelse) && bloco(ifelse)){
            return true;
        }
        return false;
    }
    
    private boolean bloco(Node node){
        traduz("{");
        Node bloco = node.addNode("bloco");
        if(id(bloco) && operadorAtribuicao(bloco) && num(bloco)){
            traduz("}\n");
            return true;
        }
        return false;    
    }
    
    private boolean operadorAtribuicao(Node node){
        Node operadorAtribuicao = node.addNode("operadorAtribuicao");
        if(matchL("=", operadorAtribuicao)){
            return true;
        }
        return false;
    }
    
    private boolean condicao(Node node){
        traduz("(");
        Node condicao = node.addNode("condicao");
        if(id(condicao) && operador(condicao) && num(condicao)){
            traduz(")\n");
            return true;
        }
        return false;
    }
    
    private boolean operador(Node node){
        Node operador = node.addNode("operador");
        if(matchL(">", operador) || matchL("<", operador) || matchL("==", operador)){
            return true;
        }
        return false;
    }
    
    private boolean id(Node node){
        Node id = node.addNode("id");
        if(matchT("id", token.lexema, id)){
            return true;
        }
        return false;
    }
    
    private boolean num(Node node){
        Node num = node.addNode("num");
        if(matchT("num", token.lexema, num)){
            return true;
        }
        return false;        
    }
    
//    private boolean matchL(String palavra){
//        if(token.lexema.equals(palavra)){
//            token = getNextToken();
//            return true;
//        }
//        return false;
//    }
//    
//    private boolean matchT(String palavra){
//        if(token.tipo.equals(palavra)){
//            token = getNextToken();
//            return true;
//        }
//        return false;
//    }
    
    private boolean matchL(String palavra, String newCode){
        if(token.lexema.equals(palavra)){
            traduz(newCode);
            token = getNextToken();
            return true;
        }
        return false;
    }
    
    private boolean matchT(String palavra, String newCode){
        if(token.tipo.equals(palavra)){
            traduz(newCode);
            token = getNextToken();
            return true;
        }
        return false;
    }
    
    private boolean matchL(String palavra, Node node){
        if(token.lexema.equals(palavra)){
            node.addNode(token.lexema);
            token = getNextToken();
            return true;
        }
        return false;
    }
    
    private boolean matchT(String palavra, Node node){
        if(token.tipo.equals(palavra)){
            node.addNode(token.lexema);
            token = getNextToken();
            return true;
        }
        return false;
    }
    
    private boolean matchL(String palavra, String newCode, Node node){
        if(token.lexema.equals(palavra)){
            traduz(newCode);   
            node.addNode(token.lexema);
            token = getNextToken();                     
            return true;
        }
        return false;
    }
    
    private boolean matchT(String palavra, String newCode, Node node){
        if(token.tipo.equals(palavra)){
            traduz(newCode);
            node.addNode(token.lexema);            
            token = getNextToken();
            return true;
        }
        return false;
    }

    private void traduz(String code) {
        traducao += code;
    }
    
    private void header(){
        traducao += "Public class Exemplo{\n";
        traducao += "   public static void main(String[] args){\n";
    }
    
    private void footer(){
        traducao += "   }\n";
        traducao += "}";
    }
    
}
