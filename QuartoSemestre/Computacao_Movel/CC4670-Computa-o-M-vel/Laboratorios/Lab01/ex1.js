class VideoGame{

    constructor(marca, nControles, tipoMidia, ligado){
        this._marca = marca;
        this._nControles = nControles;
        this._tipoMidia = tipoMidia;
        this._ligado = ligado;
    }

    get marca(){
        return this._marca;
    }

    set marca(marca){
        this._marca = marca;
    }

    get nControles(){
        return this._nControles;
    }

    set nControles(nControles){
        this._nControles = nControles;
    }

    get tipoMidia(){
        return this._tipoMidia;
    }

    set tipoMidia(tipoMidia){
        this._tipoMidia = tipoMidia;
    }

    get ligado(){
        return this._ligado;
    }

    set ligado(ligado){
        this._ligado = ligado;
    }

    jogar(){
        if(this.ligado){
            console.log("Jogo iniciado");
        }else{
            console.log("Video game desligado!");
        }
    }

    ligar(ligado){
        this._ligado = ligado;
    }

    salvar(){
        if(this._ligado){
            console.log("Jogo salvo");
        }else{
            console.log("Video game desligado!");
        }
    }

}

var playstation = new VideoGame('sony', '2', 'dvd', false);
console.log(playstation);
playstation.jogar();
playstation.ligar(true);
playstation.jogar();
playstation.salvar();
playstation.ligar(false);