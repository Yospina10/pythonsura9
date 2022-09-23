import pandas as pd

tablaEmpleados=pd.read_csv('./empleados.csv')
#print(tablaEmpleados)

#print(tablaEmpleados)

#print(tablaEmpleados.to.string())

#filtro 1 quiero obtener todos los datos de los analistas 1
'''tablaAnalistas1=tablaEmpleados[tablaEmpleados["cargo"]=="analista1"].head(50)
archivoHTML=tablaAnalistas1.to_html()
archivoTEXTO=open("datosanalista1.html","w")
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()
'''

'''tablaAnalistas2=tablaEmpleados[tablaEmpleados["cargo"]=="analista2"].head(50)
archivoHTML=tablaAnalistas2.to_html()
archivoTEXTO=open("datosanalista2.html","w")
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()
'''

tablaAnalistas3=tablaEmpleados[(tablaEmpleados["salario"]>5500000) & (tablaEmpleados["edad"]<30)].head(50)
archivoHTML=tablaAnalistas3.to_html()
archivoTEXTO=open("datosanalista3.html","w")
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()
