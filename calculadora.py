"""Lógica principal de la calculadora segura."""

from operaciones import (
    sumar,
    restar,
    multiplicar,
    dividir,
    promedio,
    convertir_texto_a_numero,
    raiz_cuadrada,
)
from historial import registrar_operacion, mostrar_historial


def obtener_numero(mensaje):
    """Solicita números hasta recibir una entrada válida."""
    while True:
        try:
            texto = input(mensaje)
            return convertir_texto_a_numero(texto)
        except ValueError:
            print("Entrada inválida. Escriba un número, por ejemplo: 8, -3 o 2.5.")
        except EOFError:
            print("No se recibió una entrada. Intente nuevamente.")
        except KeyboardInterrupt:
            print("\nCaptura cancelada. Intente nuevamente o use la opción 9 para salir.")


def calcular(operacion, *args):
    """Ejecuta una operación usando try/except/else/finally."""
    funciones = {
        "sumar": sumar,
        "restar": restar,
        "multiplicar": multiplicar,
        "dividir": dividir,
        "promedio": promedio,
        "raiz_cuadrada": raiz_cuadrada,
    }

    resultado = None
    mensaje_error = None
    entrada_historial = None

    try:
        if operacion not in funciones:
            raise ValueError(f"La operación '{operacion}' no existe.")
        resultado = funciones[operacion](*args)
    except ZeroDivisionError as error:
        mensaje_error = str(error)
        print(f"Error de división: {mensaje_error}")
    except ValueError as error:
        mensaje_error = str(error)
        print(f"Error de valor: {mensaje_error}")
    except TypeError as error:
        # Excepción específica para argumentos incorrectos.
        mensaje_error = f"Cantidad o tipo de argumentos incorrectos: {error}"
        print(f"Error de argumentos: {mensaje_error}")
    else:
        print(f"Resultado: {resultado}")
        # El resultado exitoso se registra en el bloque else.
        entrada_historial = registrar_operacion(operacion, args, resultado=resultado)
    finally:
        # Toda operación queda registrada, tanto exitosa como fallida.
        if entrada_historial is None:
            entrada_historial = registrar_operacion(
                operacion, args, error=mensaje_error or "La operación no pudo completarse."
            )
        entrada_historial["finalizada"] = True
        print("Operación finalizada y registrada en el historial.")

    return resultado


def obtener_lista_numeros():
    """Lee números separados por comas y permite probar una lista vacía."""
    while True:
        try:
            texto = input(
                "Ingrese números separados por comas "
                "(o presione Enter para probar una lista vacía): "
            ).strip()
            if texto == "":
                return []
            return [convertir_texto_a_numero(valor.strip()) for valor in texto.split(",")]
        except ValueError:
            print("Lista inválida. Ejemplo correcto: 10, 8.5, -2, 4")
        except EOFError:
            print("No se recibió una entrada. Intente nuevamente.")
        except KeyboardInterrupt:
            print("\nCaptura cancelada. Intente nuevamente.")


def lanzar_error_intencional():
    print("1. Función inferior: se lanzará un ValueError intencional.")
    raise ValueError("Error intencional para demostrar la propagación.")


def funcion_intermedia():
    print("2. Función intermedia: llama a la inferior sin capturar el error.")
    lanzar_error_intencional()


def propagar_error():
    print("3. Función superior: inicia la demostración.")
    try:
        funcion_intermedia()
    except ValueError as error:
        print("4. El ValueError subió desde la función inferior,")
        print("   atravesó la función intermedia y fue capturado por la superior.")
        print(f"   Mensaje capturado: {error}")
        registrar_operacion("propagar_error", (), error=str(error))
    finally:
        print("5. Fin de la demostración de propagación.")


def mostrar_menu():
    print("\n" + "=" * 40)
    print("  CALCULADORA SEGURA")
    print("=" * 40)
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Calcular promedio")
    print("6. Raíz cuadrada")
    print("7. Probar propagación de excepciones")
    print("8. Ver historial")
    print("9. Salir")
    print("=" * 40)


def ejecutar_operacion_binaria(nombre):
    a = obtener_numero("Ingrese el primer número: ")
    b = obtener_numero("Ingrese el segundo número: ")
    calcular(nombre, a, b)


def iniciar_calculadora():
    while True:
        mostrar_menu()
        try:
            opcion = input("Seleccione una opción: ").strip()
        except EOFError:
            print("No se recibió una opción. El programa continuará.")
            continue
        except KeyboardInterrupt:
            print("\nUse la opción 9 para cerrar la calculadora correctamente.")
            continue

        if opcion == "1":
            ejecutar_operacion_binaria("sumar")
        elif opcion == "2":
            ejecutar_operacion_binaria("restar")
        elif opcion == "3":
            ejecutar_operacion_binaria("multiplicar")
        elif opcion == "4":
            ejecutar_operacion_binaria("dividir")
        elif opcion == "5":
            numeros = obtener_lista_numeros()
            calcular("promedio", numeros)
        elif opcion == "6":
            numero = obtener_numero("Ingrese el número: ")
            calcular("raiz_cuadrada", numero)
        elif opcion == "7":
            propagar_error()
        elif opcion == "8":
            mostrar_historial()
        elif opcion == "9":
            print("Gracias por usar la calculadora segura.")
            break
        else:
            print("Opción inválida. Seleccione un número del 1 al 9.")
