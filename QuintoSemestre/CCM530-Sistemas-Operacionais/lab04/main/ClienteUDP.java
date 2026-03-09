/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package main;
import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;


/**
 *
 * @author unifgdias
 */
public class ClienteUDP {
    public static void main(String[] args) {
        System.out.println("Cliente UDP");
        DatagramSocket socket = null;
        
        try{
            String mensagem = "div:10:15";
            byte[] m = mensagem.getBytes();
            int tamanho = mensagem.length();
            int porta = 7890;
            for(int i = 100; i < 130; i++){
            
            InetAddress endereco = InetAddress.getByName(String.format("localhost", i));         
            DatagramPacket pacoteMensagem = new DatagramPacket(m, tamanho, 
                    endereco, porta);
            socket = new DatagramSocket();
            socket.send(pacoteMensagem);
            
            byte[] buffer = new byte[1000];
            DatagramPacket resposta = new DatagramPacket(buffer, buffer.length);
            
            socket.receive(resposta);
                System.out.println("resposta do servidor: " + new String(resposta.getData()));                            
            }
            
        }catch(IOException e){
            System.out.println("Error: " + e.getMessage());
        }
    }
    
}
