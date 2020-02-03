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

    def show_lil(self):
        pass

    def show_slln(self):
        pass

    def show_time_inversion(self):
        pass

class BrownianBridge(BrownianMotion):
    def __init__(self, T=1, n=1, x=0, y=1):
        super().__init__(0, 1, T, n)
        self.x = x
        self.y = y

    def generate_bb_path(self, ret_t: bool = False):
        s = [i * self.T / self.n for i in range(0, self.n + 1)]
        w = [self.x]
        for i in range(1, self.n):
            w.append((s[self.n] - s[i])*w[i - 1]/(s[self.n] - s[i - 1]) +
                     (s[i] - s[i - 1])*self.y/(s[self.n] - s[i - 1]) +
                     np.sqrt((s[self.n] - s[i])*(s[i] - s[i - 1])/(s[self.n] - s[i - 1]))*np.random.normal())
        w.append(self.y)
        if ret_t:
            return s, w
        else:
            return w

    def surface_calc(self, t, bb):
        delta = t[1] - t[0]
        surface = []
        for i in range(1, len(bb)):
            if bb[i - 1] > self.y:
                surface.append(delta*(bb[i - 1] - self.y))

        return sum(surface)




if __name__ == '__main__':
    bb = BrownianBridge(n=15000)
    s = []
    for i in range(20000):
        t, w = bb.generate_bb_path(True)
        s.append(bb.surface_calc(t, w))

    plt.hist(s, bins=25)
    plt.show()
    print(np.mean(s))
    print(np.std(s))