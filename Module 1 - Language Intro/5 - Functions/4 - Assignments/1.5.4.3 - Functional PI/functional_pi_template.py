import math


def my_pi(target_error):
    """
    Implementation of Gauss–Legendre algorithm to approximate PI from https://en.wikipedia.org/wiki/Gauss%E2%80%93Legendre_algorithm

    :param target_error: Desired error for PI estimation
    :return: Approximation of PI to specified error bound
    """
    a = 1
    b = 1 / (math.sqrt(2))
    t = 0.25
    p = 1
    for i in range(1, 100):

        a1 = ((a + b) / 2)
        b1 = math.sqrt(a * b)
        p1 = 2 * p
        t1 = (t - (p * ((a1 - a) ** 2)))
        pi_estimate = ((a1 + b1) ** 2) / (4 * t1)
        a = a1
        b = b1
        p = p1
        t = t1

    # change this so an actual value is returned
    return pi_estimate




desired_error = 1E-10

approximation = my_pi(desired_error)

print("Solution returned PI=", approximation)

error = abs(math.pi - approximation)

if error < abs(desired_error):
    print("Solution is acceptable")
else:
    print("Solution is not acceptable")
