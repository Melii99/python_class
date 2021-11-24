"""
NAME
       4_Busqueda.py
VERSION
        [1.0]
AUTHOR
        Melissa Mayén Quiroz

DESCRIPTION
        Primera parte:
        Empleando Entrez.einfo y Entrez.read, se imprime la descripción de los siguientes campos de la base de datos "protein":
        - FieldList "ECNO"
        - LinkList "protein_protein_small_genome"
        Segunda parte:
        La función 'busqueda' nos pide como parámetros (1)el path donde deseamos guardar nuestro archivo de salida y 
        algunos términos necesarios para la búsqueda: (2)el nombre del autor o autora a buscar y (3)(4)dos términos 
        que esperamos se encuentre en el título; y nos regresará un archivo en el path especificado que contenga los IDs
        de los artículos encontrados.  
INPUT
        Primera parte:
        No es necesario un input
        Segunda parte:
        -Path donde deseamos guardar el archivo de salida
        -Nombre del autor o autora a buscar
        -Término a buscar en el título 
        -Término alternativo a buscar en el título 
OUTPUT
        Archivo (con el path especificado por el usuario) que contiene los IDs de los artículos encontrados.
EXAMPLES
        Input
          Primera parte: 
            No es necesario un input
          Segunda parte:
            busqueda("C:\\Users\\Melissa\\Downloads\\archivo_ids","Cevallos", "microbiota","signaling")
        Output
          Primera parte:
            <FieldList ECNO:
            EC number for enzyme or CAS registry number
            LinkList protein_protein_small_genome:
            All proteins from this genome>
        Segunda parte:
            Archivo de salida C:\\Users\\Melissa\\Downloads\\archivo_ids 
            <IDs: 
            ['34385401', '33468700', '28798125', '28409539']>
       
GITHUB 
        https://github.com/Melii99/python_class/tree/master/Tareas/4_busqueda.py
       
"""

'''
Primera parte:
'''

#Importación de librerías
from Bio import Entrez
#Proporcionamos un email
Entrez.email = "mmayen@lcg.unam.mx"

# Handle con einfo
handle = Entrez.einfo(db = "protein")
record = Entrez.read(handle)

#Con un for recorremos "FieldList" y si coincide con "ECNO", se imprime su descripción
print("FieldList ECNO:")
for field in record["DbInfo"]["FieldList"]:
    if field["Name"] == "ECNO":
        print(field["Description"])

#Con un for recorremos "LinkList" y si coincide con "protein_protein_small_genome", se imprime su descripción
print("LinkList protein_protein_small_genome:")
for field in record["DbInfo"]["LinkList"]:
    if field["Name"] == "protein_protein_small_genome":
        print(field["Description"])

handle.close()


'''
Segunda parte:
Definimos la función busqueda, que nos regresará un archivo en el path especificado que contenga los IDs de los artículos encontrados.  
Parámetros:
        (1)Path donde deseamos guardar el archivo de salida
        (2)Nombre del autor o autora a buscar
        (3)Término a buscar en el título 
        (4)Término alternativo a buscar en el título
'''

def busqueda(path,autor, palabra1, palabra2):

    #Realizamos la importación de librerías
    from Bio import Entrez
    #Le proporcionamos un email
    Entrez.email = "mmayen@lcg.unam.mx"

    #Abrimos un archivo en modo escritura (con el path proporcionado)
    archivo = open(path, "w+")

    #Realizamos la búsqueda del autor y los términos proporcionados
    termino = f'(({autor}[AUTH]) AND ({palabra1}[Title] OR {palabra2}[Title]))'
    handle = Entrez.esearch(db="pubmed", term=termino)
    #Guardamos los IDs encontrados
    ids = Entrez.read(handle)

    #Escribimos los IDs en el archivo
    archivo.write("IDs: \n" + str(ids["IdList"]))
    #Cerramos el archivo
    archivo.close()
    #Cerramos el handle
    handle.close()


busqueda("C:\\Users\\Melissa\\Downloads\\archivo_ids","Cevallos", "microbiota","signaling")