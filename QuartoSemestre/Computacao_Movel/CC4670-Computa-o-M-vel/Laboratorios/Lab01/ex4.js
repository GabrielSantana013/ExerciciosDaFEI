const processarMensagem = (mensagem, callback) => callback(mensagem);

//Juntar as duas strings

const mensagemA = (mensagem) => `Alerta: ${mensagem}`;

console.log(processarMensagem("Sistema em manutenção", mensagemA));

//Retorna tudo em minúscula
const mensagemB = (mensagem) => mensagem.toLowerCase();
console.log(processarMensagem("ALERTA DE SEGURANÇA", mensagemB));


//Retorna a quantidade de caracteres
const mensagemC = (mensagem) => `Saída: Resumo: A mensagem contém ${mensagem.length} caracteres`;
console.log(processarMensagem("ALERTA DE SEGURANÇA", mensagemC));

//Informa se a mensagem é composta somente por maiúscula ou minúscula:

