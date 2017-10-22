# coding = utf-8
from sklearn import datasets
import numpy as np
import pylab as plt

def get_z(x, w, b):
    return np.dot(w.T, x) + b

def sigma(z):
    return 1.0/(1.0+np.exp(-z))

def loss_func(y, ymodel):
    return -( y*np.log(ymodel) + (1.0-y)*np.log(1.0-ymodel) )
def cost_func(ys, ymodels):
    cost_mean = np.mean( loss_func(ys, ymodels) )
    return cost_mean



if __name__ == '__main__':

    def train():
        global w, b
        z_trains = get_z(train_samples, w, b)
        sigms = sigma(z_trains)
        dz = sigms - train_labels
        dw = np.dot(train_samples, dz.T) / n_train_samples
        db = np.mean(dz)

        w += -learn_rate * dw
        b += -learn_rate * db

    learn_rate = 0.001
    dataAll = datasets.load_breast_cancer()
    data = dataAll["data"].T
    labels = dataAll["target"]
    n_features, n_samples = data.shape

    w = np.zeros(shape=(n_features, 1), dtype=float)
    b = 0.0


    n_train_samples = 10
    np.random.seed(100)
    idx = np.random.choice(range(n_samples), n_train_samples)

    all_idx = range(n_samples)
    test_idx = [i for i in all_idx if i  not in idx]
    test_samples = data[:, test_idx]
    test_labels = labels[test_idx]

    train_samples = data[:, idx]
    train_labels = labels[idx]

    tran_steps = 100
    cost_data = []

    for i in range(tran_steps):
        print(i)
        train()
        train_cost = cost_func(train_labels, sigma(get_z(train_samples, w, b)))
        print(train_cost)

        # train_cost = cost_func(train_labels ,sigma(get_z(train_samples, w, b)))
        # test_cost = cost_func(test_labels, sigma(get_z(test_samples, w, b)))
        # cost_data.append( train_cost )

    # cost_data = np.array(cost_data)
    # plt.figure()
    # plt.plot(cost_data, "b--")
    # plt.plot(cost_data[:, 0], cost_data[:, 2], "r-")
    # plt.show()
    pass




