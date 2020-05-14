import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

xmin, xmax = 0, 5

def f(w, x):
    return w[0] + w[1] * x

# wの事前分布
mu_w = np.zeros(2)
var_w = 0.1
sigma_w = var_w * np.identity(2)
w_prior = stats.multivariate_normal.rvs(mean=mu_w, cov=sigma_w, size=10)
# wをプロット
plt.scatter(w_prior[:,0], w_prior[:,1])
plt.xlim(-2, 2)
plt.ylim(-2, 2)
plt.show()
# wでのモデルをプロット
x_s = np.linspace(xmin, xmax, 100)
for w in w_prior:
    plt.plot(x_s, f(w, x_s))
# plt.xlim(xmin, xmax)
# plt.ylim(xmin, xmax)
plt.show()

# 学習データ(真のモデルにノイズを加えたもの)
# 真のw
w_true = [1, 1]
var_y = 0.1
x_sample = xmin + (xmax-xmin)*np.random.rand(10)
y_sample = stats.norm.rvs(loc=f(w_true, x_sample), scale=np.sqrt(var_y))
for i in range(len(x_sample)):
    plt.plot(x_sample[i], y_sample[i], marker='.', color="black")
plt.plot(x_s, f(w_true, x_s))
# plt.xlim(xmin, xmax)
# plt.ylim(xmin, xmax)
plt.show()

# ベイズ線形回帰
# 事後分布の分散共分散行列
phi_phiT = []
for x in x_sample:
    phi = np.array([1, x])
    phi_phiT.append(phi.reshape(-1, 1) * phi)
phi_sum = np.sum(np.array(phi_phiT), axis=0)
Sigma = np.linalg.inv((1/var_y)*phi_sum + (1/var_w)*np.identity(2))
# 事後分布の平均ベクトル
y_phi = []
for i in range(len(y_sample)):
    y_phi.append(y_sample[i]*np.array([1, x_sample[i]]))
y_phi_sum = np.sum(np.array(y_phi), axis=0)
Mu = np.dot(Sigma, (1/var_y)*y_phi_sum)
# wの事後確率
w_post = stats.multivariate_normal.rvs(mean=Mu, cov=Sigma, size=10)
plt.scatter(w_post[:,0], w_post[:,1])
plt.xlim(-2, 2)
plt.ylim(-2, 2)
plt.show()

for i in range(len(x_sample)):
    plt.plot(x_sample[i], y_sample[i], marker='.', color="black")
for w in w_post:
    plt.plot(x_s, f(w, x_s), alpha=0.5)
plt.plot(x_s, f(w_true, x_s), color="black")
# plt.xlim(xmin, xmax)
# plt.ylim(xmin, xmax)
plt.show()
