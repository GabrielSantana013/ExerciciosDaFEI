import { StyleSheet, Text, View, Button, TextInput, Image} from 'react-native';
import React from "react";
import {Audio} from 'expo-av';



class App extends React.Component {
    constructor(props){
      super(props);
      this.som = new Audio.Sound();
      this.som.loadAsync(require('./assets/musga2.mp3'));
      this.state={
        data: new Date(),
        horaDespertar: undefined,
        minutoDespertar: undefined, 
      }

      this.controle = false;
      this.som.setPositionAsync(0);
    }

  atualizarHora(){
    this.setState({data: new Date()})
  }

  componentDidMount(){
    setInterval(()=>{this.atualizarHora(),this.tocar()}, 1000);
  }

  tocar(){
    if(this.state.data.getHours() === this.state.horaDespertar &&
     this.state.data.getMinutes() === this.state.minutoDespertar){
      this.som.playAsync();
      this.controle = true;
    }
    else{
      this.controle = false;
      this.som.stopAsync();
    }
  }

    
  render(){
    return(
      <View style={styles.container}>
  {this.controle ? (
    <Image style={styles.imagem} source={require("./assets/cuphead-meme.gif")} />
  ) : (
    <View>
      <Text style={styles.titulo}>⏰ Despertador</Text>

      <Text style={styles.label}>Hora</Text>
      <TextInput
        style={styles.input}
        onChangeText={(text) => this.setState({ horaDespertar: parseInt(text) || null })}
        keyboardType="numeric"
      />

      <Text style={styles.label}>Minuto</Text>
      <TextInput
        style={styles.input}
        onChangeText={(text) => this.setState({ minutoDespertar: parseInt(text) || null })}
        keyboardType="numeric"
      />

      <Text style={styles.horaAtual}>{this.state.data.toLocaleTimeString('pt-br')}</Text>
      <Text style={styles.horaAtual}>{this.state.data.toLocaleDateString('pt-br')}</Text>
    </View>
  )}
</View>

    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#1e1e2f',
    alignItems: 'center',
    justifyContent: 'center',
    padding: 20,
  },
  titulo: {
    fontSize: 24,
    color: '#ffffff',
    marginBottom: 20,
    fontWeight: 'bold',
  },
  label: {
    fontSize: 18,
    color: '#cccccc',
    marginTop: 10,
  },
  input: {
    height: 40,
    width: 100,
    borderColor: '#888',
    borderWidth: 1,
    borderRadius: 8,
    backgroundColor: '#fff',
    paddingHorizontal: 10,
    marginTop: 5,
    textAlign: 'center',
  },
  horaAtual: {
    fontSize: 20,
    color: '#00ffcc',
    marginTop: 20,
  },
  imagem: {
    width: 300,
    height: 300,
    resizeMode: 'contain',
    alignSelf: 'center',
    marginTop: 20,
  },
});



export default App;
