import os
import pandas as pd

def analisis_datos(data: pd.core.frame.DataFrame)->dict:
    sum_edades_est = 0
    c_edades_est = 0
    cant_tipo = data['Tipo'].value_counts(dropna = False)
    tipo = data['Tipo']
    edad = data['Edad']
    for tipo, edad in zip(tipo, edad):
        if tipo == 'En estudio':
            sum_edades_est += edad
            c_edades_est += 1
    dic = {
        'casos_en_estudio': cant_tipo[1],
        'prom_edades_casos_en_estudio': int(sum_edades_est / c_edades_est),
    }
    return dic

print(analisis_datos(
    (pd.read_csv('https://bitbucket.org/ingluise2019/misiontic/downloads/Casos_positivos_de_COVID-19_en_Colombia.csv').sample(frac=1.0, random_state=123))))

# print(analisis_datos(
#     (pd.read_csv(os.path.dirname(__file__) + '/Casos_positivos_de_COVID-19_en_Colombia.csv').sample(frac=1.0, random_state=123))))