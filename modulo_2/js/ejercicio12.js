let opcionMenu = "guardar"

switch (opcionMenu.toUpperCase()){
    case "INICIAR":
        console.log ("El juego ha comenzado!");
        break
    case "GUARDAR " : 
        console.log ("Partida guardada correctamente .");
        break
    case "SALIR" : 
        console.log ("Hasta luego.");
        break
    default :
        console.log ("Opcion invalida.");
        break
}
