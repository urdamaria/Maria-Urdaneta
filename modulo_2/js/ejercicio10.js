let monto = 120;
let precioFinal;

if (montoCompra > 100){
    precioFinal = monto * 0.80;
    console.log ("Felicidades, Tienes un 20% de descuento.");
} else if (montoCompra > 50){
    precioFinal = monto * 0.90;
    console.log ("Tienes un 10% de descuento");
} else {
    precioFinal = monto
    console.log ("No aplica descuento para este monto.");
}

console.log ("El precio final a pagar es:$" + precioFinal)
