const { useState, useEffect } = React;
 
 function App() {
   const [numero_secreto, setNumero_secreto] = useState(null);
   const [palpite, setPalpite] = useState(0);
   const [mensagem, setMensagem] = useState('');
   const [cor_fundo, setCor_fundo] = useState('#f0f0f0');
 
   useEffect(() => {
      const numero_aleatorio = Math.floor(Math.random() * 100) + 1;
      setNumero_secreto(numero_aleatorio);
    },[]);
   
   const verificar = () =>{  
     console.log(numero_secreto, palpite);
     if(numero_secreto === palpite){       
       setMensagem("Parabéns, número correto!");
       setCor_fundo('lightgreen');
     }
     else if(numero_secreto<palpite){
       setMensagem("Dica: número muito grande!");
       setCor_fundo('orange');
     }
     else{
       setMensagem("Dica: número muito pequeno!");
       setCor_fundo('lightcoral');
     }
   }
   
   return(
      <div>
        <h1>Palpites de 1 a 100</h1>
        <input type = 'number' onChange = {(number) => setPalpite(parseInt(number.target.value))}/>
        <button onClick={verificar}>Clique aqui</button>
       <p style={{ backgroundColor: cor_fundo, padding: '20px', textAlign: 'center' }}>{mensagem}</p>
      </div>
   ); 
};  

ReactDOM.render(<App />, document.getElementById("root"));
