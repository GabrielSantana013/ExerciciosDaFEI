/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package controller;

import DAO.AlunoDAO;
import DAO.Conexao;
import java.sql.Connection;
import model.Aluno;
import view.LoginFrame;
import java.sql.SQLException;
import java.sql.ResultSet;
import javax.swing.JOptionPane;
import view.AltExcFrame;

/**
 *
 * @author unifgdias
 */
public class ControllerLogin {

    private LoginFrame view;

    public ControllerLogin(LoginFrame view) {
        this.view = view;
    }

    public void loginAluno(){
    
        Aluno aluno = new Aluno(null,
        view.getTxt_usuario_login().getText(),
        view.getTxt_senha_login().getText());
      
        Conexao conexao = new Conexao();
        
        try{
        
            Connection conn = conexao.getConnection();
            AlunoDAO dao = new AlunoDAO(conn);
            ResultSet res = dao.consultar(aluno);
            if(res.next()){
                JOptionPane.showMessageDialog(view,
                                            "Login Efetuado",
                                            "Aviso",
                                            JOptionPane.INFORMATION_MESSAGE);
                String nome = res.getString("nome");
                String usuario = res.getString("usuario");
                String senha = res.getString("senha");
                Aluno aluno2 = new Aluno(nome, usuario, senha);
                AltExcFrame aec = new AltExcFrame(aluno2);
                aec.setVisible(true);
                view.setVisible(false);
            }
            else{
            JOptionPane.showMessageDialog(view,
                                          "Login NÃO efetuado",
                                          "Aviso",
                                          JOptionPane.ERROR_MESSAGE);
                
            }
        }catch(SQLException e){
            
            JOptionPane.showMessageDialog(view,
                                        "Erro de Conexao",
                                        "Aviso",
                                        JOptionPane.ERROR_MESSAGE);
        
        }
        
    }
    
}
