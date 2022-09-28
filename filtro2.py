import pandas as pd
tablaMedellin=pd.read_csv('./Siembras.csv')

#Filtrar los datos de los municipios(andes, barbosa, caldas, tamesis y yarumal)

tablaMedellin1=tablaMedellin[tablaMedellin["Ciudad"]=="Medellín"].sort_values("Arboles",ascending=False)
print(tablaMedellin1.to_string())


archivoHTML=tablaMedellin1.to_html()
archivoTEXTO=open("datosMedellin.html","w",encoding="utf-8")
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()