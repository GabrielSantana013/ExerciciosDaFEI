/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package lab06exe03;

/**
 *
 * @author unifgdias
 */
public class MovableCircle implements Movable{
    
    private int radius;
    private MovablePoint center;

    public MovableCircle(int radius, MovablePoint center) {
        this.radius = radius;
        this.center = center;
    }

    public int getRadius() {
        return radius;
    }

    public void setRadius(int radius) {
        this.radius = radius;
    }

    public MovablePoint getCenter() {
        return center;
    }

    public void setCenter(MovablePoint center) {
        this.center = center;
    }

    
    @Override
    public void moveUp() {
        this.center.moveUp();
    }

    @Override
    public void moveDown() {
        this.center.moveDown();
    }

    @Override
    public void moveLeft() {
        this.center.moveLeft();
    }

    @Override
    public void moveRight() {
        this.center.moveRight();
    }

    @Override
    public String toString() {
        return "\nRadius - " + this.radius +
               "\n MovablePoint - " + this.center.toString();
    }
    
}
