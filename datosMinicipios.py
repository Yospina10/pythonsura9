import pandas as pd
tablaMunicipios=pd.read_csv('./Siembras.csv')

#Filtrar los datos de los municipios(andes, barbosa, caldas, tamesis y yarumal)

tablaMunicipios1=tablaMunicipios[(tablaMunicipios["Ciudad"]=="Andes") | (tablaMunicipios["Ciudad"]=="Barbosa") | (tablaMunicipios["Ciudad"]=="Caldas") | (tablaMunicipios["Ciudad"]=="Tamesis") | (tablaMunicipios["Ciudad"]=="Yarumal")]
#print(tablaMunicipios1)


archivoHTML=tablaMunicipios1.to_html()
archivoTEXTO=open("datosMunicipio.html","w",encoding="utf-8")
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()