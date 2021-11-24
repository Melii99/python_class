"""
NAME
       7_NumPy.py
VERSION
        [1.0]
AUTHOR
        MMelissa Mayén Quiroz

DESCRIPTION
        Este script usa la librería NumPy para crear arrays estructurados de los arrays (np.array) 
        del ejercicio 1 vistos en clase; y los imprime a pantalla.
INPUT
        No es necesario ingresar un input
OUTPUT
        Se imprime a pantalla los arrays estructurados creados:
        (1) produccion_array
        (2) costos_array
        (3) costo_unitario_array
EXAMPLES
        Input

        Output
                Se imprime a pantalla
               < [('Gen1',  5, 3) ('Gen2', 11, 7) ('Gen3',  4, 9) ('Gen4',  2, 6)] 

                [('Gen1', 3.5) ('Gen2', 5. ) ('Gen3', 7. ) ('Gen4', 4.3)] 

                [('Gen1', 0.7       , 1.16666667) ('Gen2', 0.45454545, 0.71428571)
                ('Gen3', 1.75      , 0.77777778) ('Gen4', 2.15      , 0.71666667)] >

GITHUB
        https://github.com/Melii99/python_class/tree/master/Tareas/7_NumPy.py
"""

#Importamos la librería Numpy con el apodo np
import numpy as np

#Arrays creados en el ejercicio 1
produccion = np.array([ [5,3], [11, 7], [4, 9], [2, 6]])
costos = np.array([3.5, 5, 7, 4.3])
costo_unitario = (costos/produccion.T).T

#Creación del array estructurado de producción
produccion_array = np.array([('Gen1', 5, 3), ('Gen2', 11, 7), ('Gen3', 4, 9), ('Gen4', 2, 6)],
       dtype=[('Gen', (np.str_, 10)), ('30_grados', np.int32), ('35_grados', np.int32)])

#Creación del array estructurado de costos
costos_array = np.array([('Gen1', 3.5), ('Gen2', 5), ('Gen3', 7), ('Gen4', 4.3)],
       dtype=[('Gen', (np.str_, 10)), ('Costo', np.float32)])

#Creación del array estructurado del costo unitario
costo_unitario_array = np.array([('Gen1', 0.7, 1.16666667), ('Gen2', 0.45454545, 0.71428571), ('Gen3', 1.75, 0.77777778), ('Gen4', 2.15, 0.71666667)],
       dtype=[('Gen', (np.str_, 10)), ('30_grados', np.float64), ('35_grados', np.float64)])

#Imprimimos a pantalla los 3 array estructurados
print(produccion_array, '\n')
print(costos_array, '\n')
print(costo_unitario_array)
