/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package mathserver;

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
public class ServidorMath {
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
                String nova_resposta = "Teste: " + new String(msg.getData());
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
    
}
