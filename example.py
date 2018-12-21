import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import time

from psquare.psquare import PSquare

NB_ITERATIONS = 30000


def random_generator():
    return np.random.normal(0, 1, 1)


def exact_value_for_quantile(values, quantile):
    return np.percentile(values, quantile)


def main():
    values = [random_generator() for _ in range(5)]
    quantile_to_estimate = 95

    psquare = PSquare(quantile_to_estimate)
    exact_quantiles = []
    estimated_quantiles = []
    psquare_exec_time = []
    numpy_exec_time = []

    for val in values:  # p square algorithm necessitates 5 values to start
        psquare.update(val)

    for _ in range(NB_ITERATIONS):
        new_val = random_generator()
        values.append(new_val)

        psquare_start = time.time()
        psquare.update(new_val)
        estimated_quantiles.append(psquare.p_estimate())
        psquare_end = time.time()

        numpy_start = time.time()
        exact_quantiles.append(exact_value_for_quantile(values, quantile_to_estimate))
        numpy_end = time.time()

        psquare_exec_time.append(psquare_end - psquare_start)
        numpy_exec_time.append(numpy_end - numpy_start)

    matplotlib.rc('figure', figsize=(10, 5))
    errors = np.abs(np.array(estimated_quantiles) - np.array(exact_quantiles))
    plt.plot(errors)
    plt.title('Absolute error between p-square predicted value and exact percentile value')
    plt.ylabel('Difference between exact percentile value and p-square estimation')
    plt.xlabel('Size of the dataset')
    plt.rcParams["figure.figsize"] = (10, 5)
    plt.show()

    plt.plot(psquare_exec_time[1:], label='p-square')
    plt.plot(numpy_exec_time[1:], label='numpy percentile')
    plt.title('Execution time to compute percentile on a growing dataset')
    plt.ylabel('Execution time (in seconds)')
    plt.xlabel('Size of the dataset')
    plt.legend()
    plt.rcParams["figure.figsize"] = (10, 5)
    plt.show()


if __name__ == '__main__':
    main()
