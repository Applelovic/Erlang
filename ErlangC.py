import pandas as pd
import numpy as np
import math


class ErlangC:

    def __init__(
            self,
            lmbd: float,  # mean arrival rate of customers into the system
            s_bar: float,  # Expected customer service time
            n_agents: int,  # number of agents
    ):
        self.lmbd = lmbd
        self.s_bar = s_bar
        self.n_agents = n_agents
        self.rho = self.lmbd * self.s_bar  # traffic intensity or offered load, mean number of busy servers
        self.a = self.rho / self.n_agents  # server utilization

    @property
    def p_0(self):
        part_1 = np.sum([self.rho ** k / math.factorial(k) for k in range(0, self.n_agents)])
        part_2 = self.rho ** self.n_agents / math.factorial(self.n_agents) / (1 - self.a)
        return np.reciprocal(part_1 + part_2)

    @property
    def p_waiting(self):
        numerator = self.rho ** self.n_agents / math.factorial(self.n_agents - 1) / (self.n_agents - self.rho)
        denominator = np.sum(
            [
                self.rho ** k / math.factorial(k) for k in range(0, self.n_agents)
            ]
        ) + numerator
        return numerator / denominator


if __name__ == '__main__':

    tst = ErlangC(lmbd=6, )






