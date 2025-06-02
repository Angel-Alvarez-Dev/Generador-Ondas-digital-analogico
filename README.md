# Actividad V: Sistema Digital-Analógico Generador de Formas de Onda

---

## Objetivo

Desarrollar habilidades para diseñar sistemas digitales con memoria de semiconductor, capaces de generar cuatro formas de señales analógicas: senoidal, cuadrada, diente de sierra y triangular. El sistema incluirá un control de frecuencia (potenciómetro) y permitirá determinar la amplitud y polaridad (unipolar o bipolar) de la señal mediante un convertidor digital-analógico (CDA).

---

## Introducción

Esta actividad consiste en implementar, simular y documentar un generador de señales analógicas basado en un subsistema digital. El diseño emplea:

- **Temporizador 555**: genera un reloj ajustable con un potenciómetro para modificar la frecuencia.
- **Contador binario de 8 bits**: avanza la dirección de memoria de forma secuencial.
- **Memoria ROM (1024×8 bits)**: almacena los valores digitales correspondientes a los cuatro tipos de onda.
- **Convertidor Digital-Analógico (DAC) de 8 bits**: convierte los valores digitales en una señal analógica de salida.  
- El **potenciómetro** permite variar la frecuencia de la señal generada.
- La **memoria ROM** contiene los datos precalculados de amplitud para cada forma de onda (seno, cuadrada, diente de sierra y triangular).  

La idea es, mediante la simulación en CircuitJS (o cualquier CAD compatible con HTML), comprobar el correcto funcionamiento del sistema y verificar que la señal de salida cumple con las cuatro formas de onda requeridas.

---

## Desarrollo

### a) Definición de datos en la memoria

Para almacenar las cuatro formas de onda en la ROM, se definieron bloques de direcciones para cada tipo:

- **Bloque 0 a 255**: Valores para onda senoidal (256 muestras por ciclo).  
- **Bloque 256 a 511**: Valores para onda cuadrada (estado alto/bajo alternado).  
- **Bloque 512 a 767**: Valores para onda diente de sierra (rampas ascendentes).  
- **Bloque 768 a 1023**: Valores para onda triangular (rampas ascendentes y descendentes).  

Los valores digitales de amplitud se codificaron en 8 bits (0–255), y en la simulación se configuró el DAC para interpretar 0 como onda negativa (pol. bipolar) y 255 como onda positiva máxima.

### b) Diagrama electrónico (CircuitJS)

En el archivo `Generator.html` se encuentra el diagrama interactivo que integra:

1. **Temporizador 555**:  
   - Conexiones de R<sub>A</sub>, R<sub>B</sub> y C para generar un reloj astable.  
   - Potenciómetro de 10 kΩ permite ajustar la frecuencia de oscilación.
2. **Contador binario 8 bits**:  
   - Se utiliza un contador síncrono (o secuencial) que avanza en cada pulso del temporizador.  
   - Las salidas Q<sub>0</sub>…Q<sub>7</sub> forman el bus de direcciones A<sub>0</sub>…A<sub>7</sub>.
3. **Memoria ROM (1024×8 bits)**:  
   - Entradas de dirección A<sub>0</sub>…A<sub>9</sub> (Q<sub>0</sub>…Q<sub>7</sub> combinadas con rangos de selección).  
   - Salida de datos D<sub>0</sub>…D<sub>7</sub> conecta al DAC.
4. **DAC de 8 bits**:  
   - Convierte el dato digital en tensión analógica.  
   - Un amplificador o red de resistencias configuradas determinan polaridad y amplitud.  

Adicionalmente, el archivo `circuitjs_connections_guide.html` muestra cómo se interconectan los módulos (555, contador, ROM y DAC) en CircuitJS.

### c) Simulación y verificación

Para simular y comprobar:

