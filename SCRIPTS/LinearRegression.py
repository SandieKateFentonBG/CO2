import numpy as np


class LinReg:
    def __init__(self, theta=None, regul=1):
        self.regul = regul
        self.theta = theta

    def calibration(self, x, y):
        # Calculate the regularized pseudo_inverse of A
        # todo : understand why i get a singular matrix when integrating my xQuali for a regularisation/parameter study
        # todo :> why should i replace np.linalg.inv by np.linalg.pinv - what's the differnece?
        # todo :  https://stackoverflow.com/questions/10326015/singular-matrix-issue-with-numpy

        try:
        # your code that will (maybe) throw
            pinv = np.matmul(np.linalg.inv(np.add(np.matmul(x.T, x), self.regul * np.identity(np.shape(x)[1]))), x.T)
            #print('used : np.linalg.inv')
        except np.linalg.LinAlgError as e:
            if 'Singular matrix' in str(e):
                # your error handling block
                pinv = np.matmul(np.linalg.pinv(np.add(np.matmul(x.T, x), self.regul * np.identity(np.shape(x)[1]))), x.T)
                #print('used : np.linalg.pinv')
            else:
                raise
        self.theta = np.matmul(pinv, y)

    def prediction(self, x):
        if self.theta is None:
            print("Model has no theta")
            return
        return np.matmul(x, self.theta)

    def evaluation(self, x, y, method, tolerance=0.05):
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
