'''
Script para procesar los datos de las encuestas desde csv a json, para
despues ser procesadas y mostradas en el manual
'''

import csv
import json

# Procesar csv de la encuesta
with open("encuesta.csv", "r", encoding="utf8", newline='') as encuesta_csv:
    encuesta = csv.reader(encuesta_csv)

    respuestas = []
    for fila in encuesta:
        # Remover columnas innecesarias
        fila.pop(0)
        respuestas.append([i for i in fila if i != ''])

    respuestas.pop(0)

# Procesar respuestas a un diccionario
data = {}
for respuesta in respuestas:
    ramo = respuesta[0][-8:-1]

    if not ramo in data:
        data[ramo] = {
            "respuestas": 0,
            "total_dificultad": 0,
            "dificultad": 0,
            "comentarios": [],
        }

    data[ramo]["respuestas"] += 1
    data[ramo]["total_dificultad"] += int(respuesta[1])

    if respuesta[2] in data[ramo]["comentarios"]:
        continue

    data[ramo]["comentarios"].append(respuesta[2])

# Calcular dificultad promedia de cada asignatura
for ramo, resultados in data.items():
    dificultad: int = round(resultados["total_dificultad"] / resultados["respuestas"])
    resultados["dificultad"] = dificultad
    resultados.pop("total_dificultad")

# Guardar resultados en json
with open("resultados.json", "w", encoding="utf8") as resultados_json:
    json.dump(data, resultados_json, ensure_ascii=False, indent="\t")
