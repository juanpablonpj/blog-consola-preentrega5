# ==========================================
# Punto de entrada del sistema de blog
# ==========================================

from blog.datos import posts, estados_post
from blog.menu import mostrar_menu
from blog.operaciones import listar_posts, buscar_por_titulo, filtrar_por_tag
from blog.validaciones import validar_post


def ejecutar_sistema():
    while True:
        opcion = mostrar_menu()

        if opcion is None:
            continue

        if opcion == 1:
            listar_posts(posts)

        elif opcion == 2:
            termino = input("Buscar por titulo: ")
            buscar_por_titulo(posts, termino)

        elif opcion == 3:
            tag = input("Filtrar por tag: ")
            filtrar_por_tag(posts, tag)

        elif opcion == 4:
            print("\nValidación de posts:")
            for i, post in enumerate(posts, start=1):
                resultado = validar_post(post, estados_post)
                if resultado is True:
                    print(f"Post {i}: válido")
                else:
                    print(f"Post {i}: {resultado}")

        elif opcion == 5:
            print("\nGracias por usar el sistema del blog. ¡Hasta luego!")
            break

        else:
            print("\n[Error]: Opción inválida, por favor elige un número entre 1 y 5.")


if __name__ == "__main__":
    ejecutar_sistema()