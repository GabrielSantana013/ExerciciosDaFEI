package lab06exe01;
/**
 *
 * @author unifgdias
 */
public class Retangulo extends Formas{

    private double comprimento, largura;

    public double getComprimento() {
        return comprimento;
    }

    public void setComprimento(double comprimento) {
        this.comprimento = comprimento;
    }

    public double getLargura() {
        return largura;
    }

    public void setLargura(double largura) {
        this.largura = largura;
    }

    @Override
    public double perimetro() {
        return ((2*comprimento) + (2*largura));
    }
    
    @Override
    public void print() {
        super.print();
        System.out.printf("\nPerimetro: %.2f", this.perimetro());
    }
    
}
