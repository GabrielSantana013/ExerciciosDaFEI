import React from "react";
import ReactDOM from 'react-dom/client';

/*function Welcome(){
    return React.createElement(
        "div", //tag
        {style: {color:'red'}}, //estilo
        "Olá Mundo!" //conteúdo da tab
    );
}*/

/*ReactDOM.render(
    React.createElement(Welcome),
    document.getElementById('root')
);*/


//pratica 1

class Componente1 extends React.Component{
    render(){
        const style ={
            backgroundColor:"#61dafb",
            fontFamily: "Arial"
        };        
        return(
            <section style = {style}>
                <h1>Computação Móvel</h1>
                <h1>React</h1>
                <h2>Biblioteca Javascript para criar UI</h2>
                <p>Aula um</p>
            </section>
        );
    }
}

function Componente2(){
    const style = {
        backgroundColor: "green",
        padding: "20px",
        fontFamily: "Verdana"
    };

     return React.createElement(
        'section',
        { style: style },
        React.createElement('h1', null, 'Vamos utilizar:'),
        React.createElement('ul', null,
        React.createElement('li', null, 'HTML'),
        React.createElement('li', null, 'CSS'),
        React.createElement('li', null, 'JavaScript')
        )
  );
}

class App extends React.Component{
    render(){
        return(
            <div>
                <Componente1/>
                <Componente2/>
            </div>
        );
    }
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(React.createElement(App))
