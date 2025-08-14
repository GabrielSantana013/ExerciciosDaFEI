/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package DAO;

import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.PreparedStatement;
import model.Aluno;

        
/**
 *
 * @author unifgdias
 */
public class AlunoDAO {
    
    private Connection conn;

    public AlunoDAO(Connection conn) {
        this.conn = conn;
    }
    
    public ResultSet consultar(Aluno aluno) throws SQLException{
    
        String sql = "select * from Aluno where usuario = ? AND senha = ?";        
        PreparedStatement statement = conn.prepareStatement(sql);
        statement.setString(1, aluno.getUsuario());
        statement.setString(2, aluno.getSenha());
        statement.execute();        
        ResultSet resultado = statement.getResultSet();
        return resultado;
    }
    
    public void inserir(Aluno aluno)throws SQLException{
        String sql = "insert into aluno (nome, usuario, senha) values ('"
                + aluno.getNome() +"','"
                + aluno.getUsuario() +"','"
                + aluno.getSenha() +"')";
        PreparedStatement statement = conn.prepareStatement(sql);
        statement.execute();
        conn.close();
    
    }
    
    public void atualizar(Aluno aluno)throws SQLException{        
        String sql = "update aluno set senha = ? where usuario = ?";                
        PreparedStatement statement = conn.prepareStatement(sql);
        statement.setString(1, aluno.getSenha());
        statement.setString(2, aluno.getUsuario());
        statement.execute();
        conn.close();
    
    }
    
    public void remover(Aluno aluno) throws SQLException{    
        String sql = "delete from aluno where usuario = ?";                
        PreparedStatement statement = conn.prepareStatement(sql);        
        statement.setString(1, aluno.getUsuario());
        statement.execute();
        conn.close();
    }
}
