/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package controller;

import DAO.AlunoDAO;
import DAO.Conexao;
import java.sql.Connection;
import java.sql.SQLException;
import javax.swing.JOptionPane;
import model.Aluno;
import view.AltExcFrame;


/**
 *
 * @author unifgdias
 */
public class ControllerUsuario {
    
    private AltExcFrame view;
    private Aluno aluno;

    public ControllerUsuario(AltExcFrame view, Aluno aluno) {
        this.view = view;
        this.aluno = aluno;
    }
    
    public void atualizar(){
        String nome = view.getLbl_nome_alt_esc().getText();
        String usuario = view.getLbl_usuario_alt_esc().getText();
        String senha = view.getTxt_senha_alt_esc().getText();
        
        Aluno aluno = new Aluno(nome, usuario, senha);
        Conexao conexao = new Conexao();
        
        try{
            Connection conn = conexao.getConnection();
            AlunoDAO dao = new AlunoDAO(conn);
            dao.atualizar(aluno);
            JOptionPane.showMessageDialog(view, "Senha Atualizada");
        }catch(SQLException e){
            JOptionPane.showMessageDialog(view, "Erro de conexao");
        }
    }
    
    public void remover(){
        int option = JOptionPane.showConfirmDialog(view, "deseja realmente excluir?");
        
        if(option !=1){
            Conexao conexao = new Conexao();
            try{
                Connection conn = conexao.getConnection();
                AlunoDAO dao = new AlunoDAO(conn);
                dao.remover(aluno);
                JOptionPane.showMessageDialog(view, "Usuario Excluido");
            }catch(SQLException e){
                JOptionPane.showMessageDialog(view, "Erro de conexao");
            }
        }
        
    }    
}
