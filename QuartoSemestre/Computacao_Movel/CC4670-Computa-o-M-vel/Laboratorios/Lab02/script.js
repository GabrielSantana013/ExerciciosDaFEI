class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      num1: '',
      acumulado:'',
      operador:'',
      resultado:''
    };
  }

handleDigit = (digit) => {
  this.setState((prevState) => ({
    num1: prevState.num1 + digit
  }));
};

  
handleOperador = (operador) => {
  const { num1 } = this.state;

  if (num1 === '') return; // evita operação sem número

  this.setState({
    acumulado: num1,
    num1: '',
    operador
  });
};
  
Calcular = () => {
  const { acumulado, num1, operador } = this.state;

  if (num1 === '') {
    alert('Operação incompleta');
    return;
  }
  else if(num1 !== '' && acumulado === ''){
    return;    
  }

  const a = Number(acumulado);
  const b = Number(num1);
  let resultado;

  switch (operador) {
    case '+':
      resultado = a + b;
      break;
    case '-':
      resultado = a - b;
      break;
    case '*':
      resultado = a * b;
      break;
    case '/':
      resultado = b === 0 ? 'Erro: divisão por zero' : a / b;
      break;
    default:
      resultado = 'Operador inválido';
  }

  // Se for erro, não atualiza num1
  if (typeof resultado === 'string') {
    this.setState({ resultado });
  } else {
    this.setState({
      num1: resultado.toString(), // resultado vira novo num1
      acumulado: '',
      operador: '',
      resultado: resultado.toString()
    });
  }
};


  render() {
    return (
      <div class ="calculator">
        <h1>Calculadora</h1>
        <input
            type="text"
            value={this.state.num1 || this.state.resultado}
            readOnly
          />
        <br /><br />
        <button onClick={() => this.handleDigit('7')}>7</button>
        <button onClick={() => this.handleDigit('8')}>8</button>
        <button onClick={() => this.handleDigit('9')}>9</button>
        <button onClick={() => this.handleOperador('*')}>*</button>
        <br /><br />
        <button onClick={() => this.handleDigit('4')}>4</button>
        <button onClick={() => this.handleDigit('5')}>5</button>
        <button onClick={() => this.handleDigit('6')}>6</button>
        <button onClick={() => this.handleOperador('/')}>/</button>
        <br /><br />
        <button onClick={() => this.handleDigit('1')}>1</button>
        <button onClick={() => this.handleDigit('2')}>2</button>
        <button onClick={() => this.handleDigit('3')}>3</button>
        <button onClick={() => this.handleOperador('-')}>-</button>
        <br /><br />
        
        <button onClick={() => this.setState({
          num1: '',
          acumulado: '',
          operador: '',
          resultado: ''
        })}>C</button>
        <button onClick={() => this.handleDigit('0')}>0</button>
        <button onClick={this.Calcular}>=</button>
        <button onClick={() => this.handleOperador('+')}>+</button>
      </div>
    );
  }
}

ReactDOM.render(<App />, document.getElementById('root'));