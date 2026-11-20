# ==========================================
# Estructuras de datos base del blog
# ==========================================

perfil_autor = {
    "nombre": "Aline Npj",
    "bio": "Diseñadora de espacios elegantes y funcionales, apasionada por la luz natural y el diseño sustentable.",
    "especialidad": "Decoración de Interiores Profesional",
    "redes_sociales": ["@aline.interiores", "@aline_npj_design"]
}

estados_post = ("borrador", "publicado", "archivado")

etiquetas_blog = {"Diseño", "Decoración", "Interiores", "Tendencias"}

posts = [
    {
        "id": 1,
        "titulo": "Claves para aprovechar la luz natural en el hogar",
        "contenido": "Descubre cómo maximizar la entrada de luz natural para transformar cualquier espacio.",
        "autor": perfil_autor,
        "tags": ["Decoración", "Luz Natural", "Interiores"],
        "estado": "publicado"
    },
    {
        "id": 2,
        "titulo": "Paletas de colores neutros para dormitorios relajantes",
        "contenido": "Los tonos neutros ayudan a crear ambientes de paz y descanso profundo.",
        "autor": perfil_autor,
        "tags": ["Diseño", "Colores", "Tendencias"],
        "estado": "borrador"
    },
    {
        "id": 3,
        "titulo": "Cómo elegir el mobiliario perfecto para espacios reducidos",
        "contenido": "Consejos prácticos para optimizar cada metro cuadrado sin perder estilo.",
        "autor": perfil_autor,
        "tags": ["Decoración", "Mobiliario"],
        "estado": "archivado"
    },
    {
        "id": 4,
        "titulo": "",
        "autor": "Texto incorrecto en vez de diccionario",
        "tags": "No es una lista",
        "estado": "estado_invalido"
    }
]