# 
#  penalty_function.py
#  @author kukimukiku
#  Penalty function & optimization
#  

import math

def penalty_function(x, y, z, r):
    return -(x * y * z) + r * ((max(x ** 2) + max(y ** 2) + max(z ** 2) + (2 * x * y + 2 * x * z + 2 * y * z - 1) ** 2))

def max(x):
    if -x > 0:
        return x
    else:
        return 0

def derivatives(x, y, z, r):
    temp_x = -(y * z) + r * (derivative_for_max(2 * x) + 4 * ((2 * x * y + 2 * x * z + 2 * y * z) - 1) * (y + z))
    temp_y = -(x * z) + r * (derivative_for_max(2 * y) + 4 * ((2 * x * y + 2 * x * z + 2 * y * z) - 1) * (x + z))
    temp_z = -(x * y) + r * (derivative_for_max(2 * z) + 4 * ((2 * x * y + 2 * x * z + 2 * y * z) - 1) * (x + y))
    return [temp_x] + [temp_y] + [temp_z]

def derivative_for_max(x):
    if -x > 0:
        return x
    else:
        return 0

def gradient_descent_method(x, y, z, r, i):
    while True:
        X = derivatives(x, y, z, r)
        x = x - 0.0001 * X[0]
        y = y - 0.0001 * X[1]
        z = z - 0.0001 * X[2]
        i += 1
        if math.sqrt(X[0] ** 2 + X[1] ** 2 + X[2] ** 2) < 0.0001:
            break
    return [x] + [y] + [z] + [i]

# Count minimum using gradient descent and penalty function
def min_with_penalty(x, y, z):
    # Gradient descent iteration
    gd_iteration = 0
    i = 0
    r = 1
    while True:
        X = gradient_descent_method(x, y, z, r, gd_iteration)
        x = X[0]
        y = X[1]
        z = X[2]
        gd_iteration = X[3]
        print("\nPenalty function iteration - ", i, ":")
        print("     f(X) - %.8f" % penalty_function(x, y, z, r))
        print("     Gradient descent iteration - ", gd_iteration)
        r = r * 2.5
        i += 1
        gd_iteration = 0
        if r * ((max(x ** 2) + max(y ** 2) + max(z ** 2) + (2 * x * y + 2 * x * z + 2 * y * z - 1) ** 2)) < 0.001:
            break

    print("-----------------")
    print("%.8f %.8f %.8f" % (x, y, z))
    print("f(X) - %.8f" % penalty_function(x, y, z, r))
    print("Iterations total - ", i)


if __name__ == '__main__':
    print("\nX(1, 1, 1)")
    min_with_penalty(1, 1, 1)
    print("\n\nX(0.8, 0.9, 0.6)")
    min_with_penalty(0.8, 0.9, 0.6)
