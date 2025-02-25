package aula05exe01.lab05exe01;

public class Laser {

    private String fabricante;
    private double alcance, precisao, medida;

    public Laser() {
    }

    public Laser(String fabricante, double alcance, double precisao, double medida) {
        this.fabricante = fabricante;
        this.alcance = alcance;
        this.precisao = precisao;
        this.medida = medida;
    }
    
    public String getFabricante() {
        return fabricante;
    }

    public void setFabricante(String fabricante) {
        this.fabricante = fabricante;
    }

    public double getAlcance() {
        return alcance;
    }

    public void setAlcance(double alcance) {
        this.alcance = alcance;
    }

    public double getPrecisao() {
        return precisao;
    }

    public void setPrecisao(double precisao) {
        this.precisao = precisao;
    }

    public double getMedida() {
        return medida;
    }

    public void setMedida(double medida) {
        this.medida = medida;
    }

    @Override
    public String toString() {
        return  "fabricante: " + fabricante 
                + "| alcance: " + alcance 
                + "| precisao: " + precisao 
                + "| medida: " 
                + medida;
    }
    
    
    
}
