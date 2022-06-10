import numpy as np
from scipy.stats import multivariate_normal
from models import BaseModel


class EMScalar(BaseModel):
    def fit(self, X, y):

        MAX_IT = 500

        # Dimensions
        n = X.shape[0]
        k = 2

        # Parameters initialization
        p = np.random.uniform(0, 1, (k, 1))
        p = p / np.sum(p, axis=0)
        means = np.random.uniform(np.min(X), np.max(X), (k, 1))
        covariance = np.sum((np.hstack((X, X))-means.T)**2, axis=0)/(X.shape[0]-1)
        covariance = covariance.reshape(-1, 1)
        Nij = np.zeros((n, k))
        Eij = np.zeros((n, k))
        Eij_ant = np.zeros((n, k))

        i = 0
        delta = False
        tol = 1E-5
        for j in range(k):
            Nij[:, j] = multivariate_normal.pdf(X, means[j], covariance[j])

        # Execution Loop
        while not (delta or i > MAX_IT):
            Eij_ant[:, :] = Eij
            for j in range(k):
                Eij[:, j] = (p[j] * Nij[:, j]) / (Nij @ p)[:, 0]
                means[j] = (Eij[:, j].dot(X)) / np.sum(Eij[:, j], axis=0)
                covariance[j] = Eij[:, j].dot((X - means[j]) * (X - means[j])) / np.sum(Eij[:, j])
                p[j] = np.mean(Eij[:, j])
                Nij[:, j] = multivariate_normal.pdf(X, means[j], covariance[j])
            delta = np.allclose(Eij_ant, Eij, rtol=tol)
            i = i + 1
        idx = np.argsort(means[:, 0], axis=0)
        self.model = {'mu': means[idx, :], 'cov': covariance[idx, :], 'p': p[idx, :]}

    def predict(self, X):
        k = self.model['mu'].shape[0]
        N = np.zeros((X.shape[0], k))
        E = np.zeros((X.shape[0], k))

        for i in range(k):
            N[:, i] = multivariate_normal.pdf(X, self.model['mu'][i, 0], self.model['cov'][i, 0])
        for i in range(k):
            E[:, i] = (self.model['p'][i, 0] * N[:, i]) / (N @ self.model['p'])[:, 0]
        idx = np.argmax(E, axis=1)
        return idx
