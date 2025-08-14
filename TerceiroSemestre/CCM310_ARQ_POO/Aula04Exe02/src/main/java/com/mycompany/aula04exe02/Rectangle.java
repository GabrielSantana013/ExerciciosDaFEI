package com.mycompany.aula04exe02;

import static java.lang.Math.abs;

public class Rectangle {

    private double x1,x2,x3,x4,y1,y2,y3,y4;

    public Rectangle() {
    }

    public Rectangle(double x1, double x2, double x3, double x4, double y1,
            double y2, double y3, double y4) {
        this.x1 = x1;
        this.x2 = x2;
        this.x3 = x3;
        this.x4 = x4;
        this.y1 = y1;
        this.y2 = y2;
        this.y3 = y3;
        this.y4 = y4;
    }
    
    
    public double getX1() {
        return x1;
    }

    public void setX1(double x1) {
        if(x1>20.0)
        {
            System.out.println("Valor inválido (deve ser menor que 20.0)");
        }
        else{
            this.x1 = x1;
        }
    }

    public double getX2() {
        return x2;
    }

    public void setX2(double x2) {
        if(x2>20.0)
        {
            System.out.println("Valor inválido (deve ser menor que 20.0)");
        }
        else{
            this.x2 = x2;
        }
    }

    public double getX3() {
        return x3;
    }

    public void setX3(double x3) {
        if(x3>20.0)
        {
            System.out.println("Valor inválido (deve ser menor que 20.0)");
        }
        else{
            this.x3 = x3;
        }
    }

    public double getX4() {
        return x4;
    }

    public void setX4(double x4) {
        if(x4>20.0)
        {
            System.out.println("Valor inválido (deve ser menor que 20.0)");
        }
        else{
            this.x4 = x4;
        }
    }

    public double getY1() {
        return y1;
    }

    public void setY1(double y1) {
        if(y1>20.0)
        {
            System.out.println("Valor inválido (deve ser menor que 20.0)");
        }
        else{
            this.y1 = y1;
        }
    }

    public double getY2() {
        return y2;
    }

    public void setY2(double y2) {
        if(y2>20.0)
        {
            System.out.println("Valor inválido (deve ser menor que 20.0)");
        }
        else{
            this.y2 = y2;
        }
    }

    public double getY3() {
        return y3;
    }

    public void setY3(double y3) {
        if(y3>20.0)
        {
            System.out.println("Valor inválido (deve ser menor que 20.0)");
        }
        else{
            this.y3 = y3;
        }
    }

    public double getY4() {
        return y4;
    }

    public void setY4(double y4) {
       if(y4>20.0)
        {
            System.out.println("Valor inválido (deve ser menor que 20.0)");
        }
        else{
            this.y4 = y4;
        }
    }
    
    public boolean verificaQuadrante(){
        
        if(x1>0 && x2>0 && x3>0 && x4>0 && y1>0 && y2>0 && y3>0 && y4>0)
        {
            return true;
        }
        else{
            return false;
        }
    }
    
    public boolean verificaRetangulo(){
    
            if(x1 == x3 && x2 == x4 && y1 == y2 && y3 == y4){
                return true;
            }
            else{
                return false;
            }
    }
    
    public double calcComprimento(){
        double comprimento = abs(y1-y3);
        return comprimento;       
    }
    
    public double calcLargura(){
        double largura = abs(x1-x2);
        return largura;
    }
    
    public double calcPerimetro(){
        
        double perimetro = 2* calcComprimento() + 2 * calcLargura();
        return perimetro;
    }
    
    
    
}
