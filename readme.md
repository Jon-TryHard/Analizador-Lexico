# Analizador Léxico para B-Minor+

Este proyecto implementa la primera fase de un compilador (el Analizador Léxico o *Lexer*) para el lenguaje **B-Minor+**. Está desarrollado en Python utilizando la librería **SLY (Syntax Language oY-compiler)** para la tokenización y **Rich** para una visualización estética, formateada y legible de los tokens en la terminal.

---

## Integrantes
* **Jonathan David Ochoa Echeverri**
* **Juan Camilo Gil Ramírez**
* **Juan José Ruiz Mellizo**

---

## Estructura del Proyecto

Al descomprimir el archivo, encontrará la siguiente estructura de directorios y archivos base:

```text
Analizador_Lexico/
├── lexer.py             # Código fuente del Analizador Léxico en Python
├── requirements.txt     # Archivo de dependencias del proyecto (sly, rich)
├── sieve.bp             # Archivo de prueba: Algoritmo de la Criba de Eratóstenes
├── test.bp              # Archivo de prueba: Expresión aritmética simple
└── README.md            # Documentación del proyecto (este archivo)