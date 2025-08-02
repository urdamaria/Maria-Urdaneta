const secreto = 8; 
let intento = 0;

console.log ( `El numero secreto es ${secreto}.`)
while (intento !== secreto){
    intento= Math.floor (Math.random()*10) + 1;
    console.log (`Es el ${intento}?`)
}
console.log (`El numero secreto era ${secreto}`)