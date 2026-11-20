# ==========================================
# Reglas de validación del blog
# ==========================================

ESTADOS_POR_DEFECTO = ("borrador", "publicado", "archivado")


def validar_post(post, estados_validos=ESTADOS_POR_DEFECTO):
    """Valida la estructura de un post. Retorna True si es válido o un string con el error."""
    if not isinstance(post, dict):
        return "error - el post no es un diccionario válido"

    claves_obligatorias = ["id", "titulo", "contenido", "autor", "tags", "estado"]
    for clave in claves_obligatorias:
        if clave not in post:
            return f'error - falta la clave "{clave}"'

    if not isinstance(post["titulo"], str) or not post["titulo"].strip():
        return 'error - el campo "titulo" está vacío o no es texto'

    if not isinstance(post["contenido"], str) or not post["contenido"].strip():
        return 'error - el campo "contenido" está vacío o no es texto'

    if not isinstance(post["autor"], dict):
        return 'error - el campo "autor" debe ser un diccionario'

    if "nombre" not in post["autor"] or not str(post["autor"]["nombre"]).strip():
        return 'error - el diccionario de autor no contiene la clave "nombre"'

    if not isinstance(post["tags"], list):
        return 'error - el campo "tags" debe ser una lista'

    if post["estado"] not in estados_validos:
        return f'error - el estado "{post["estado"]}" no es válido'

    return True
