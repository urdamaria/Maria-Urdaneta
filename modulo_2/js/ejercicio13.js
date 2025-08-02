let mes = "octubre"

switch (mes.toLowerCase()){
    case "diciembre":
    case "enero":
    case "febrero":
        console.log (`${mes} es invierno`);
        break;
    case "marzo":
    case "abril":
    case "mayo":
        console.log (`${mes} es primavera`);
        break;
    case "junio":
    case "julio":
    case "agosto":
        console.log (`${mes} es verano`);
        break;
    case "septiembre":
    case "octubre":
    case "noviembre":
        console.log (`${mes} es otoño`);
        break;
    default:
        console.log ("Aprendete los meses bobo");
        break;
}