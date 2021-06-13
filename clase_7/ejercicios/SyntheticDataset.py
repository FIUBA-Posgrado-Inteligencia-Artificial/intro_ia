import numpy as np


class SyntheticDataset(object):

    def __init__(self, mu, var, p, n_samples):
        n_uniform = np.random.uniform(0, 1, n_samples)
        x = np.zeros(n_uniform.shape)
        y = np.zeros(n_uniform.shape)
        # noise_a = np.random.normal(mu[0], var[0], x[n_uniform <= p].shape[0])
        # noise_b = np.random.normal(mu[1], var[1], x[n_uniform > p].shape[0])
        x[n_uniform <= p] = np.random.normal(mu[0], var[0], x[n_uniform <= p].shape[0])
        x[n_uniform > p] = np.random.normal(mu[1], var[1], x[n_uniform > p].shape[0])
        y[n_uniform <= p] = 0
        y[n_uniform > p] = 1
        self.x = x
        self.y = y
        self.mu = mu
        self.var = var

    def split(self, percentage):  # 0.8
        X = self.x
        y = self.y

        permuted_idxs = np.random.permutation(X.shape[0])
        train_idxs = permuted_idxs[0:int(percentage * X.shape[0])]
        test_idxs = permuted_idxs[int(percentage * X.shape[0]): X.shape[0]]

        X_train = X[train_idxs]
        X_test = X[test_idxs]

        y_train = y[train_idxs]
        y_test = y[test_idxs]

        return X_train, X_test, y_train, y_test

    def overlap(self):
        x_0 = self.x[self.y == 0]
        x_1 = self.x[self.y == 1]
        mu = self.mu
        std = self.var ** 0.5
        ov_1 = np.sum(np.logical_and(x_1 > (mu[0] - 1 * std[0]), x_1 < (mu[0] + 1 * std[0])), axis=0)
        ov_2 = np.sum(np.logical_and(x_0 > (mu[1] - 1 * std[1]), x_0 < (mu[1] + 1 * std[1])), axis=0)
        return (ov_1 + ov_2) / self.x.shape[0]
