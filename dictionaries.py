"Formas de crear diccionarios para lectura (Erick Ivan Gil Reyes)

nucleotidos = {"A":"Adenina", "C": "Citosina", "G":"Guanina", "T":"Timina"}

print len (nucleotidos)
print nucleotidos

print nucleotidos ["A"] = "ADENINA"
print nucleotidos ["C"] = "CITOCINA"
print nucleotidos ["G"] = "GUANINA"
print nucleotidos ["T"] = "TIMINA"

nucleotidos["A"] = "ADENINA"
print nucleotidos
nucleotidos.pop(´T´, None)
print nucleotidos

