package aula06exe01;

public class Pessoa {

    private String name, phoneNumber;
    private static int globalId = 1;
    private int Id;
  
    public Pessoa(String name, String phoneNumber) {
        this.name = name;
        this.phoneNumber = phoneNumber;
        this.Id = currentId();
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getPhoneNumber() {
        return phoneNumber;
    }

    public void setPhoneNumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
    }

    public int getId() {
        return Id;
    }

    public void setId(int Id) {
        this.Id = Id;
    }

    public int currentId(){
        this.Id = globalId;
        return Pessoa.globalId++;
    }

    @Override
    public String toString() {
        return "Nome: " + name + " Telefone: " + phoneNumber + " Id: " + Id;
    }
   
}
