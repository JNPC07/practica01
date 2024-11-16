dicc = {
            "VEHEMENTE": "Obra de forma irreflexiva, dejándose llevar por los impulsos.",
            "IMPERICIA": "Falta de pericia. inexperiencia, ineptitud, inepcia, incapacidad.",
            "TUMULTO": "Motín, confusión, alboroto producido por una multitud.",
            "LOL" : "Una respuesta a algo gracioso", 
            "CRINGE" : "Algo raro o embarazoso",
            "ROFL" : "Una respuesta a una broma",
            "SHEESH" : "Ligera desaprobación",
            "CREEPY" : "Aterrador, siniestro",
            "AGGRO" : "Ponerse agresivo/enojado"
            }

word = input("Ingresa la palabra que desees aclarar")

if word in dicc.keys():
    print(dicc[word])

else: 
    print("No disponemos ese significado")
