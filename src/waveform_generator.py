"""
waveform_generator.py

Script para generar datos de memoria (ROM/RAM) de un generador de formas de onda.
Incluye cuatro tipos de onda: senoidal, cuadrada, diente de sierra y triangular.
Cada forma de onda consta de 256 muestras (valores de 0 a 255), y la ROM final 
contiene 1024 valores en total (4 bloques).

El archivo resultante se puede guardar en formato CSV o en formato de RAM estática.
"""

import math
import csv
from typing import List


def generate_sine_wave(num_samples: int = 256) -> List[int]:
    """Genera valores (0-255) de una onda senoidal de un ciclo."""
    sine_wave: List[int] = []
    for n in range(num_samples):
        theta = 2 * math.pi * n / num_samples
        # La salida de sin oscila entre -1 y 1. Se normaliza a 0-255.
        normalized = (math.sin(theta) + 1) / 2  # valor en [0,1]
        value = int(round(normalized * 255))
        sine_wave.append(value)
    return sine_wave


def generate_square_wave(num_samples: int = 256) -> List[int]:
    """Genera valores (0 o 255) correspondientes a una onda cuadrada de un ciclo."""
    half_point = num_samples // 2
    square_wave: List[int] = [255 if n <
                              half_point else 0 for n in range(num_samples)]
    return square_wave


def generate_sawtooth_wave(num_samples: int = 256) -> List[int]:
    """Genera valores (0-255) correspondientes a una onda diente de sierra de un ciclo."""
    sawtooth_wave: List[int] = []
    for n in range(num_samples):
        # División de (num_samples - 1) para asegurar rango [0,255]
        value = int(round(n * 255 / (num_samples - 1)))
        sawtooth_wave.append(value)
    return sawtooth_wave


def generate_triangle_wave(num_samples: int = 256) -> List[int]:
    """Genera valores (0-255) correspondientes a una onda triangular de un ciclo."""
    triangle_wave: List[int] = []
    half_point = num_samples // 2
    # Ascendente
    for n in range(half_point):
        value = int(round(n * 255 / (half_point - 1)))
        triangle_wave.append(value)
    # Descendente
    for n in range(half_point, num_samples):
        # Symmetry: valor en (num_samples-1 - n)
        value = int(round((num_samples - 1 - n) * 255 / (half_point - 1)))
        triangle_wave.append(value)
    return triangle_wave


def generate_rom_data(num_blocks: int = 4, block_size: int = 256) -> List[int]:
    """Genera la lista completa de 1024 muestras para ROM:
    Bloque 0: Onda senoidal
    Bloque 1: Onda cuadrada
    Bloque 2: Onda diente de sierra
    Bloque 3: Onda triangular
    """
    if num_blocks != 4:
        raise ValueError(
            "Se requieren 4 bloques de 256 muestras cada uno para generar la ROM.")
    # Cada función interna utiliza por defecto 256 muestras.
    sine_block = generate_sine_wave(block_size)
    square_block = generate_square_wave(block_size)
    sawtooth_block = generate_sawtooth_wave(block_size)
    triangle_block = generate_triangle_wave(block_size)
    # Concatenar en orden: seno, cuadrada, sierra, triangular
    return sine_block + square_block + sawtooth_block + triangle_block


def save_to_csv(filename: str = "memoria_datos.csv") -> None:
    """Guarda los datos de ROM en un archivo CSV con columnas 'address' y 'value'."""
    rom_data = generate_rom_data()
    try:
        with open(filename, mode="w", newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["address", "value"])
            for address, value in enumerate(rom_data):
                writer.writerow([address, value])
        print(
            f"Datos ROM guardados en '{filename}' (total {len(rom_data)} muestras).")
    except IOError as e:
        print(f"Error al guardar el archivo CSV: {e}")


def save_to_static_ram_format(filename: str = "Contenido_RAM_Estática.txt") -> None:
    """
    Guarda los datos de ROM en formato de RAM estática.
    Formato: dirección: valor1 valor2 valor3 valor4 valor5 valor6 valor7 valor8
    Cada línea contiene 8 valores consecutivos.
    """
    rom_data = generate_rom_data()
    try:
        with open(filename, mode="w", encoding='utf-8') as file:
            for i in range(0, len(rom_data), 8):
                # Tomar 8 valores consecutivos
                chunk = rom_data[i:i+8]
                # Si la última línea tiene menos de 8 valores, completar con los disponibles
                values_str = " ".join(map(str, chunk))
                file.write(f"{i}: {values_str}\n")

        print(
            f"Datos ROM guardados en formato RAM estática en '{filename}' (total {len(rom_data)} muestras).")

        # Mostrar información sobre los bloques
        print("\nDistribución de bloques:")
        print("Direcciones 0-255:   Onda senoidal")
        print("Direcciones 256-511: Onda cuadrada")
        print("Direcciones 512-767: Onda diente de sierra")
        print("Direcciones 768-1023: Onda triangular")

    except IOError as e:
        print(f"Error al guardar el archivo: {e}")


def save_both_formats(csv_filename: str = "memoria_datos.csv",
                      ram_filename: str = "Contenido_RAM_Estática.txt") -> None:
    """Guarda los datos en ambos formatos: CSV y RAM estática."""
    save_to_csv(csv_filename)
    save_to_static_ram_format(ram_filename)


def main() -> None:
    """Función principal: genera y guarda los datos de ROM en ambos formatos."""
    print("Generando datos de formas de onda...")
    save_both_formats()

    # Opcional: mostrar algunos valores de ejemplo
    rom_data = generate_rom_data()
    print(f"\nEjemplos de valores generados:")
    print(f"Onda senoidal (primeros 8 valores): {rom_data[0:8]}")
    print(f"Onda cuadrada (primeros 8 valores): {rom_data[256:264]}")
    print(f"Onda sierra (primeros 8 valores): {rom_data[512:520]}")
    print(f"Onda triangular (primeros 8 valores): {rom_data[768:776]}")


if __name__ == "__main__":
    main()
