import numpy as np

MAX_ITERATIONS = 10


def k_means(X, n_clusters):
    centroids = np.eye(n_clusters, X.shape[1])
    print(centroids)
    for i in range(MAX_ITERATIONS):
        print("Iteration # {}".format(i))
        centroids, cluster_ids = k_means_loop(X, centroids)
        print(centroids)
    return centroids, cluster_ids


def k_means_loop(X, centroids):
    # encontrar el label de cada fila de X en función de los centroides
    expanded_centroids = centroids[:, None]
    distances = np.sqrt(np.sum((expanded_centroids - X) ** 2, axis=2))
    arg_min = np.argmin(distances, axis=0)

    # redeterminar los centroides
    for i in range(centroids.shape[0]):
        centroids[i] = np.mean(X[arg_min == i, :], axis=0)

    return centroids, arg_min
