import {  Text, TextInput, Button, View, StyleSheet, Alert} from 'react-native';
import React, {useState, useEffect} from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import Adivinhacao from './Jogos/Adivinhacao';
import PPT from './Jogos/PPT';
import Home from './Screens/Home';


const Stack = createStackNavigator();

export default function App(){
  return(
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Home">
        <Stack.Screen name = "Home" component = {Home}/>
        <Stack.Screen name = "Adivinhacao" component = {Adivinhacao}/>
        <Stack.Screen name = "PPT" component = {PPT}/>
      </Stack.Navigator>
    </NavigationContainer>

  );
}

