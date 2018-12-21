import numpy as np
from psquare.psquare import PSquare

NB_ITERATIONS = 100


def random_generator():
    return np.random.normal(0, 1, 1)


def exact_value_for_quantile(values, quantile):
    return np.percentile(values, quantile)


def main():
    values = [random_generator() for _ in range(10)]
    quantile_to_estimate = 95

    psquare = PSquare(quantile_to_estimate)
    estimated_quantiles = []

    for val in values:
        psquare.update(val)

    for _ in range(NB_ITERATIONS):
        new_val = random_generator()
        values.append(new_val)

        psquare.update(new_val)
        estimated_quantiles.append(psquare.p_estimate())


if __name__ == '__main__':
    main()
