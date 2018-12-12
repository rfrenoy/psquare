import numpy as np
import matplotlib.pyplot as plt

from psquare.psquare import PSquare

NB_ITERATIONS = 1000


def random_generator():
    return np.random.normal(0, 1, 1)


def exact_value_for_quantile(values, quantile):
    return np.percentile(values, quantile)


def main():
    values = [random_generator() for _ in range(10)]
    quantile_to_estimate = 95

    psquare = PSquare(quantile_to_estimate / 100.0)  # FIXME Use same notation as numpy, e.g. 95 and not 0.95
    exact_quantiles = []
    estimated_quantiles = []
    sum_errors = []

    for val in values:
        psquare.update(val)

    for _ in range(NB_ITERATIONS):
        new_val = random_generator()
        values.append(new_val)

        psquare.update(new_val)
        estimated_quantiles.append(psquare.p_estimate())
        exact_quantiles.append(exact_value_for_quantile(values, quantile_to_estimate))
        sum_errors.append(np.abs(estimated_quantiles[-1] - exact_quantiles[-1]))

    plt.plot(sum_errors)
    plt.show()


if __name__ == '__main__':
    main()
