/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package lab06exe03;

/**
 *
 * @author unifgdias
 */
public class Lab06Exe03 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        
        MovablePoint p1 = new MovablePoint(0,0,0,0);
        p1.moveUp();
        p1.moveUp();
        System.out.println(p1);
        
        MovableCircle mc1 = new MovableCircle(10,p1);
        mc1.moveRight();
        System.out.println(mc1);
        
    }
    
}
