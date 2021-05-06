import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler


def pca_numpy(X, n_components=2):
    """
    :param X: numpy array con los datos a reducir
    :param n_components: n° de componentes principales a utilizar
    :return: autovalores, PCA sobre X para el n° de componentes
    """
    X = X - X.mean(axis=0)
    cov = np.cov(X.T)/X.shape[0]
    # v son los autovalores y w los autovectores
    v, w = np.linalg.eig(cov)
    idx = v.argsort()[::-1]
    v = v[idx]
    w = w[:, idx]
    return v[:n_components], X.dot(w[:, :n_components])


if __name__ == '__main__':
    # ndarray de prueba
    x = np.array([[0.8, 0.7], [0.1, -0.1]])
    pca = PCA(n_components=1)
    x_std = StandardScaler(with_std=False).fit_transform(x)
    x_pca_sk = pca.fit_transform(x_std)
    x_pca_np = pca_numpy(x, 1)
    print("Resultado PCA con Scikit-learn:{}".format(x_pca_sk))
    print("Resultado PCA con Numpy:{}".format(x_pca_np))
    np.testing.assert_allclose(x_pca_sk, x_pca_np[1])
