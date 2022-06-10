import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
from scipy.stats import norm
from EM_Numpy import EMScalar
from SyntheticDataset import SyntheticDataset
from metrics import Accuracy, Precision, Recall
from k_means_numpy import k_means, k_means_classify

sns.set()

# Data preparation
mu = np.array([5, 10])
var = np.array([15, 2])
p = 0.25
dataset = SyntheticDataset(mu, var, p, 500)
x_train, x_test, y_train, y_test = dataset.split(0.8)

# Histogram
sns.set(color_codes=True)
sns.distplot(x_train, hist=True, rug=True)
plt.show()

x_train = x_train.reshape(-1, 1)
x_test = x_test.reshape(-1, 1)

# Model fit and predict
EM = EMScalar()
EM.fit(x_train, y_train)
predictions = EM.predict(x_test)

# Results and Metrics
print("Expectation Maximization")
print("Means: ")
print(EM.model['mu'])
print("Covariance: ")
print(EM.model['cov'])
print("Probabilities: ")
print(EM.model['p'])
metrics = [Precision(), Accuracy(), Recall()]
for metric in metrics:
    print('{metric}: {value}'.format(metric=metric.__class__.__name__, value=metric(y_test, predictions)))

# K-means
print("K-means")
centers, ids = k_means(x_train, 2)
k_predictions = k_means_classify(x_test, centers)
for metric in metrics:
    print('{metric}: {value}'.format(metric=metric.__class__.__name__, value=metric(y_test, k_predictions)))

# Plots
mpl.rc_file_defaults()
f, (ax, bx, cx) = plt.subplots(3, 1, sharey='col', sharex='col')

ax.scatter(x_test[:, 0], np.zeros_like(x_test), c=y_test, alpha=1)
xr_1 = np.linspace(mu[0] - 3 * var[0], mu[0] + 3 * var[0], 100)
xr_2 = np.linspace(mu[1] - 3 * var[1], mu[1] + 3 * var[1], 100)
density_r1 = norm.pdf(xr_1, loc=mu[0], scale=var[0])
density_r2 = norm.pdf(xr_2, loc=mu[1], scale=var[1])
ax.fill_between(xr_1, density_r1, alpha=0.4)
ax.fill_between(xr_2, density_r2, alpha=0.4)
ax.text(mu[0] - 1 * var[0], 0.1, 'Mean = {media}\n Stdv:{std}'.format(media=mu[0], std=var[0]))
ax.text(mu[1] + 1 * var[1], 0.1, 'Mean = {media}\n Stdv:{std}'.format(media=mu[1], std=var[1]))
ax.set_title('Valores reales')

bx.scatter(x_test[:, 0], np.zeros_like(x_test), c=predictions, alpha=1)
x_1 = np.linspace(EM.model['mu'][0] - 3 * (EM.model['cov'][0] ** 0.5),
                  EM.model['mu'][0] + 3 * (EM.model['cov'][0] ** 0.5), 100)
x_2 = np.linspace(EM.model['mu'][1] - 3 * (EM.model['cov'][1] ** 0.5),
                  EM.model['mu'][1] + 3 * (EM.model['cov'][1] ** 0.5), 100)
density_1 = norm.pdf(x_1[:, 0], loc=EM.model['mu'][0], scale=EM.model['cov'][0] ** 0.5)
density_2 = norm.pdf(x_2[:, 0], loc=EM.model['mu'][1], scale=EM.model['cov'][1] ** 0.5)
bx.fill_between(x_1[:, 0], density_1, alpha=0.4)
bx.fill_between(x_2[:, 0], density_2, alpha=0.4)
bx.set_title('Predicciones EM')
bx.text(EM.model['mu'][0] - 1 * EM.model['cov'][0] ** 0.5, 0.1,
        'Mean = {media}\n Stdv:{std}'.format(media=EM.model['mu'][0], std=EM.model['cov'][0] ** 0.5))
bx.text(EM.model['mu'][1] + 1 * EM.model['cov'][1] ** 0.5, 0.1,
        'Mean = {media}\n Stdv:{std}'.format(media=EM.model['mu'][1], std=EM.model['cov'][1] ** 0.5))

cx.scatter(x_test[:, 0], np.zeros_like(x_test), c=k_predictions, alpha=1)
cx.set_title('Predicciones K-means')
cx.annotate('Centroide 1', xy=(centers[0], 0), xytext=(centers[0], 0.2),
            arrowprops=dict(facecolor='black', shrink=0.03))
cx.annotate('Centroide 2', xy=(centers[1], 0), xytext=(centers[1], 0.2),
            arrowprops=dict(facecolor='black', shrink=0.03))

plt.show()

# Iteration over different variances
list_var = np.linspace(1, 20, 100)
ovl = np.zeros_like(list_var)
metric_ovl = np.zeros((ovl.shape[0], 3))
EM_iter = EMScalar()

for i in range(list_var.shape[0]):

    idx = np.random.randint(0, list_var.shape[0], 4)

    mu = np.array([5, 10])
    var = np.array([15, list_var[i]])
    mu = mu.reshape(-1, 1)
    var = var.reshape(-1, 1)

    dataset = SyntheticDataset(mu, var, 0.25, 500)
    x_train, x_test, y_train, y_test = dataset.split(0.8)
    x_train = x_train.reshape(-1, 1)
    x_test = x_test.reshape(-1, 1)
    ovl[i] = dataset.overlap()

    EM_iter.fit(x_train, y_train)
    predictions = EM_iter.predict(x_test)

    for j, metric in enumerate(metrics):
        metric_ovl[i, j] = metric(y_test, predictions)

index = np.argsort(ovl, axis=0)

f, (ax, bx, cx) = plt.subplots(3, 1, sharex='col')
ax.scatter(list_var, metric_ovl[:, 0])
ax.set_title('Precision vs Variance of different sintetic datasets. Means = [5, 10]. Var[15, X]')
ax.set_xlabel('Variance of Second Normal Distribution')
ax.set_ylabel('Precision')

bx.scatter(list_var, metric_ovl[:, 1])
bx.set_title('Accuracy vs Variance of different sintetic datasets. Means = [5, 10]. Var[15, X]')
bx.set_xlabel('Variance of Second Normal Distribution')
bx.set_ylabel('Accuracy')

cx.scatter(list_var, metric_ovl[:, 2])
cx.set_title('Recall vs Variance of different sintetic datasets. Means = [5, 10]. Var[15, X]')
cx.set_xlabel('Variance of Second Normal Distribution')
cx.set_ylabel('Recall')

plt.show()
