# import numpy as np
# import matplotlib.pyplot as plt

# # x_soat = np.array([1.0, 2.0, 3.0])
# # y_baho = np.array([2.0, 4.0, 6.0])



# with open("test.txt", "r") as f:
#     lines = f.readlines()

# x_soat = list(map(int, lines[0].strip().split()))
# y_baho = list(map(int, lines[1].strip().split()))



# w_list = []
# mse_list = []


# def y_(x):
#     return x * w


# def loss(x, y):
#     return pow((y_(x) - y), 2)

# def sigmoid(x,w):
#     return 1.0/(1+np.exp(-(x*w)))

# for w in np.arange(1.0, 3.1, 0.01):
#     print("w={:.3f}".format(w))
#     L_umum = 0
#     print("\t  x   |   y   |  r   |  y_b  | sigmoid")

#     for x_1, y_1 in zip(x_soat, y_baho):
#         y_bash = y_(x_1)
#         L_qiym = loss(x_1, y_1)
#         L_umum += L_qiym
#         # :
#         print("\t", "{:.2f} | {:.2f} | {:.2f} | {:.2f} |   {}".format(x_1, y_1, L_qiym, y_bash, sigmoid(x_1,w) >= 0.6))



#     print("MSE={:.3f}".format(L_umum / len(x_soat)))
#     print("______________________________________")
#     w_list.append(w)
#     mse_list.append(L_umum / len(x_soat))



# print("\nEng yaxshi MSE : ", min(mse_list))
# print("Eng yaxshi w : ", w_list[mse_list.index(min(mse_list))])





with open("test.txt", "r") as f:
    lines = f.readlines()

x = list(map(int, lines[0].strip().split()))
y = list(map(int, lines[1].strip().split()))


def chiz_regressiya(n, x, y):
    x1 = sum(x) / len(x)
    y1 = sum(y) / len(y)

    sur = 0
    maxr = 0
    for i in range(0, n):
        sur += (x[i]-x1)*(y[i]-y1)
        maxr += (x[i]-x1)
        print(f"w[ {i+1} ] = {sur/maxr}")
    return "ok"

print(chiz_regressiya(540, x, y))
