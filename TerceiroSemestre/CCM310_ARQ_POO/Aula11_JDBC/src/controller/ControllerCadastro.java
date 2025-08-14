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
import view.CadastroFrame;

/**
 *
 * @author unifgdias
 */
public class ControllerCadastro {
    
    private CadastroFrame view;

    public ControllerCadastro(CadastroFrame view) {
        this.view = view;
    }
    
    public void salvarAluno(){
        String nome = view.getTxt_nome_cadastro().getText();
        String usuario = view.getTxt_usuario_cadastro().getText();
        String senha = view.getTxt_senha_cadastro().getText();
        
        Aluno aluno = new Aluno(nome, usuario, senha);        
        
        Conexao conexao = new Conexao();
        try{
            Connection conn = conexao.getConnection();
            AlunoDAO dao = new AlunoDAO(conn);
            dao.inserir(aluno);
            JOptionPane.showMessageDialog(view, "Usuario Cadastrado");
        }catch(SQLException e){
            JOptionPane.showMessageDialog(view, "Erro de conexão");
        }        
    }    
}
