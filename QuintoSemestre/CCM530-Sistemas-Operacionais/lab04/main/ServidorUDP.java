/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package main;

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.time.LocalTime;

/**
 *
 * @author unifgdias
 */
public class ServidorUDP {
    public static void main(String[] args) {
        
        System.out.println("Servidor UDP Online");
        DatagramSocket socket = null;
        LocalTime horaAtual = LocalTime.now();
                
        try{
        
            socket = new DatagramSocket(7890);
            
            while(true){
                byte[] buffer = new byte[1000];
                DatagramPacket msg = new DatagramPacket(buffer, buffer.length);
                socket.receive(msg);
                System.out.println("Recebido em: " + horaAtual);
                System.out.println(new String(msg.getData()));                
                String nova_resposta = "Resultado: " + calc(new String(msg.getData()));
                System.out.println(nova_resposta);
                DatagramPacket resposta = new DatagramPacket(
                        nova_resposta.getBytes(),
                        nova_resposta.length(),
                        msg.getAddress(),
                        msg.getPort());
                    socket.send(resposta);
                    System.out.println("Resposta enviada para: " + msg.getAddress().toString() + "\n");
                    
            }
            
        }catch(IOException e){
            System.out.println("Error: " + e.getMessage());
        }
        socket.close();
    }
    
    
    public static Double calc(String exp){
        String[]exp2 = (exp.split(":"));
        Double n1 = Double.parseDouble(exp2[1]);
        Double n2 = Double.parseDouble(exp2[2]);
        
        switch(exp2[0]){
            
            case "soma":
                return n1+n2;
            case "sub":
                return n1-n2;
            case "mult":
                return n1*n2;
            case "div":
                return n1/n2;
            
        }
        return null;
    }
    
    
}
