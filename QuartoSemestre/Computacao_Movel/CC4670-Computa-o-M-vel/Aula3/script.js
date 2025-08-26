/*

Crie um componente Card que receba as seguintes props:
● nome
● idade
● profissão
Crie um componente App que que renderize pelo menos 3 Cards com 
conteudos diferentes para os props do Card
*/

/*
function Card(props){
  return (
    <h1>Olá {props.name}, você tem {props.age} e trabalha como {props.job}</h1>
  );
}


function App(){
  return(
    <div>
      <Card name="Cleito" age="20" job="Pedreiro"/>
    </div>
  );
}


ReactDOM.render(
  <App />, document.getElementById('root'));*/


/*Crie uma aplicação React Web e no componente principal App faça: 
● Renderize dois botões. O primeiro mostrando o rótulo "Oi" e 
o segundo mostrando o rótulo "Tchau".
● Vincule ao primeiro botão um método que faz o alerta do 
texto: "Oi"
● Vincule ao segundo botão um método que faz o alerta do 
texto: "Tchau*/

/*
class App extends React.Component {
  constructor(props) {
	  super(props);    
  }
  
  Oi = () =>{
	  alert("Ola");
  }
  
  Tchau = ()=>{
	  alert("Tchau");
  }
 
  render() {
	  return (
      <div>
	    <button onClick={this.Oi}>Ola</button>
      <button onClick={this.Tchau}>Tchau</button>
      </div>
	  );
   
  }
};


ReactDOM.render(<App />, document.getElementById('root'));
*/

/*
Crie uma aplicação React Web com Programação Orientado a Objetos: 
● Receba dois valores numéricos.
● Crie 4 botões para soma, subtração, multiplicação e divisão.
● Realize o cálculo apresentando a resposta referente a 
operação escolhida, exemplo:
○ A soma de 23 + 57 = 80
*/                
class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      num1: 0,
      num2: 0
    };
  }

  handleChangeNum1 = (event) => {
    this.setState({ num1: Number(event.target.value) });
  };

  handleChangeNum2 = (event) => {
    this.setState({ num2: Number(event.target.value) });
  };

  Soma = () => {
    const { num1, num2 } = this.state;
    alert(`A soma de ${num1} + ${num2} = ${num1 + num2}`);
  };

  Subtracao = () => {
    const { num1, num2 } = this.state;
    alert(`A subtração de ${num1} - ${num2} = ${num1 - num2}`);
  };

  Multiplicacao = () => {
    const { num1, num2 } = this.state;
    alert(`A multiplicação de ${num1} × ${num2} = ${num1 * num2}`);
  };

  Divisao = () => {
    const { num1, num2 } = this.state;
    if (num2 === 0) {
      alert("Não é possível dividir por zero!");
    } else {
      alert(`A divisão de ${num1} ÷ ${num2} = ${num1 / num2}`);
    }
  };

  render() {
    return (
      <div>
        <h1>Digite seus números:</h1>
        <input type="number" onChange={this.handleChangeNum1} />
        <input type="number" onChange={this.handleChangeNum2} />
        <br /><br />
        <button onClick={this.Soma}>Soma</button>
        <button onClick={this.Subtracao}>Subtração</button>
        <button onClick={this.Multiplicacao}>Multiplicação</button>
        <button onClick={this.Divisao}>Divisão</button>
      </div>
    );
  }
}

ReactDOM.render(<App />, document.getElementById('root'));

        
 
 