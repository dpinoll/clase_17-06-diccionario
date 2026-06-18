# libreria estandar de python
La librería estándar de Python es un conjunto de módulos que vienen preinstalados con Python y no requieren instalación adicional. Estas librerías cubren una amplia gama de funcionalidades, desde manejo de archivos hasta redes, fechas, matemáticas, y más.

- cuales son
No hay una lista oficial "fija", ya que puede variar ligeramente entre versiones de Python, pero las más importantes y comúnmente incluidas son:
Categorías principales

      Categoría
      Módulos destacados
     
      Manejo de datos
      json, csv, pickle, shelve, sqlite3
     
      Sistema y OS
      os, sys, shutil, pathlib, subprocess
     
      Matemáticas y números
      math, random, statistics, decimal, fractions
    
      Fechas y tiempos
      datetime, time, calendar
      
      Texto y strings
      re (expresiones regulares), string, textwrap
      
      Estructuras de datos
      collections, heapq, bisect, array
      
      Funcionales
      functools, itertools, operator
      
      Redes y HTTP
      http, urllib, socket, ftplib, smtplib
    
    
      Concurrencia
      threading, multiprocessing, asyncio, queue
     
      Archivos y directorios
      glob, fnmatch, fileinput
      
     Depuración y pruebas
      pdb, unittest, traceback
      
      Interfaz gráfica (básica)
      tkinter
        
      Compresión y archivos
      zipfile, gzip, tarfile
       
      Configuración y entorno
      configparser, argparse, getopt
     
      Utilidades varias
      copy, enum, typing, abc
    
- cuales son los mas usados
Los 10 módulos más populares de la librería estándar, según su frecuencia de uso en proyectos reales, son:
Módulos más usados
  
      Módulo
      Descripción
      Ejemplo de uso
      
      os
      Interacción con el sistema operativo (archivos, directorios, variables de entorno).
      os.listdir(), os.path.join()
      
      sys
      Acceso a variables y funciones del intérprete de Python.
      sys.argv, sys.exit()
       
      datetime
      Manejo de fechas, horas y zonas horarias.
      datetime.now(), timedelta
      
      json
      Serialización y deserialización de datos en formato JSON.
      json.dumps(), json.loads()
      
      re
      Expresiones regulares para búsqueda y manipulación de patrones en strings.
      re.search(), re.sub()
      
      random
      Generación de números aleatorios.
      random.randint(), random.choice()
      
      math
      Funciones matemáticas avanzadas.
      math.sqrt(), math.sin()
      
      collections
      Estructuras de datos especializadas (dicts, listas, etc.).
      defaultdict, Counter, namedtuple  
    
      requests
      ❌ No es estándar (pero muy usado; requiere pip install requests).
      requests.get()
       
      pathlib
      Manejo de rutas de archivos de forma orientada a objetos.
      Path("archivo.txt").read_text()
    
- y las formas 
Formas de usar las librerías estándar
Hay 3 formas principales de importar y usar módulos en Python:
a) Importar el módulo completo
python
Copiar

import os
os.listdir()  # Usas el nombre del módulo como prefijo

b) Importar funciones/clases específicas
python
Copiar

from datetime import datetime, timedelta
hora_actual = datetime.now()  # No necesitas el prefijo

c) Importar con alias (útil para nombres largos)
python
Copiar
import numpy as np  # Ejemplo con librería externa (no estándar)
import pandas as pd

d) Importar todo el contenido del módulo (no recomendado)
python
Copiar
from math import *  # Evita esto: puede causar conflictos de nombres
sqrt(16)  # Funciona, pero no es buena práctica
