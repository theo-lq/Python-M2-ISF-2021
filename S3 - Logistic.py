import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns; sns.set(style="ticks")




r = 2.8
logistic = lambda x: r * x * (1 -x)





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






def double_vector(vector):
    doubled_vector = []
    
    for i in range(len(vector)):
        doubled_vector.extend([vector[i], vector[i]])
    
    return doubled_vector[:2*len(vector)-1], doubled_vector[1:]






def plot_suite(sequence):
    abscissa = [iteration for iteration in range(len(sequence))]
    
    sns.despine()
    plt.plot(abscissa, sequence, 'o-', c="blue")

    if r>=1 and r<=3:
        limit = [1-1/r for i in abscissa]
        plt.plot(abscissa, limit, c="black", linestyle=":", label="Theoric limit")

    plt.legend()
    plt.title("Sequence limit")






def plot_recurrence(sequence):
    x = np.linspace(0, 1, 100)

    sns.despine()
    plt.plot(x, x, c="red")
    plt.plot(x, logistic(x), c="blue")

    X, Y = double_vector(sequence)
    plt.plot(X, Y, c='black')

    plt.title("Sequence value")









#Visualisation ---------------------------------------

sequence = sequence_generator(15, logistic)

plt.subplot(1,2,1)
plot_recurrence(sequence)

plt.subplot(1,2,2)
plot_suite(sequence)

plt.suptitle("Logistic sequence for r=%0.2f" % r)
plt.show()
