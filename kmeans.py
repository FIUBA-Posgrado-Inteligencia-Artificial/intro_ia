def __main__():
    pass

import numpy as np

def genData(clusters, samples, features):
    data = []
    samplesPerClass = samples // clusters 
    # Implemento la generación de este modo para que cada clase
    # tenga realmente una distribución diferente al resto.  
    for i in range(clusters):
        newPoints = np.random.normal(loc=0, scale=((i+1)**2)/2, size=(samplesPerClass, features))
        data.append(newPoints)
    data = np.array(data).reshape((samples,features))
    return data


def kmeans(clusters, data, iter):
    classification = np.zeros(len(data))
    indexes = np.array([x for x in range(0,len(data),1)]) # Lista con los indices de los datos
    np.random.shuffle(indexes) # Mezcla y toma los primeros <clusters> elementos
    centroids = data[indexes] # Inicializa centroides
    centroids = centroids[:, None] # Agrega dimensión para broadcasting

    for i in range(iter): # Cantidad de iteraciones
        # Calcular la distancia de cada vector a cada centroide
        distances = np.sqrt((data - centroids)**2)
        # Asigna clase según centroide más cercano
        classification = np.argmin(distances, axis=)
        for c in range(clusters): # Se actualizan los centroides uno a uno
            centroids[c] = np.mean(data[classification == c], axis=0)
            
    # Última actualización de clases con centroides finales
    distances = np.sqrt((data - centroids)**2)
    classification = np.argmin(distances, axis=0)

    return classification, centroids


#output = kmeans(clusters = 5, data = data, iter = 10)