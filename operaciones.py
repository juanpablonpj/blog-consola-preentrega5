# ==========================================
# Operaciones del blog (listar, buscar, filtrar)
# ==========================================

def listar_posts(lista):
    """Recorre y muestra título, autor y estado de los posts con datos básicos válidos."""
    print("\nPosts disponibles:")
    contador = 0

    for post in lista:
        if isinstance(post, dict) and "titulo" in post and isinstance(post.get("autor"), dict):
            nombre_autor = post["autor"].get("nombre", "Desconocido")
            estado = post.get("estado", "sin estado")
            print(f"- {post['titulo']} | Autor: {nombre_autor} | Estado: {estado}")
            contador += 1

    if contador == 0:
        print("No hay publicaciones válidas para mostrar.")


def buscar_por_titulo(lista, termino):
    """Busca y muestra publicaciones cuyo título contenga el término (insensible a mayúsculas/minúsculas)."""
    termino_limpio = termino.strip().lower()

    if not termino_limpio:
        print("\n[Aviso]: El término de búsqueda no puede estar vacío.")
        return

    print(f"\nResultados de búsqueda para '{termino}':")
    encontrados = False

    for post in lista:
        if isinstance(post, dict) and "titulo" in post:
            if termino_limpio in post["titulo"].lower():
                print(f"- {post['titulo']}")
                encontrados = True

    if not encontrados:
        print("No se encontraron publicaciones con ese título.")


def filtrar_por_tag(lista, tag):
    """Filtra y muestra publicaciones que contengan el tag indicado (insensible a mayúsculas/minúsculas)."""
    tag_limpio = tag.strip().lower()

    if not tag_limpio:
        print("\n[Aviso]: El tag de búsqueda no puede estar vacío.")
        return

    print(f"\nPosts con el tag '{tag}':")
    encontrados = False

    for post in lista:
        if isinstance(post, dict) and isinstance(post.get("tags"), list):
            tags_minusculas = [t.lower() for t in post["tags"] if isinstance(t, str)]
            if tag_limpio in tags_minusculas:
                print(f"- {post['titulo']}")
                encontrados = True

    if not encontrados:
        print("No se encontraron publicaciones con ese tag.")