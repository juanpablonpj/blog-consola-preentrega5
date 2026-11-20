# ==========================================
# Menú e interacción por consola
# ==========================================

def mostrar_menu():
    """Muestra el menú en consola, captura de forma segura la opción elegida y la retorna."""
    print("\n--- MENU DEL BLOG ---")
    print("1. Ver todos los posts")
    print("2. Buscar por titulo")
    print("3. Filtrar por tag")
    print("4. Validar posts")
    print("5. Salir")

    try:
        opcion = int(input("Elige una opción (1-5): "))
        return opcion
    except ValueError:
        print("\n[Error]: Por favor, ingresa un número válido.")
        return None
