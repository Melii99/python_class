"""
NAME
        6_ExPASy.py
VERSION
        [1.0]
AUTHOR
        Melissa Mayén Quiroz
        
DESCRIPTION
        La función 'expasy'  nos pide como parámetros (1)una lista de IDs de UniProt y (2)una lista de GOs. Con ellos se
        realizará una búsqueda de cada uno de los términos GO dentro de cada archivo  del cual proporcionamos un ID.
        En caso de encontrarse algún término GO en uno de los archivos, se escribirán lo siguientes datos
        en un archivo de salida llamado 'archivo_ExPASy':
        -ID y nombre de la proteína donde se encontró
        -El término GO encontrado y su definición
        -El organismo al que pertenece la proteína
        -Localización subcelular
        -Un abstract de alguno de los artículos mencionado en el archivo
        -Prosite ID
INPUT
        -Lista de que contenga IDs de UniProt
        -Lista que contenga GOs
OUTPUT
        Archivo (archivo_ExPASy) que contiene los sig. datos  de los GOs encontrados en los archivos:
        -ID y nombre de la proteína donde se encontró
        -El término GO encontrado y su definición
        -El organismo al que pertenece la proteína
        -Localización subcelular
        -Un abstract de alguno de los artículos mencionado en el archivo
        -Prosite ID
EXAMPLES
        Input
                uniprot_IDs = ["A0A0K2RVI7_9BETC", "A8R4D4_9BETC",
                        "POLG_YEFV1", "POLG_DEN1W",
                        "Q6W352_CVEN9", "D9SV67_CLOC7",
                        "A9KSF7_LACP7", "B8I7R6_RUMCH"]
                        expasy(uniprot, go)
                GO_Terms = ["GO:0046755", "GO:0046761",
                        "GO:0046760", "GO:0039702",
                        "GO:0046765", "GO:0046762"]

                expasy(uniprot_IDs, GO_Terms)
        Output

               < ID:      A0A0K2RVI7_9BETC
                Proteína donde se encontró:     Envelope small membrane protein 
                GO encontrado:  GO:0046760
                Definición:     P:viral budding from Golgi membrane
                Organismo al que pertence la proteina:  Equine coronavirus.
                Localizacion subcelular:         Host Golgi apparatus membrane 
                Abstract:       
                1. Arch Virol. 2015 Nov;160(11):2903-6. doi: 10.1007/s00705-015-2565-1. Epub 2015
                Aug 14.

                Complete genome analysis of equine coronavirus isolated in Japan.

                Nemoto M(1), Oue Y(2), Murakami S(3), Kanno T(4), Bannai H(5), Tsujimura K(5),
                Yamanaka T(5), Kondo T(5).

                Author information: 
                (1)Epizootic Research Center, Equine Research Institute, Japan Racing
                Association, 1400-4 Shiba, Shimotsuke, Tochigi, 329-0412, Japan.
                nemoto_manabu@equinst.go.jp.
                (2)Hokkaido Kushiro Livestock Hygiene Service Center, 127-1 Otanoshike, Kushiro, 
                Hokkaido, 084-0917, Japan.
                (3)Thermo Fisher Scientific, Life technologies Japan Ltd., Sumitomo Fudosan Mita 
                Twin Bldg., 4-2-8 Shibaura, Minato-ku, Tokyo, 108-0023, Japan.
                (4)Dairy Hygiene Research Division, Hokkaido Research Station, National Institute
                of Animal Health, 4 Hitsujigaoka, Toyohira, Sapporo, Hokkaido, 062-0045, Japan.
                (5)Epizootic Research Center, Equine Research Institute, Japan Racing
                Association, 1400-4 Shiba, Shimotsuke, Tochigi, 329-0412, Japan.

                Equine coronavirus has been responsible for several outbreaks of disease in the
                United States and Japan. Only one complete genome sequence (NC99 isolated in the 
                US) had been reported for this pathogenic RNA virus. Here, we report the complete
                genome sequences of three equine coronaviruses isolated in 2009 and 2012 in
                Japan. The genome sequences of Tokachi09, Obihiro12-1 and Obihiro12-2 were
                30,782, 30,916 and 30,916 nucleotides in length, respectively, excluding the
                3'-poly (A) tails. All three isolates were genetically similar to NC99
                (98.2-98.7%), but deletions and insertions were observed in the genes nsp3 of
                ORF1a, NS2 and p4.7.

                DOI: 10.1007/s00705-015-2565-1 
                PMCID: PMC7086706
                PMID: 26271151  [Indexed for MEDLINE]

                Prosite IDs:    ['PS51926']

                (...) >

GITHUB 
        https://github.com/Melii99/python_class/tree/master/Tareas/6_ExPASy.py
       
"""

