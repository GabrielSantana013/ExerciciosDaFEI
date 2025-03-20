package lab06exe02;

/**
 *
 * @author unifgdias
 */
public class Area {
    public void imprimirArea(double lado){
        System.out.printf("\nArea do quadrado: %.2f", Math.pow(lado, 2));
    }
    public void imprimirArea(double comprimento, double largura){    
        System.out.printf("Area do Retãngulo: %.2f", comprimento*largura);
    }        
}
