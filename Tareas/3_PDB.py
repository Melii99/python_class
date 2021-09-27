"""
NAME
       3_PDB.py
VERSION
        [1.0]
AUTHOR
        Melissa Mayén Quiroz
DESCRIPTION
        La función lista_residuos nos pide como parámetros un path a la ubicación del archivo pdb,
        el nombre de la cadena de la cual sacaremos los residuos (str) y nuestro residuo de interés (str),
         y nos regresará una ista con los residuos de interés de la cadena especificada
INPUT
        Path a la ubicación del archivo pdb
        Nombre de lacadena de la cual sacaremos los residuos 
        Residuo de interés
OUTPUT
        Lista con los residuos de interés de la cadena especificada

EXAMPLES
        Input
          Lista_residuos('/content/1kcw.pdb', 'A', 'CYS')   
        Output
          [<Residue CYS het=  resseq=155 icode= >,
          <Residue CYS het=  resseq=181 icode= >,
          <Residue CYS het=  resseq=221 icode= >,
          <Residue CYS het=  resseq=257 icode= >,
          <Residue CYS het=  resseq=319 icode= >,
          <Residue CYS het=  resseq=338 icode= >,
          <Residue CYS het=  resseq=515 icode= >,
          <Residue CYS het=  resseq=541 icode= >,
          <Residue CYS het=  resseq=618 icode= >,
          <Residue CYS het=  resseq=680 icode= >,
          <Residue CYS het=  resseq=699 icode= >,
          <Residue CYS het=  resseq=855 icode= >,
          <Residue CYS het=  resseq=881 icode= >,
          <Residue CYS het=  resseq=1021 icode= >]
       
GITHUB 
        https://github.com/Melii99/python_class/tree/master/Tareas/3_PDB.py
       
"""

def Lista_residuos(file, cadena, residuo):
  """
  La función lista_residuos nos pide como parámetros un path a la ubicación del archivo pdb,
  el nombre de la cadena de la cual sacaremos los residuos (str) y nuestro residuo de interés (str),
  y nos regresará una ista con los residuos de interés de la cadena especificada
  """

  #Importamos librerías y ajustamos los warnings
  from Bio import PDB
  parser = PDB.PDBParser(QUIET=True)  

  #Uamos el método get_structure para obtener el obeto structure desde un archivo
  struc = parser.get_structure('archivo_PDB', file)

  #Creamos una lista vacía para añadir los residuos de interés
  residuos = []

  #Iteramos sobre los modelos dentro de struc
  for modelo in struc:
    #Iteramos sobre las cadenas de cada modelo
    for chain in modelo:
      #Ingresamos a la cadena de nuestro interés
      if chain.id == cadena:
        #Iteramos sobre los residuos de la cadena de interés
        for residue in chain:
          #Si el residuo sobre el que se itera es igual a nuestro aminoácido de interés, se añadirá a la lista residuos
          if residue.get_resname() == residuo:
            residuos.append(residue)

  return residuos