'''
Función expasy:
Definimos la funcion expasy, que nos regresará un archivo llamado archivo_ExPASy que, de encontrar un término GO
en alguno de los archivos contendrá el ID y nombre de la proteína donde se encontró,el término GO encontrado y su definición, 
el organismo al que pertenece la proteína, la localización subcelular, un abstract de alguno de los artículos mencionado en el
archivo y Prosite IDs asociados que se encuentren.
Parámentos:
        (1)Lista de que contenga IDs de UniProt
        (2)ista que contenga GOs

'''
def expasy(uniprot_idlst, GOs):

        #Importamos las librerias necesarias
        from Bio import Entrez
        #proporcionamos un email
        Entrez.email = "mmayen@lcg.unam.mx"
        from Bio import ExPASy
        from Bio import SwissProt

        #Creamos un archivo en modo escritura titulado 'archivo_ExPASy'
        archivo = open("archivo_ExPASy", "w")

        #Recorremos cada elememto en la lista de IDs de UniProt
        for i in uniprot_idlst:
                #Obtenemos los archivos y se guardan en el record
                handle = ExPASy.get_sprot_raw(i)
                record = SwissProt.read(handle)

                #Recorremos cada elemeto de la lista de GOs
                for j in range(0,len(GOs)):
                        #Recorremos las referencias cruzadas
                        for k in range(0,len(record.cross_references)):

                                #Condición para saber si los términos GO se encuentran en los archivos
                                #En caso de ser así, se obtienen los datos deseados
                                if (GOs[j] == record.cross_references[k][1]):
                                        #guardamos un ID de un artículo encontrado en las referencias
                                        id_articulo = record.references[0].references

                                        ##### ID y Nombre de la proteína #####
                                        #partimos la descripción del record para obtener el nombre de la proteína
                                        protein = record.description.split("=")[1]
                                        protein = protein.split("{")[0]
                                        protein = protein.split(";")[0]
                                        #Se escribe el ID y el nombre de la proteína en el archivo
                                        archivo.write('ID:\t'+ i + '\nProteína donde se encontró:\t'+ protein)

                                        ##### GO encontrado y su definición #####
                                        #Se escribe el GO encontrado y su definición en el archivo
                                        archivo.write('\nGO encontrado:\t'+ GOs[j] + '\nDefinición:\t' + record.cross_references[k][2])

                                        ##### Organismo al que pertenece #####
                                        #Se escribe el organismo al que pertenece en el archivo
                                        archivo.write('\nOrganismo al que pertence la proteina:\t'+ record.organism)

                                        ##### Localización subcelular #####
                                        #Recorremos los comentarios
                                        for l in range(0, len(record.comments)):
                                                #Si se encuentra la localización subcelular en los comentarios hacemos varios splits
                                                if 'SUBCELLULAR LOCATION' in record.comments[l]:
                                                        #partimos los comentarios para guardar unicamente la localización subcelular
                                                        location = record.comments[l].split('SUBCELLULAR LOCATION:')[1]
                                                        location = location.split("{")[0]
                                                        location = location.split(";")[0]
                                                        #Se escribe la localización subcelular en el archivo
                                                        archivo.write("\nLocalizacion subcelular:\t" + location)
      
                                        ##### Absrtact #####
                                        #En caso de encontrar un ID de algún artículo mencionado en el archivo se busca su abstract
                                        if len(id_articulo) > 0:
                                                id_articulo = id_articulo[0][1]
                                                #Búsqueda del abstract
                                                fetch_handle = Entrez.efetch(db="pubmed", id=id_articulo, rettype="abstract", retmode="text")
                                                abstract = fetch_handle.read()
                                                fetch_handle.close()
                                                #Se escribe el abtract en el archivo
                                                archivo.write("\nAbstract:\t" + abstract)
                                        #En caso de no enontrarse un ID, se indica en el archivo que no se encontró un absrtact        
                                        else:
                                                archivo.write("\nNo se encontró un abstract con los términos deseados")

                                        ##### Prosite ID #####
                                        #Se usa una bandera para saber si se encontraron prosite IDs
                                        prosite = 0
                                        #Se crea una lista vacía para guardar los prosites
                                        prosite_list = []
                                        #Se recorren las referencias
                                        for l in record.cross_references: 
                                                #Si se encuentra algún prosite se añade a la lista de prosites
                                                if 'PROSITE' in l:
                                                        prosite_list.append(l[1])
                                                        #La bandera señaliza que sí se encontraron prosites
                                                        prosite = 1
                                        #Si se encontraron prosites se escriben en el archivo
                                        if prosite == 1:   
                                                archivo.write("\nProsite IDs:\t" + str(prosite_list)+ "\n\n\n\n")
                                        #En caso de no encontrar prosites se indica en el archivo
                                        if prosite == 0:
                                                archivo.write("\n>No se encontró algún Prosite ID\n\n\n\n")



#Se guarda una lista con IDs de UniProt
uniprot_IDs = ["A0A0K2RVI7_9BETC","A8R4D4_9BETC","POLG_YEFV1","POLG_DEN1W","Q6W352_CVEN9","D9SV67_CLOC7","A9KSF7_LACP7","B8I7R6_RUMCH"]
#Se guarda una lista con GOs
GO_Terms = ["GO:0046755","GO:0046761","GO:0046760","GO:0039702","GO:0046765","GO:0046762"]

#Pasamos como parámetros las listas a la función 'expasy' creamos un nuevo archivo 'archivo_ExPASy' con la info. deseada
expasy(uniprot_IDs, GO_Terms)