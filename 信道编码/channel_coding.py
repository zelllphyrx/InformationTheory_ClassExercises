import numpy as np

# 定义信道传递矩阵
P_Y_given_X = np.array([
    [1/2, 1/3, 1/6],
    [1/6, 1/2, 1/3],
    [1/3, 1/6, 1/2]
])

# 定义信源概率
P_X = np.array([1/2, 1/4, 1/4])

# 计算联合概率矩阵 P(X, Y) = P(Y|X) * P(X)
P_XY = P_Y_given_X * P_X[:, None]

# 最大似然译码规则
# F(y1) = x1, F(y2) = x2, F(y3) = x3
# 对应的误码概率计算如下
P_E_max_likelihood = (
    P_X[0] * (P_Y_given_X[0, 1] + P_Y_given_X[0, 2]) +
    P_X[1] * (P_Y_given_X[1, 0] + P_Y_given_X[1, 2]) +
    P_X[2] * (P_Y_given_X[2, 0] + P_Y_given_X[2, 1])
)

# 最小错误概率译码规则
# 计算条件概率 P(X|Y) = P(Y|X) * P(X) / P(Y)
P_Y = P_XY.sum(axis=0)
P_X_given_Y = P_XY / P_Y

# 确定最小错误概率译码规则
F_min_error = np.argmax(P_X_given_Y, axis=0)

# 对应的误码概率计算如下
P_E_min_error = 1 - sum(P_XY[i, j] for j, i in enumerate(F_min_error))

print(f"最小错误概率译码规则的平均错误概率: {P_E_min_error}")
print(f"最大似然译码规则的平均错误概率: {P_E_max_likelihood}")