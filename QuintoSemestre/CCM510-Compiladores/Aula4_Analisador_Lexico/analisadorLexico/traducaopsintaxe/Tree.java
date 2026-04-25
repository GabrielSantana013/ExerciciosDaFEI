/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package traducaopsintaxe;

/**
 *
 * @author unifgdias
 */
public class Tree {

    Node root;
    
    public Tree() {
    }

    public Tree(Node root) {
        this.root = root;
    }

    public void setRoot(Node root) {
        this.root = root;
    }        
    
    public void preOrder(){
        preOrder(root);
        System.out.println("");        
    }
    
    public void printCode(){
        printCode(root);
        System.out.println("");
    }
    
    public void preOrder(Node node){
        System.out.println(node);
        for(Node n: node.nodes){
            preOrder(n);   
        }
        System.out.println(node.exit);        
    }
    
    public void printCode(Node node){
        System.out.println(node.enter);
        if(node.nodes.isEmpty()){
            System.out.println(node);
        }
        for(Node n : node.nodes){
            printCode(n);
        }
        System.out.println(node.exit);
    }
    
    public void printTree(){
        System.out.println(root.getTree());
    }
    
}
