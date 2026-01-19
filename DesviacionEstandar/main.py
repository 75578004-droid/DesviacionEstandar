from src.logica.DesviacionEstandar import DesviacionEstandar


def main():
    print("=== CÁLCULO DE DESVIACIÓN ESTÁNDAR ===")
    print("Ingrese los números separados por espacios:")
    
    entrada = input("> ")
    
    try:
        numeros = [float(x) for x in entrada.split()]
        
        if len(numeros) == 0:
            print("Error: Debe ingresar al menos un número")
            return
        
        desviacion = DesviacionEstandar(numeros)
        resultado = desviacion.calcular()
        
        if resultado is None:
            print("No se puede calcular la desviación estándar")
        else:
            print(f"\nDatos: {numeros}")
            print(f"Desviación Estándar: {resultado:.4f}")
    
    except ValueError:
        print("Error: Ingrese solo números válidos")


if __name__ == "__main__":
    main()
