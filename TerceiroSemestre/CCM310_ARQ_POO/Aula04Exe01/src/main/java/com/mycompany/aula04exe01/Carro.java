package com.mycompany.aula04exe01;

public class Carro {

    private String model, color;
    private int year;
    private double km, price;

    public Carro() {
        
    }

    public Carro(String model, String color, int year) {
        this.model = model;
        this.color = color;
        this.year = year;
    }

    public Carro(String model, String color, int year, double km, double price) {
        this.model = model;
        this.color = color;
        this.year = year;
        this.km = km;
        this.price = price;
    }

    
    public String getModel() {
        return model;
    }
    
    public void setModel(String model) {
        this.model = model;
    }

    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }

    public int getYear() {
        return year;
    }

    public void setYear(int year) {
        this.year = year;
    }

    public double getKm() {
        return km;
    }

    public void setKm(double km) {
        this.km = km;
    }

    public double getPrice() {
        return price;
    }

    public void setPrice(double price) {
        this.price = price;
    }

    @Override
    public String toString() {
        return "Model: " + model 
                + " |Color: " + color 
                + " |Year: " + year
                + " |Km: " + km
                + " |Price: " + price;
    }
    
}
