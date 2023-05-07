import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

if __name__ == '__main__':
    pts = np.random.randn(100, 2)
    pts[:, 0] = pts[:, 0] - 0.6
    pts[:, 1] = pts[:, 1] * 0.5 + 0.4

    plt.scatter(pts[:, 0], pts[:, 1])
    plt.scatter(np.average(pts[:, 0]), np.average(pts[:, 1]), color='red')
    plt.grid()
    plt.axis('equal')

    print('mean:', np.average(pts[:, 0]), np.average(pts[:, 1]))
    print('std:', np.std(pts[:, 0]), np.std(pts[:, 1]))

    scaler = MinMaxScaler()
    pts_scale = scaler.fit_transform(pts)

    plt.scatter(pts_scale[:, 0], pts_scale[:, 1])
    plt.scatter(np.average(pts_scale[:, 0]), np.average(pts_scale[:, 1]), color='red')
    plt.grid()
    plt.axis('equal')

    print('mean:', np.average(pts_scale[:, 0]), np.average(pts_scale[:, 1]))
    print('std:', np.std(pts_scale[:, 0]), np.std(pts_scale[:, 1]))
