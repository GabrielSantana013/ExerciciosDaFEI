//import React from 'react';
//import ReactDOM from 'react-dom';
//import { useState } from "react"; 
const { useState } = React;
 
 function App() {
   const [count, setCount] = useState(0);

   return (
    <div>
      <p>Você clicou {count} vezes</p>
      <button onClick={() => setCount(count + 1)}>
       Clique aqui
      </button>
    </div>
  );
}

ReactDOM.render(<App />, document.getElementById("root"));




//==========================================================================================



//import React from 'react';
//import ReactDOM from 'react-dom';
//import { useState } from "react"; 
const { useState, useEffect } = React;
 
 function App() {
   const [segundos,setSegundos] = useState(0);
   const [minutos,setMinutos] = useState(0);
   const [horas, setHoras] = useState(0);
   const [ativo, setAtivo] = useState(false);
                                                                
  useEffect(() => {
    let intervalo;

    if (ativo) {
      intervalo = setInterval(() => {
        setSegundos((prevSegundos) => {
          if (prevSegundos + 1 === 60) {
            setMinutos((prevMinutos) => {
              if (prevMinutos + 1 === 60) {
                setHoras((prevHoras) => prevHoras + 1);
                return 0;
              }
              return prevMinutos + 1;
            });
            return 0;
          }
          return prevSegundos + 1;
        });
      }, 1000); // 1 segundo
    } else {
      clearInterval(intervalo);
    }

    return () => clearInterval(intervalo);
  }, [ativo]);

   
   function iniciarCronometro(){
     setAtivo(true);
   }
   
   function pausarCronometro(){
     setAtivo(false);
   }
   
   function zerarCronometro(){
     setAtivo(false);
     setSegundos(0);
     setMinutos(0);
     setHoras(0);
   }
   
    return (
    <div>
      <h1>
        {String(horas).padStart(2, '0')}:
        {String(minutos).padStart(2, '0')}:
        {String(segundos).padStart(2, '0')}
      </h1>
      <button onClick={iniciarCronometro}>Iniciar</button>
      <button onClick={pausarCronometro}>Pausar</button>
      <button onClick={zerarCronometro}>Zerar</button>
    </div>
  );
}   

ReactDOM.render(<App />, document.getElementById("root"));



//=======================================================================================

//versão do professor

//import React from 'react';
//import ReactDOM from 'react-dom';
//import { useState } from "react"; 
const { useState, useEffect } = React;
 
 function App() {
   const [segundos,setSegundos] = useState(0);
   const [ativo, setAtivo] = useState(false);
                                                                
useEffect(() => {
  let intervaloId = null;

  if (ativo) {
    intervaloId = setInterval(() => {
      setSegundos((segundos) => segundos + 1);
    }, 1000);
  }

  return () => {
    if (intervaloId) {
      clearInterval(intervaloId);
    }
  };
}, [ativo]);

   
  const formatTime = (segundos) =>{
    const hours = Math.floor(segundos/3600).toString().padStart(2,'0');
    const minutes = Math.floor((segundos % 3600)/60).toString().padStart(2,'0');
    const seconds = Math.floor(segundos%60).toString().padStart(2,'0');
    return `${hours}:${minutes}:${seconds}`
  }
  
   
   const iniciarCronometro = () =>{
     setAtivo(true);
   }
   
   const pausarCronometro = () =>{
     setAtivo(false);
   }
   
   const zerarCronometro = () =>{
     setAtivo(false);
     setSegundos(0);
   }
   
    return (
    <div>
      <h1>
        <p>{formatTime(segundos)}</p>
      </h1>
      <button onClick={iniciarCronometro}>Iniciar</button>
      <button onClick={pausarCronometro}>Pausar</button>
      <button onClick={zerarCronometro}>Zerar</button>
    </div>
  );
}   

ReactDOM.render(<App />, document.getElementById("root"));