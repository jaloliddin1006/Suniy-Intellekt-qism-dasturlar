import numpy as np
import matplotlib.pyplot as plt

with open("test.txt", "r") as f:
    lines = f.readlines()

x_soat = list(map(int, lines[0].strip().split()))
y_baho = list(map(int, lines[1].strip().split()))
print(len(x_soat))
# x_soat = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0])
# y_baho = np.array([3.0, 7.0, 5.0, 8.0, 11.0, 13.0])

w_list = []
mse_list = []

def y_(x):
    return x * w

def loss(x, y):
    return pow((y_(x) - y), 2)

def softmax(x, w):
    return np.exp(x* w) / np.sum(np.exp(x*w))

for w in np.arange(1.0, len(x_soat), 0.01):
    # break
    print("w={:.3f}".format(w))
    L_umum = 0
    print("\t  x   |   y   |  r   |  y_b  | softmax")

    for x_1, y_1 in zip(x_soat, y_baho):
        y_bash = y_(x_1)
        L_qiym = loss(x_1, y_1)
        L_umum += L_qiym

        print("\t", "{:.2f} | {:.2f} | {:.2f} | {:.2f} |   {}".format(x_1, y_1, L_qiym, y_bash, softmax(y_bash, w)))
    
    print("MSE={:.3f}".format(L_umum / len(x_soat)))
    print("______________________________________")
    w_list.append(w)
    mse_list.append(L_umum / len(x_soat))

print("\nEng yaxshi MSE : ", min(mse_list))
print("Eng yaxshi w : ", w_list[mse_list.index(min(mse_list))])
