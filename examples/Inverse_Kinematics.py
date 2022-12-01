import numpy as np
from numpy import sin, cos
import matplotlib.pyplot as plt
import quaternion
import matplotlib
from mpl_toolkits.mplot3d import Axes3D

# deg
platform_roll = 20
platform_pitch = 20
platform_yaw = 10
platform_heave = 1.5



def rotation_matrix(roll, pitch, yaw):
    r = np.array([
        [cos(yaw) * cos(-pitch),
         -sin(yaw) * cos(roll) + cos(yaw) * sin(-pitch) * sin(roll),
         sin(yaw) * sin(roll) + cos(yaw) * sin(-pitch) * sin(roll)],

        [sin(yaw) * cos(-pitch),
         cos(yaw) * cos(roll) + sin(yaw) * sin(-pitch) * sin(roll),
         -cos(yaw) * sin(roll) + sin(yaw) * sin(-pitch) * cos(roll)],

        [-sin(-pitch),
         cos(-pitch) * sin(roll),
         cos(-pitch) * cos(roll)]
    ])
    print(r)
    return r


def x_compensation(rotm, rotp):
    rotated_point = np.dot(rotm, rotp)
    xcomp = np.array([0, rotp[1] - rotated_point[1], 0])
    print(xcomp)
    return xcomp


def main():
    # position actuator on Reference frame
    a_0r = np.array([0, 1, 0])
    a_1r = np.array([0, -1, 0])
    a_2r = np.array([3, 1, 0])
    a_3r = np.array([3, -1, 0])

    # position actuator on Motion Frame
    b_0m = np.array([0, 0, 0])
    b_1m = np.array([0, 0, 0])
    b_2m = np.array([3, 0.8, 0])
    b_3m = np.array([3, -0.8, 0])

    # rotation point
    rp_0m = np.array([2, 0, 0])

    rotation = rotation_matrix(np.deg2rad(platform_roll), np.deg2rad(platform_pitch), np.deg2rad(platform_yaw))
    # translation = np.array([0, 0, platform_heave])
    translation = np.add(np.array([0, 0, platform_heave]), x_compensation(rotation, rp_0m))
    print("translation is " , translation)

    b_0r = np.dot(rotation, b_0m) + translation
    b_1r = np.dot(rotation, b_1m) + translation
    b_2r = np.dot(rotation, b_2m) + translation
    b_3r = np.dot(rotation, b_3m) + translation

    rp_0r = np.dot(rotation, rp_0m) + translation

    l_0 = np.linalg.norm(b_0r - a_0r)
    l_1 = np.linalg.norm(b_1r - a_1r)
    l_2 = np.linalg.norm(b_2r - a_2r)
    l_3 = np.linalg.norm(b_3r - a_3r)

    print(l_0)
    print(l_1)
    print(l_2)
    print(l_3)

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    ax.set_xlim3d(-1, 4)
    ax.set_ylim3d(-3, 3)
    ax.set_zlim3d(0, 4)
    ax.scatter(a_0r[0], a_0r[1], a_0r[2], color='red', s=100)
    ax.scatter(a_1r[0], a_1r[1], a_1r[2], color='red', s=100)
    ax.scatter(a_2r[0], a_2r[1], a_2r[2], color='red', s=100)
    ax.scatter(a_3r[0], a_3r[1], a_3r[2], color='red', s=100)

    ax.scatter(rp_0r[0], rp_0r[1], rp_0r[2], color='black', s=100)

    ax.scatter(b_0r[0], b_0r[1], b_0r[2], color='blue', s=100)
    ax.scatter(b_1r[0], b_1r[1], b_1r[2], color='blue', s=100)
    ax.scatter(b_2r[0], b_2r[1], b_2r[2], color='blue', s=100)
    ax.scatter(b_3r[0], b_3r[1], b_3r[2], color='blue', s=100)

    ax.plot([a_0r[0], b_0r[0]], [a_0r[1], b_0r[1]], [a_0r[2], b_0r[2]], color='purple')
    ax.plot([a_1r[0], b_1r[0]], [a_1r[1], b_1r[1]], [a_1r[2], b_1r[2]], color='purple')
    ax.plot([a_2r[0], b_2r[0]], [a_2r[1], b_2r[1]], [a_2r[2], b_2r[2]], color='purple')
    ax.plot([a_3r[0], b_3r[0]], [a_3r[1], b_3r[1]], [a_3r[2], b_3r[2]], color='purple')

    ax.plot([b_0r[0], b_2r[0]], [b_0r[1], b_2r[1]], [b_0r[2], b_2r[2]], color='green')
    ax.plot([b_1r[0], b_3r[0]], [b_1r[1], b_3r[1]], [b_1r[2], b_3r[2]], color='green')
    ax.plot([b_0r[0], b_1r[0]], [b_0r[1], b_1r[1]], [b_0r[2], b_1r[2]], color='green')
    ax.plot([b_2r[0], b_3r[0]], [b_2r[1], b_3r[1]], [b_2r[2], b_3r[2]], color='green')

    plt.show()


main()
