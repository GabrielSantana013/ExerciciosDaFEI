class FuncionariosDoHospital{
    construtor(nome){
        this._nome = nome;
        this._numeroRestantesDeFerias = 20;
    }

    get nome(){
        return this._nome;
    }

    set nome(nome){
        this._nome = nome;
    }

    get numeroRestantesDeFerias(){
        return this._numeroRestantesDeFerias;
    }

    set numeroRestantesDeFerias(numeroRestantesDeFerias){
        this._numeroRestantesDeFerias = numeroRestantesDeFerias;
    }

    tirarFerias(numDias){
        if(numDias > this._numeroRestantesDeFerias){
            console.log("Número solicitado maior do que o disponível");
        }
        else{
            this._numeroRestantesDeFerias -= numDias;
            console.log(this._nome + "tirou" + numDias + " de férias");
        }
    }
}

class Medico extends FuncionariosDoHospital{
    constructor(nome, cpf){
        super(nome);
        this._cpf = cpf;
    }
}

class Enfermeira extends FuncionariosDoHospital{
    constructor(nome){
        super(nome);
        this._certificados = [];
    }

    adicionarCertificado(ceritficado){
        this._certificados.push(ceritficado);
    }
}

var medico = new Medico("nome", "123123123");
var enfermeira = new Enfermeira("sei la2");

console.log(medico);
medico.tirarFerias(10);
console.log(medico);

console.log(enfermeira);
enfermeira.tirarFerias(30);
enfermeira.adicionarCertificado("Teste 1")
console.log(enfermeira);