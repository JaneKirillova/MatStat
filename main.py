import numpy as np
import matplotlib.pyplot as plt
from math import factorial

THETA = 1
S = 100
N = 1000
MAX_K = 100


def generate_uniform_distribution():
    return np.random.uniform(0, THETA, N)


def generate_exponential_distribution():
    return np.random.exponential(1 / THETA, N)


def count_theta_uniform(k, m_k):
    return ((k + 1) * m_k) ** (1 / k)


def count_theta_exponential(k, m_k):
    return (m_k / factorial(k)) ** (1 / k)


def count_m_k(array_of_values, function):
    return sum([function(x) for x in array_of_values]) / len(array_of_values)


def count_standard_derivation(k, generation_function, count_theta_function):
    result = 0
    for i in range(S):
        X = generation_function()
        m_k = count_m_k(X, lambda x: x ** k)
        new_theta = count_theta_function(k, m_k)
        result += (THETA - new_theta) ** 2
    return (result / S) ** 0.5


def make_graph(path, generate_function, count_theta_function):
    k_values = range(1, MAX_K)
    standard_derivation = [count_standard_derivation(k, generate_function, count_theta_function) for k in k_values]
    plt.clf()
    plt.plot(k_values, standard_derivation, color='blue')
    plt.xlabel("k")
    plt.ylabel("standard derivation")
    plt.grid()
    plt.savefig(path)


make_graph("uniform.png", generate_uniform_distribution, count_theta_uniform)
make_graph("exponential.png", generate_exponential_distribution, count_theta_exponential)
