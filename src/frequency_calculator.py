"""
frequency_calculator.py

Este script proporciona funciones para calcular la frecuencia de un temporizador 555 en configuración astable,
dado los valores de las resistencias RA, RB y el condensador C. También permite calcular alguno de los valores
de resistencia o capacitancia necesarios para alcanzar una frecuencia deseada.

Fórmulas:
- Periodo (T) = 0.693 * (RA + 2*RB) * C
- Frecuencia (f) = 1 / T

Donde:
- RA: resistencia entre Vcc y descarga
- RB: resistencia entre descarga y umbral
- C: capacitancia en Faradios

Funciones incluidas:
- calculate_frequency
- calculate_period
- calculate_ra_for_frequency
- calculate_rb_for_frequency
- calculate_c_for_frequency
"""

from typing import Optional

def calculate_period(ra: float, rb: float, c: float) -> float:
    """
    Calcula el periodo (T) de la señal generada por el 555 en modo astable.

    Parámetros:
    - ra: resistencia RA en ohmios
    - rb: resistencia RB en ohmios
    - c: capacitancia C en Faradios

    Retorna:
    - Periodo T en segundos
    """
    if ra < 0 or rb < 0 or c <= 0:
        raise ValueError("RA y RB deben ser no negativos, C debe ser positivo.")
    period = 0.693 * (ra + 2 * rb) * c
    return period

def calculate_frequency(ra: float, rb: float, c: float) -> float:
    """
    Calcula la frecuencia (f) de la señal del 555 en modo astable.

    Parámetros:
    - ra: resistencia RA en ohmios
    - rb: resistencia RB en ohmios
    - c: capacitancia C en Faradios

    Retorna:
    - Frecuencia f en Hertz
    """
    period = calculate_period(ra, rb, c)
    frequency = 1.0 / period
    return frequency

def calculate_ra_for_frequency(target_freq: float, rb: float, c: float) -> float:
    """
    Calcula el valor de RA necesario para obtener una frecuencia deseada,
    dado RB y C.

    Parámetros:
    - target_freq: frecuencia deseada en Hertz
    - rb: resistencia RB en ohmios
    - c: capacitancia C en Faradios

    Retorna:
    - Valor de RA en ohmios
    """
    if target_freq <= 0 or rb < 0 or c <= 0:
        raise ValueError("Frecuencia debe ser positiva, RB no negativo, C positivo.")
    # Periodo deseado
    t = 1.0 / target_freq
    # t = 0.693 * (RA + 2*RB) * C  => RA = (t / (0.693 * C)) - 2*RB
    ra = (t / (0.693 * c)) - 2 * rb
    if ra < 0:
        raise ValueError("No se puede obtener una RA positiva con los valores dados.")
    return ra

def calculate_rb_for_frequency(target_freq: float, ra: float, c: float) -> float:
    """
    Calcula el valor de RB necesario para obtener una frecuencia deseada,
    dado RA y C.

    Parámetros:
    - target_freq: frecuencia deseada en Hertz
    - ra: resistencia RA en ohmios
    - c: capacitancia C en Faradios

    Retorna:
    - Valor de RB en ohmios
    """
    if target_freq <= 0 or ra < 0 or c <= 0:
        raise ValueError("Frecuencia debe ser positiva, RA no negativo, C positivo.")
    t = 1.0 / target_freq
    # t = 0.693 * (RA + 2*RB) * C  => RB = ( (t / (0.693 * C)) - RA ) / 2
    rb = ((t / (0.693 * c)) - ra) / 2
    if rb < 0:
        raise ValueError("No se puede obtener una RB positiva con los valores dados.")
    return rb

def calculate_c_for_frequency(target_freq: float, ra: float, rb: float) -> float:
    """
    Calcula el valor de C necesario para obtener una frecuencia deseada,
    dado RA y RB.

    Parámetros:
    - target_freq: frecuencia deseada en Hertz
    - ra: resistencia RA en ohmios
    - rb: resistencia RB en ohmios

    Retorna:
    - Valor de C en Faradios
    """
    if target_freq <= 0 or ra < 0 or rb < 0:
        raise ValueError("Frecuencia debe ser positiva, RA y RB no negativos.")
    t = 1.0 / target_freq
    # t = 0.693 * (RA + 2*RB) * C  => C = t / (0.693 * (RA + 2*RB))
    c = t / (0.693 * (ra + 2 * rb))
    return c

def main() -> None:
    """
    Ejemplo de uso de las funciones. Se pueden comentar las secciones no deseadas.
    """
    # Ejemplo: calcular frecuencia con RA=1kΩ, RB=2kΩ, C=100nF
    ra_value = 1e3  # ohmios
    rb_value = 2e3  # ohmios
    c_value = 100e-9  # Faradios (100 nF)

    freq = calculate_frequency(ra_value, rb_value, c_value)
    print(f"Frecuencia calculada: {freq:.2f} Hz")

    # Ejemplo: calcular RA para frecuencia de 1 kHz, con RB=2kΩ y C=100nF
    target = 1e3  # 1 kHz
    try:
        ra_needed = calculate_ra_for_frequency(target, rb_value, c_value)
        print(f"RA necesaria para {target} Hz: {ra_needed:.2f} Ω")
    except ValueError as ve:
        print(ve)

    # Ejemplo: calcular RB para frecuencia de 500 Hz, con RA=1kΩ y C=100nF
    target2 = 500  # Hz
    try:
        rb_needed = calculate_rb_for_frequency(target2, ra_value, c_value)
        print(f"RB necesaria para {target2} Hz: {rb_needed:.2f} Ω")
    except ValueError as ve:
        print(ve)

    # Ejemplo: calcular C para frecuencia de 2 kHz, con RA=1kΩ y RB=2kΩ
    target3 = 2e3  # 2 kHz
    c_needed = calculate_c_for_frequency(target3, ra_value, rb_value)
    print(f"C necesaria para {target3} Hz: {c_needed * 1e9:.2f} nF")

if __name__ == "__main__":
    main()
