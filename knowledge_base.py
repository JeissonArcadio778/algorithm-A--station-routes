# Definición de la base de conocimiento en reglas lógicas

knowledge_base = {
    "conexiones": {
        "X": [("Y", 4), ("Z", 2)],
        "Y": [("W", 3)],
        "Z": [("W", 5), ("V", 7)],
        "W": [("T", 6)],
        "V": [("T", 4)],
        "T": []
    }
}
