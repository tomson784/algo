import numpy as np

n_in = 0
n_iter = 1000000
print_step = 1000

for i in range(1, n_iter + 1):
    x, y = np.random.uniform(-1.0, 1.0, 2)
    if x**2 + y**2 <= 1:
        n_in += 1

    if i % print_step == 0:
        print("{} {}".format(i, n_in / i))

print(n_in / n_iter)
print("3.14 / 4.0 = {}".format(3.14 / 4.0))
