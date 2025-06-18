import nltk
from nltk.tokenize import word_tokenize

# Diccionario con los 5 documentos 
documentos = {
    "doc1": "La inteligencia artificial está revolucionando la tecnología",
    "doc2": "El aprendizaje automático es clave en la inteligencia artificial",
    "doc3": "Procesamiento del lenguaje natural y redes neuronales",
    "doc4": "Las redes neuronales son fundamentales en deep learning",
    "doc5": "El futuro de la IA está en el aprendizaje profundo"}

# Creamos el índice invertido (diccionario que guarda en qué doc está cada palabra)
indice = {}

# Tokenizamos y limpiamos cada documento
for nombre, texto in documentos.items():
    texto = texto.lower()
    tokens = word_tokenize(texto)
    for palabra in tokens:
        if palabra.isalpha(): 
            if palabra not in indice:
                indice[palabra] = {nombre}
            else:
                indice[palabra].add(nombre)

# Bucle para que el usuario ingrese consultas 
while True:
    consulta = input("Ingrese una consulta booleana (o 'salir' para terminar): ").lower()
    
    if consulta == "salir":
        break
    elif " and " in consulta:
        t1, t2 = consulta.split(" and ")
        docs = indice.get(t1, set()) & indice.get(t2, set())
        print(" Documentos encontrados:", docs)
    elif " or " in consulta:
        t1, t2 = consulta.split(" or ")
        docs = indice.get(t1, set()) | indice.get(t2, set())
        print(" Documentos encontrados:", docs)
    elif " not " in consulta:
        t1, t2 = consulta.split(" not ")
        docs = indice.get(t1, set()) - indice.get(t2, set())
        print(" Documentos encontrados:", docs)
    else: #los errores siempre afuera
        print("Consulta no reconocida. Usá 'AND', 'OR' o 'NOT'")
