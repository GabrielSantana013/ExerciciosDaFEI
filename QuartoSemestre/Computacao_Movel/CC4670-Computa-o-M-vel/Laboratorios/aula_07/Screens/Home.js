// Home.js
import React from 'react';
import { View, Text, TouchableOpacity, StyleSheet } from 'react-native';

export default function Home({ navigation }) {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>🎮 Bem-vindo aos Mini Jogos</Text>

      <TouchableOpacity
        style={styles.button}
        onPress={() => navigation.navigate('Adivinhacao')}
      >
        <Text style={styles.buttonText}>🔢 Jogo de Adivinhação</Text>
      </TouchableOpacity>

      <TouchableOpacity
        style={styles.button}
        onPress={() => navigation.navigate('PPT')}
      >
        <Text style={styles.buttonText}>🪨 Pedra Papel Tesoura</Text>
      </TouchableOpacity>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#121212',
    alignItems: 'center',
    justifyContent: 'center',
    padding: 20,
  },
  title: {
    fontSize: 28,
    color: '#ffffff',
    marginBottom: 40,
    fontWeight: 'bold',
  },
  button: {
    backgroundColor: '#4e9af1',
    paddingVertical: 15,
    paddingHorizontal: 30,
    borderRadius: 10,
    marginVertical: 10,
    width: '100%',
    alignItems: 'center',
    elevation: 3,
  },
  buttonText: {
    color: '#fff',
    fontSize: 18,
    fontWeight: '600',
  },
});
