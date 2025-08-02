let nombreUsuario = prompt ("Hola, cual es tu nombre?");
let anioNacimiento = prompt ("En que año naciste?");

let anioActual = 2025;
let edadAproximada = anioActual - Number (anioNacimiento);

console.log ("Hola," + nombreUsuario + "tienes aproximadamente" + edadAproximada + "años.");