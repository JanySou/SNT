import numpy as np
import matplotlib.pyplot as plt

t = 0.066 * np.arange(11)
x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 4, 9, 16, 25])
plt.plot(x, y, "ro", label="y=f(x)")
plt.xlabel("xreelle")
plt.ylabel("yreelle")
plt.grid()
plt.legend()
plt.title("Trajectoire de la balle")
plt.show()

print("truc")


test2
