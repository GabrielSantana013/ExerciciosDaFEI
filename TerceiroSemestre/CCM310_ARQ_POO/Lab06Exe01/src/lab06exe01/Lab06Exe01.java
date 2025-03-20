/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package lab06exe01;

import java.util.ArrayList;

/**
 *
 * @author unifgdias
 */
public class Lab06Exe01 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        
        ArrayList<Formas> formas = new ArrayList<>();
        
        formas.add(new Circulo());
        formas.add(new Retangulo());
        
        formas.get(0).setTipo("Círculo");
        ((Circulo)formas.get(0)).setRaio(8.7);
        
        formas.get(1).setTipo("Retângulo");
        ((Retangulo)formas.get(1)).setComprimento(5.4);
        ((Retangulo)formas.get(1)).setLargura(7.2);
        
        formas.get(0).print();
        formas.get(1).print();
    }
    
}
