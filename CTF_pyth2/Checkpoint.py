import time
import os
import pickle

CHECKPOINT_FILE = "scraper_checkpoint.pkl"

# Lista de páginas web a extraer
PAGINAS_OBJETIVO = [
    "https://tienda.com/producto-1",
    "https://tienda.com/producto-2",
    "https://tienda.com/producto-3",
    "https://tienda.com/producto-4",
    "https://tienda.com/producto-5",
    "https://tienda.com/producto-6",
    "https://tienda.com/producto-7",
    "https://tienda.com/producto-8"
]


def guardar_checkpoint(estado):
    """Guarda el progreso actual."""
    with open(CHECKPOINT_FILE, "wb") as archivo:
        pickle.dump(estado, archivo)

    print(
        f"[Checkpoint guardado: "
        f"{len(estado['completadas'])} completadas / "
        f"{len(estado['pendientes'])} pendientes]"
    )


def cargar_checkpoint():
    """Recupera el progreso anterior si existe."""
    if os.path.exists(CHECKPOINT_FILE):
        with open(CHECKPOINT_FILE, "rb") as archivo:
            estado = pickle.load(archivo)

        print("--> Checkpoint detectado. Restaurando progreso...")
        print(f"--> Páginas completadas: {len(estado['completadas'])}")
        print(f"--> Páginas pendientes: {len(estado['pendientes'])}\n")

        return estado

    print("--> No existe un checkpoint. Iniciando desde cero...\n")

    return {
        "pendientes": list(PAGINAS_OBJETIVO),
        "completadas": [],
        "datos_extraidos": []
    }


def simular_peticion_web(url):
    """Simula la extracción de información de una página."""
    time.sleep(2)

    id_producto = url.split("-")[-1]

    return {
        "url": url,
        "titulo": f"Producto Ejemplo #{id_producto}",
        "precio": f"${float(id_producto) * 15.50:.2f}"
    }


def main():
    estado = cargar_checkpoint()

    print("--- INICIANDO PROCESO DE SCRAPING ---\n")

    while estado["pendientes"]:
        url_actual = estado["pendientes"][0]

        print(f"Extrayendo datos de: {url_actual}...")

        datos = simular_peticion_web(url_actual)

        estado["datos_extraidos"].append(datos)
        estado["completadas"].append(url_actual)
        estado["pendientes"].pop(0)

        # Guardar el progreso después de cada página
        guardar_checkpoint(estado)

        # Simular una caída automática al completar 3 páginas
        if len(estado["completadas"]) == 3:
            print("\n[!] SIMULACIÓN DE FALLO AUTOMÁTICO")
            print("El programa se detuvo después de completar 3 páginas.")
            print("Presiona RUN nuevamente para reanudar el proceso.\n")
            return

    print("\n--- SCRAPING COMPLETADO CON ÉXITO ---")
    print("\nDatos recolectados:")

    for item in estado["datos_extraidos"]:
        print(
            f"- {item['titulo']} -> {item['precio']} "
            f"({item['url']})"
        )

    # Eliminar el checkpoint cuando todo termina correctamente
    if os.path.exists(CHECKPOINT_FILE):
        os.remove(CHECKPOINT_FILE)
        print("\nCheckpoint eliminado. Proceso finalizado.")


if __name__ == "__main__":
    main()