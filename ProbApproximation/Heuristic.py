import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

class Queue():
    def __init__(self, x0):
        self.x0 = x0


class MM1_Queue(Queue):
    def __init__(self, x0, a, b, b_):
        super().__init__(x0)
        self.alpha = a
        self.beta = b
        self.dist = stats.rv_discrete(name='mm1_queue', values=((1, -1), (self.alpha, self.beta)))
        self.lambda_b = self.lambda_b_calc(b_)

    def first_hitting_time(self, b, max_steps=10000, x0=0, alpha=0, beta=0):
        if x0 == 0:
            x0 = self.x0

        if (alpha == 0) | (beta == 0):
            dist = self.dist
        else:
            dist = stats.rv_discrete(name='mm1_queue', values=((1, -1), (alpha, beta)))

        pos = x0
        for i in range(max_steps):
            pos = pos + dist.rvs()
            if pos < 0:
                pos = 0
            if pos == b:
                return i

        return 0

    def lambda_b_calc(self, b):
        return pow(self.beta, -1)*pow((self.beta - self.alpha), 2)*pow((self.alpha/self.beta), b)


if __name__ == '__main__':
    q = MM1_Queue(10, 0.51, 0.49, 750)
    t = []
    print(q.lambda_b)
    print(1/q.lambda_b)
    for i in range(10000):
        print(i)
        t.append(q.first_hitting_time(750, 70000))
    plt.hist(t, bins=20)
    plt.show()





