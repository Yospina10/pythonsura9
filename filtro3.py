import pandas as pd
tablaCaucasia=pd.read_csv('./Siembras.csv')

#Filtrar los datos de los municipios(andes, barbosa, caldas, tamesis y yarumal)

tablaCaucasia1=tablaCaucasia[(tablaCaucasia["Ciudad"]=="Caucasia")]
tablaCaucasia2=tablaCaucasia1["Hectareas"].to_frame()
#print(tablaCaucasia2)


archivoHTML=tablaCaucasia2.to_html()
archivoTEXTO=open("datosCaucasia.html","w",encoding="utf-8")
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()