1. Abrir `Generator.html` en un navegador web moderno (Chrome, Firefox, Edge).  
2. Ajustar el potenciómetro para seleccionar una frecuencia de reloj adecuada (por ejemplo, 1 kHz).  
3. En el osciloscopio virtual conectado a la salida del DAC, verificar que aparecen las cuatro formas de onda:
   - **Senoidal** (bloque 0–255 de la ROM).  
   - **Cuadrada** (bloque 256–511).  
   - **Diente de sierra** (bloque 512–767).  
   - **Triangular** (bloque 768–1023).  
4. Cambiar la selección de bloque de memoria (mediante interruptores o entradas L en la ROM) para conmutar entre las cuatro señales.  
5. Observar la polaridad correcta (bipolar/unipolar) y la amplitud conforme a los valores de la ROM y la configuración del DAC.

---

## Prueba de conocimientos

1. **Explica el principio de funcionamiento de un temporizador 555 en modo astable.**  
2. **¿Cómo se calcula el valor del condensador y las resistencias para obtener una frecuencia específica en el 555?**  
3. **Describe el funcionamiento interno de un contador binario de 8 bits y cómo genera las direcciones para la ROM.**  
4. **¿Por qué se necesitan 1024 direcciones en la ROM para generar las cuatro formas de onda?**  
5. **Explica cómo un DAC de 8 bits convierte un valor digital en una señal analógica.**  
6. **¿Qué cambios realizarías si quisieras que el sistema funcione en modo unipolar en lugar de bipolar?**

---

## Conclusiones

- El sistema digital-analógico diseñado cumple con la generación de las cuatro formas de onda requeridas: senoidal, cuadrada, diente de sierra y triangular.  
- El uso de un temporizador 555 con un potenciómetro proporciona un control sencillo de la frecuencia de muestreo, cambiando la velocidad del contador y, por ende, la frecuencia de la onda.  
- La memoria ROM correctamente programada con bloques de datos facilita la conmutación entre diferentes formas de onda de manera rápida.  
- El DAC de 8 bits demostró ser suficiente para generar formas de onda continuas con resolución aceptable.  
- Para modos unipolar, basta con ajustar el rango de voltaje en el DAC (por ejemplo, usando sólo valores positivos y desplazando la referencia a 0 V).  
- Las simulaciones en CircuitJS ofrecieron un entorno práctico para validar el diseño sin necesidad de hardware físico.

---

## Bibliografía

1. **Texas Instruments.** _LM555 Timer Datasheet_.  
2. **Manuales de CircuitJS.** _Guía de uso y librerías de componentes_.  
3. **Malvino, A. P. & Brown, D. J.** _Fundamentos de Electrónica Digital_.  
4. **Sedra, A. S. & Smith, K. C.** _Microelectrónica_.  
5. **Rabaey, J. M.** _Fundamentos de Sistemas de Comunicaciones_, capítulo sobre conversión D/A.  

---

## Estructura del repositorio

```
/
├── .gitignore
├── README.md
├── assets/
│   ├── Señal_senoidal.png
│   ├── Señal_cuadrada.png      
│   ├── Señal_diente_de_sierra.png      
│   ├── Señal_triangular.png      
│   └── Circuito.png
│
├── circuitjs_connections_guide.html (Datos de las conexiones del circuito)
├── ram_programming_data.html      (Datos de la RAM estática)
├── Generator.html                 (simulación completa)
│
└── docs/
    ├── Sistema Digital-Analógico Generador de Formas de Onda.txt  (Exportado Circuito para CircuitJS)
    ├── Contenido_RAM_Estática.txt (Valores RAM estática (SRAM))
    └── Diagrama electrónico.pdf  (Resultados y conclusiones)
```

- **`assets/Señal_senoidal.png`**
- - **`assets/Señal_senoidal.png`**
- **`assets/Señal_senoidal.png`**
- - **`assets/Señal_senoidal.png`**
- - : captura de ejemplo con las cuatro formas de onda superpuestas.  


---

> **Fecha de entrega en Classroom:** 5 de junio de 2025  
> **Alumno:** Álvarez Villegas José Ángel  
> **Curso:** Sistemas Digitales, Grupo 2611E, UNAM FES Cuautitlán  

