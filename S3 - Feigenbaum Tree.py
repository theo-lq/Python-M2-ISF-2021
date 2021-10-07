import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns; sns.set(style="ticks")
    


def random_initialisation(low=0, high=1):
    start = np.random.uniform(low=low, high=high)
    while start == 0:
        start = np.random.uniform(low=low, high=high)
    return start




def sequence_generator(iteration, function, initial_value=None):
    sequence = [initial_value if initial_value != None else random_initialisation()]

    for index in range(1, iteration):
        sequence.append(function(sequence[index-1]))
    
    return sequence





def plot_feigenbaum_tree(r_iteration, depth=30, base_iteration=200):
    r_values = np.linspace(0, 4, r_iteration)
    for r in r_values:
        logistic = lambda x: r * x * (1 -x)
        sequence = sequence_generator(base_iteration + depth, logistic)
        plt.plot([r] * depth, sequence[-depth:], 'o', markersize=1, c="black", alpha=0.3)
    
    sns.despine()
    plt.xlabel("r values")
    plt.ylabel("Limits observed")
    plt.title("Feigenbaum tree")
    plt.show()
