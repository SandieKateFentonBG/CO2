import numpy as np


class LinReg:
    def __init__(self, theta=None, regul=1):
        self.regul = regul
        self.theta = theta

    def calibration(self, x, y):
        # Calculate the regularized pseudo_inverse of A
        pinv = np.matmul(np.linalg.inv(np.add(np.matmul(x.T, x), self.regul * np.identity(np.shape(x)[1]))), x.T)
        # fit the regularized polynomial to find optimal theta matrix
        self.theta = np.matmul(pinv, y)

    def prediction(self, x):
        if not self.theta:
            print("Model has no theta")
            return
        return np.matmul(x, self.theta)

    def evaluation(self, x, y, method='mse', tolerance=0.05):
        pred = self.prediction(x)
        if method == 'mse':
            # Calculate the mean square error between the prediction and reference vectors
            return 0.5 * np.mean(np.square(pred - y))
        elif method == 'mae':
            # Calculate the mean absolute error between the prediction and reference vectors
            return np.mean(np.abs(pred - y))
        elif method == 'accuracy':
            validated = [1 if abs(pred[i]-y[i]) < abs(y[i])*tolerance else 0 for i in range(len(y))]
            return sum(validated) / len(validated)
