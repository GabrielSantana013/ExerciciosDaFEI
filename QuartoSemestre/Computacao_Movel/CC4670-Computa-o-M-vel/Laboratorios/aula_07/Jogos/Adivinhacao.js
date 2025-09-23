import React, { useState, useEffect } from 'react';
import { View, Text, TextInput, Button, StyleSheet } from 'react-native';

export default function Adivinhacao({ navigation }) {
  const [numero_secreto, setNumero_secreto] = useState(null);
  const [palpite, setPalpite] = useState('0');
  const [mensagem, setMensagem] = useState('');
  const [cor_fundo, setCor_fundo] = useState('#f0f0f0');
  const [numero_tentativas, setNumero_tentativas] = useState(0);

  useEffect(() => {
    const numero_aleatorio = Math.floor(Math.random() * 100) + 1;
    setNumero_secreto(numero_aleatorio);
  }, []);

  const verificar = () => {
    const numeroConvertido = parseInt(palpite);
    if (isNaN(numeroConvertido)) {
      setMensagem("Digite um número válido!");
      setCor_fundo('red');
      return;
    }

    if (numero_secreto === numeroConvertido) {
      setMensagem("Parabéns, número correto!");
      setCor_fundo('lightgreen');
    } else if (numero_secreto < numeroConvertido) {
      setMensagem("Dica: número muito grande!");
      setCor_fundo('orange');
    } else {
      setMensagem("Dica: número muito pequeno!");
      setCor_fundo('lightcoral');
    }
    setNumero_tentativas(prev => prev + 1);
  };

  return (
    <View style={[styles.container, { backgroundColor: cor_fundo }]}>
      <Text>Jogo de adivinhação!</Text>
      <TextInput
        style={styles.caixa}
        value={String(palpite)}
        onChangeText={(text) => setPalpite(text)}
        placeholder="Número Secreto"
        keyboardType="numeric"
      />
      <Text>Número secreto: {numero_secreto}</Text>
      <View style={styles.botao}>
        <Button title="Palpite" onPress={verificar} />
      </View>
      <Text style={styles.mensagem}>{mensagem}</Text>
      <Text style={styles.mensagem}>Número de tentativas: {numero_tentativas}</Text>
      <Button title="Voltar" onPress={() => navigation.goBack()} />
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, justifyContent: 'center', alignItems: 'center' },
  caixa: { borderWidth: 1, padding: 10, width: 200, marginBottom: 10 },
  botao: { marginVertical: 10 },
  mensagem: { fontSize: 16, marginTop: 10 }
});
