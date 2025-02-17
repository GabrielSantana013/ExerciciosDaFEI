package com.mycompany.aula03exe02;

public class Swapper {
    
    private Double x,y;

    public Swapper(){}
    
    
    public Double getX() {
        return x;
    }

    public void setX(Double x) {
        this.x = x;
    }

    public Double getY() {
        return y;
    }

    public void setY(Double y) {
        this.y = y;
    }

    public Swapper(Double x, Double y) {
        this.x = x;
        this.y = y;
    }
    
    void swap(){
        double temp;
        temp = x;
        x = y;
        y = temp;
    }
    
}
