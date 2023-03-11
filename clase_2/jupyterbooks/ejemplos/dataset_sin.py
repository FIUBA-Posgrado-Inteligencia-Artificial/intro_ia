import numpy as np
import matplotlib.pyplot as plt
from models import ConstantModel, LinearRegression, LinearRegressionWithB


def sin_fitting_example():
    # y = sin(x)
    amt_points = 36
    x = np.linspace(0, 360, num=amt_points)
    y = np.sin(x * np.pi / 180.)
    noise = np.random.normal(0, .1, y.shape)
    noisy_y = y + noise

    X_train = x
    y_train = noisy_y

    regression = LinearRegression()

    # linear
    X_linear = np.vstack((X_train, np.ones(len(X_train)))).T
    regression.fit(X_linear, y_train.reshape(-1, 1))
    W_linear = regression.model
    y_linear = W_linear[0] * x + W_linear[1]

    # quadratic
    X_quadratic = np.vstack((np.power(X_train, 2), X_train, np.ones(len(X_train)))).T
    regression.fit(X_quadratic, y_train.reshape(-1, 1))
    W_quadratic = regression.model
    y_quadratic = W_quadratic[0] * np.power(x, 2) + W_quadratic[1] * x + W_quadratic[2]

    # cubic
    X_cubic = np.vstack((np.power(X_train, 3), np.power(X_train, 2), X_train, np.ones(len(X_train)))).T
    regression.fit(X_cubic, y_train.reshape(-1, 1))
    W_cubic = regression.model
    y_cubic = W_cubic[0] * np.power(x, 3) + W_cubic[1] * np.power(x, 2) + W_cubic[2] * x + W_cubic[3]

    # X10
    X_10 = np.vstack((np.power(X_train, 10), np.power(X_train, 9), np.power(X_train, 8),
                      np.power(X_train, 7), np.power(X_train, 6), np.power(X_train, 5),
                      np.power(X_train, 4), np.power(X_train, 3), np.power(X_train, 2),
                      X_train, np.ones(len(X_train)))).T
    regression.fit(X_10, y_train.reshape(-1, 1))
    W_10 = regression.model
    y_10 = W_10[0] * np.power(x, 10) + W_10[1] * np.power(x, 9) + W_10[2] * np.power(x, 8) + \
           W_10[3] * np.power(x, 7) + W_10[4] * np.power(x, 6) + W_10[5] * np.power(x, 5) + \
           W_10[6] * np.power(x, 4) + W_10[7] * np.power(x, 3) + W_10[8] * np.power(x, 2) + \
           W_10[9] * x + W_10[10]

    # PLOTS
    plt.figure()
    plt.subplot(1, 1, 1)
    plt.gca().set_title('Sin(x) - Fitting curves')

    # original
    plt.plot(x, noisy_y, 'o')

    # linear
    plt.plot(x, y_linear, '-')

    # quadratic
    plt.plot(x, y_quadratic, '-')

    # cubic
    plt.plot(x, y_cubic, '-')

    # 10 power
    plt.plot(x, y_10, '-')

    plt.legend(['noisy signal', 'linear', 'quadratic', 'cubic', '10th power'])
    plt.show()


if __name__ == '__main__':
    sin_fitting_example()