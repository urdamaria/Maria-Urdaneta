let mes = "octubre"

switch (mes.toLowerCase()){
    case "diciembre":
    case "enero":
    case "febrero":
        console.log ('Este mes es de invierno');
        break;
    case "marzo":
    case "abril":
    case "mayo":
        console.log ('Este mes es de primavera');
        break;
    case "junio":
    case "julio":
    case "agosto":
        console.log ('Este mes es de verano');
        break;
    case "septiembre":
    case "octubre":
    case "noviembre":
        console.log ('Este mes es de otoño');
        break;
    default:
        console.log ("Aprendete los meses bobo");
        break;
}