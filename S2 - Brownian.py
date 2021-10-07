import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set(style="whitegrid")






def generate_brownian_motion(draw_number, step, initial_value):
    gaussian = np.random.normal(size=(step, draw_number))
    gaussian[0, :] = initial_value
    
    brownian = gaussian.cumsum(axis=0)
    return brownian





def generate_correlated_brownian_motion(step, initial_value, gamma):
    initial_gaussian = np.random.normal(size=(step, 1))
    initial_gaussian[0, :] = initial_value
    correlated_gaussian = gamma * initial_gaussian + np.sqrt(1 - (gamma**2)) * np.random.normal(size=(step, 1))
    correlated_gaussian[0, :] = initial_value
    
    brownian = initial_gaussian.cumsum(axis=0)
    correlated_brownian = correlated_gaussian.cumsum(axis=0)
    return brownian, correlated_brownian








def call(strike, premium=0, type="buy"):
    call_function = lambda x: (np.maximum(0, x - strike) - premium) * (1 if type == "buy" else -1)
    return call_function



def put(strike, premium=0, type="buy"):
    put_function = lambda x: (np.maximum(0, strike - x) - premium) * (1 if type == "buy" else -1)
    return put_function








def get_price(strike, initial_value, step=500, draw_number=100):
    brownian = generate_brownian_motion(draw_number=100, step=step, initial_value=initial_value)
    payoff = call(strike=strike)
    price = np.mean(payoff(brownian[-1, ]))
    print("The price is : €%0.2f" % price)
    return price



def print_example_price(strike, initial_value, step=500, draw_number=100):
    price = get_price(strike, initial_value, step=step, draw_number=draw_number)
    brownian = generate_brownian_motion(draw_number=20, step=step, initial_value=initial_value)
    plt.plot(brownian, alpha=0.6)
    plt.axhline(y=strike, lw=2, ls='--', c=sns.color_palette()[2], label="Strike")
    plt.legend()
    plt.title("Strike=%d, price=€%0.2f" % (strike, price))
    plt.show()




