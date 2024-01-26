import time
import numpy as np
import matplotlib.pyplot as plt
from dataset_income import Data
from metrics import MSE
from models import ConstantModel, LinearRegression, LinearRegressionWithB
from gradient_descent import stochastic_gradient_descent, gradient_descent, mini_batch_gradient_descent


if __name__ == '__main__':
    dataset = Data(r'C:\Users\Lautaro\PycharmProjects\ceia_intro_a_IA\clase_3\ejercicios\data\income.csv')

    X_train, X_test, y_train, y_test = dataset.split(0.8)

    linear_regression = LinearRegression()
    linear_regression.fit(X_train, y_train)
    lr_y_hat = linear_regression.predict(X_test)

    linear_regression_b = LinearRegressionWithB()
    linear_regression_b.fit(X_train, y_train)
    lrb_y_hat = linear_regression_b.predict(X_test)

    constant_model = ConstantModel()
    constant_model.fit(X_train, y_train)
    ct_y_hat = constant_model.predict(X_test)

    mse = MSE()
    lr_mse = mse(y_test, lr_y_hat)
    lrb_mse = mse(y_test, lrb_y_hat)
    ct_mse = mse(y_test, ct_y_hat)

    x_plot = np.linspace(0, 10, 10)
    lr_y_plot = linear_regression.model * x_plot
    lrb_y_plot = linear_regression_b.model[0] * x_plot + linear_regression_b.model[1]

    # gradient descent
    print('\n\n\nGRADIENT DESCENT VS LINEAR REGRESSION')
    lr_1 = 0.001
    amt_epochs_1 = 1000
    start = time.time()
    W_manual = gradient_descent(X_train.reshape(-1, 1), y_train.reshape(-1, 1), lr=lr_1, amt_epochs=amt_epochs_1)
    time_1 = time.time() - start
    W_real = linear_regression.model
    print('W_manual:  {}\nW_real:    {}\nManual time [s]: {}'.format(W_manual.reshape(-1), W_real, time_1))

    # gradient descent with b
    print('\n\n\nGRADIENT DESCENT VS LINEAR REGRESSION WITH B')
    X_expanded = np.vstack((X_train, np.ones(len(X_train)))).T
    lr_2 = 0.001
    amt_epochs_2 = 100000
    start = time.time()
    W_manual = gradient_descent(X_expanded, y_train.reshape(-1, 1), lr=lr_2, amt_epochs=amt_epochs_2)
    time_2 = time.time() - start
    W_real = linear_regression_b.model
    print('W_manual:  {}\nW_real:    {}\nManual time [s]: {}'.
          format(W_manual.reshape(-1), W_real, time_2))

    # stochastic gradient descent
    print('\n\n\nSTOCHASTIC GRADIENT DESCENT VS LINEAR REGRESSION WITH B')
    X_expanded = np.vstack((X_train, np.ones(len(X_train)))).T
    lr_3 = 0.05
    amt_epochs_3 = 1000
    start = time.time()
    W_manual = stochastic_gradient_descent(X_expanded, y_train.reshape(-1, 1), lr=lr_3, amt_epochs=amt_epochs_3)
    time_3 = time.time() - start
    W_real = linear_regression_b.model
    print('W_manual:  {}\nW_real:    {}\nManual time [s]: {}'.
          format(W_manual.reshape(-1), W_real, time_3))

    # Mini batch gradient descent
    print('\n\n\nMINI BATCH GRADIENT DESCENT VS LINEAR REGRESSION WITH B')
    X_expanded = np.vstack((X_train, np.ones(len(X_train)))).T
    lr_4 = 0.05
    amt_epochs_4 = 10000
    start = time.time()
    W_manual = mini_batch_gradient_descent(X_expanded, y_train.reshape(-1, 1), lr=lr_4, amt_epochs=amt_epochs_4)
    time_4 = time.time() - start
    W_real = linear_regression_b.model
    print('W_manual:  {}\nW_real:    {}\nManual time [s]: {}'.
          format(W_manual.reshape(-1), W_real, time_4))

    # PLOTS
    plt.figure()
    x_plot = np.linspace(1, 4, 4)
    legend = ['GD', 'GD(B)', 'S-GD(B)', 'MB-GD(B)']

    plt.subplot(1, 3, 1)
    plt.gca().set_title('Learning Rate')
    y_plot = [lr_1, lr_2, lr_3, lr_4]
    plt.plot(x_plot[0], y_plot[0], 'o', x_plot[1], y_plot[1], 'o', x_plot[2], y_plot[2], 'o',
             x_plot[3], y_plot[3], 'o')
    plt.legend(legend)
    for x, y in zip(x_plot, y_plot):
        plt.text(x, y, str(y))

    plt.subplot(1, 3, 2)
    plt.gca().set_title('Epochs')
    y_plot = [amt_epochs_1, amt_epochs_2, amt_epochs_3, amt_epochs_4]
    plt.plot(x_plot[0], y_plot[0], 'o', x_plot[1], y_plot[1], 'o', x_plot[2], y_plot[2], 'o',
             x_plot[3], y_plot[3], 'o')
    plt.legend(legend)
    for x, y in zip(x_plot, y_plot):
        plt.text(x, y, str(y))

    plt.subplot(1, 3, 3)
    plt.gca().set_title('Time')
    y_plot = [time_1, time_2, time_3, time_4]
    plt.plot(x_plot[0], y_plot[0], 'o', x_plot[1], y_plot[1], 'o', x_plot[2], y_plot[2], 'o',
             x_plot[3], y_plot[3], 'o')
    plt.legend(legend)
    for x, y in zip(x_plot, y_plot):
        plt.text(x, y, str(y))

    plt.show()
