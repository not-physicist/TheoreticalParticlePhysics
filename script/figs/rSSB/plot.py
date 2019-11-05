import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 25})

def v(x, mu2):
    l = 1
    return x**2*(mu2/2.0 + l*x**2/4.0)


x = np.linspace(-10, 10, 1000)
plt.figure(figsize=(15, 10))
plt.plot(x, v(x, -30))
plt.plot(x, v(x, 30))
plt.axis("off")
ax = plt.gca()
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

plt.savefig("./rSSB.eps", bbox_inches="tight")
