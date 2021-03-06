from abapy.materials import Hollomon
import matplotlib.pyplot as plt

E = 1.       # Young's modulus
sy = 0.001     # Yield stress
n = 0.15    # Hardening exponent
nu = 0.3
eps_max = .1 # maximum strain to be computed
N = 30      # Number of points to be computed (30 is a low value useful for graphical reasons, in real simulations, 100 is a better value).
mat1 = Hollomon(labels = 'my_material', E=E, nu=nu, sy=sy, n=n)
table1 = mat1.get_table(0, N=N, eps_max=eps_max)
eps1 = table1[:,0]
sigma1 = table1[:,1]
sigma_max1 = max(sigma1)

mat2 = Hollomon(labels = 'my_material', E=E, nu=nu, sy=sy, n=n, kind = 2)
table2 = mat2.get_table(0, N=N, eps_max=eps_max)
eps2 = table2[:,0]
sigma2 = table2[:,1]
sigma_max2 = max(sigma2)


plt.figure()
plt.clf()
plt.title('Hollomon tensile behavior: $n = {0:.2f}$, $\sigma_y / E = {1:.2e}$'.format(n, sy/E))
plt.xlabel('Strain $\epsilon$')
plt.ylabel('Stress $\sigma$')
plt.plot(eps1, sigma1, 'or-', label = 'Plasticity kind=1')
plt.plot(eps2, sigma2, 'vg-', label = 'Plasticity kind=2')
plt.plot([0., sy / E], [0., sy], 'b-', label = 'Elasticity')
plt.xticks([0., sy/E, eps_max], ['$0$', '$\epsilon_y$', '$\epsilon_{max}$'], fontsize = 16.)
plt.yticks([0., sy, sigma_max1], ['$0$', '$\sigma_y$', '$\sigma_{max}$'], fontsize = 16.)
plt.grid()
plt.legend(loc = "lower right")
plt.show()
