import numpy as np
import matplotlib.pyplot as plt

class BrownianMotion:
    def __init__(self, mu=0, sigma=1, T=1, n=1):
        self.mu = mu
        self.sigma = sigma
        self.T = T
        self.n = n

    def generate_bm(self):
        p = list(np.random.normal(self.mu, self.sigma, self.n))
        return np.cumsum(p)

    def generate_bm_path(self, ret_t: bool = False):
        t = [i * self.T / self.n for i in range(0, self.n+1)]
        w = [0]
        for i in range(1, self.n + 1):
            w.append(w[i - 1] + self.mu*(t[i] - t[i - 1]) + self.sigma*np.sqrt(t[i] - t[i - 1])*np.random.normal())
        if ret_t:
            return t, w
        else:
            return w



if __name__ == '__main__':
    bm = BrownianMotion(n=10000)
    plt.figure(figsize=(10, 10))
    plt.plot(bm.generate_bm_path())
    plt.show()