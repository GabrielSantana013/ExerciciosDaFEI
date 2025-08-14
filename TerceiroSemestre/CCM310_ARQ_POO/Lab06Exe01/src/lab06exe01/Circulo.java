package lab06exe01;

import static java.lang.Math.pow;

/**
 *
 * @author unifgdias
 */
public class Circulo extends Formas{

    private final double PI = 3.1415;
    
    private double raio;

    public double getRaio() {
        return raio;
    }

    public void setRaio(double raio) {
        this.raio = raio;
    }
    
    public double area(){
        return PI*pow(raio,2);
    }

    @Override
    public double perimetro() {
        return 2*PI*raio;
    }
    
    @Override
    public void print() {
        super.print();
        System.out.printf("\nArea: %.2f", this.area());
        System.out.printf("\nPerimetro: %.2f", this.perimetro());
        System.out.printf("\nRaio: %.2f", this.raio);
    }      
}