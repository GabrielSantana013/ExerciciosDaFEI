package com.mycompany.aula03exe01;

public class Pessoa {

    private String CPF;
    private String name;
    private int age;

    public Pessoa(String CPF, String name, int age) {
        this.CPF = CPF;
        this.name = name;
        this.age = age;
    }

    public Pessoa(){}

    public String getCPF() {
        return CPF;
    }

    public void setCPF(String CPF) {
        this.CPF = CPF;
    }

    public String getName() {
        return name;
    }

    public void setName(String nome) {
        this.name = nome;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        if(age<0 || age > 150){age = 0;}
        this.age = age;
    }

    @Override
    public String toString() {
        return "Nome: " + name + "| Idade: " + age + "| CPF: " + CPF;
    }
   
}
