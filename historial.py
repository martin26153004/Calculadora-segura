"""Almacenamiento y presentación del historial."""

HISTORIAL = []


def registrar_operacion(operacion, argumentos, resultado=None, error=None):
    entrada = {
        "operacion": operacion,
        "argumentos": argumentos,
        "resultado": resultado,
        "error": error,
        "finalizada": False,
    }
    HISTORIAL.append(entrada)
    return entrada


def mostrar_historial():
    print("\n" + "=" * 40)
    print("HISTORIAL DE OPERACIONES")
    print("=" * 40)

    if not HISTORIAL:
        print("Todavía no hay operaciones registradas.")
        return

    for numero, entrada in enumerate(HISTORIAL, start=1):
        print(f"{numero}. Operación: {entrada['operacion']}")
        print(f"   Argumentos: {entrada['argumentos']}")
        if entrada["error"] is None:
            print(f"   Resultado: {entrada['resultado']}")
            print("   Estado: exitosa")
        else:
            print(f"   Error: {entrada['error']}")
            print("   Estado: fallida")
        print("-" * 40)
