import numpy as np

def compute_steady_state_capital(beta, delta, alpha):
    'returns the steady state capital according to equation (2.12) and given production function'
    return ((1 / beta - 1 + delta) / alpha) ** (1 / (alpha - 1))

def make_grid(min, max, n):
    'returns a grid of n equally spaced points between min and max'
    return np.linspace(min, max, n)

def get_fasible_range_of_K(current_capital, alpha, delta):
    'returns the LB and UB of the feasible range of capital values for next period'
    return {'LB': (1 - delta) * current_capital, 'UB': current_capital ** alpha + (1 - delta) * current_capital}

def get_consumption(current_capital, next_capital, alpha, delta):
    'returns the consumption given current and next period capital'
    return current_capital ** alpha + (1 - delta) * current_capital - next_capital

def get_utility(consumption, sigma):
    'returns the utility of consumption'
    if (sigma == 1):
        return np.log(consumption)
    return (consumption ** (1 - sigma) - 1) / (1 - sigma)

def get_index_of_close_value(array, value):
    'returns the index of the closest value in the array to the given value'
    return np.abs(array - value).argmin()

def iterate(value_function_matrix, payoff_matrix, beta, epsilon, initial_grid_index, index_vector, k):
    k += 1

    if k > 1 and np.abs(value_function_matrix[k - 1] - value_function_matrix[k - 2]) < epsilon:
        k = 0
        return value_function_matrix, index_vector
    
    pair = np.amax(payoff_matrix + beta * value_function_matrix), np.argmax(beta * value_function_matrix)
    value_function_matrix[k + 1:] = pair[0]
    index_vector[i + 1] = pair[1]