package com.mycompany.aula04exe02;

public class Main {

    public static void main(String[] args) {
        
        Rectangle r1 = new Rectangle(2, 12, 2 , 12, 3 ,3 ,8 ,8);
        
        if(!r1.verificaRetangulo()){
            System.out.println("Os valores informados não formam um retangulo");
            return;
        }
        
        if(!r1.verificaQuadrante()){
            System.out.println("Um dos pontos não se encontra no primeiro "
                    + "quadrante");
        }
        System.out.println("Comprimento: ");
        System.out.println(r1.calcComprimento());
        System.out.println("Largura: ");
        System.out.println(r1.calcLargura());
        System.out.println("Perimetro: ");
        System.out.println(r1.calcPerimetro());
                
    }
}
