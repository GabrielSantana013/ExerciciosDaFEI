package lab06exe01;

/**
 *
 * @author unifgdias
 */
public abstract class Formas {

    private String tipo;

    public String getTipo() {
        return tipo;
    }

    public void setTipo(String tipo) {
        this.tipo = tipo;
    }
    
    public abstract double perimetro();
    public void print(){
        System.out.printf("\nTipo: %s", this.tipo);
    };
    
}
