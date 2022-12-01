import numpy as np
from numpy import sin, cos
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# deg
platform_roll = 0
platform_pitch = 0
platform_yaw = 0
platform_heave = 1.5


def calculate_position(vector,roll_angle,pitch_angle,yaw_angle,pitch_point,roll_yaw_point,heave_height):
    new_vector = vector
    new_vector = np.dot(yaw_matrix(yaw_angle), new_vector)
    new_vector = compensate_vector_position(new_vector,yaw_matrix(yaw_angle),roll_yaw_point)
    new_vector = np.dot(pitch_matrix(pitch_angle), new_vector)
    new_vector = compensate_vector_position(new_vector,pitch_matrix(pitch_angle),pitch_point)
    new_vector = np.dot(roll_matrix(roll_angle), new_vector)
    new_vector = compensate_vector_position(new_vector, roll_matrix(yaw_angle), roll_yaw_point)
    new_vector = add_heave(new_vector, heave_height)
    return new_vector


def compensate_vector_position(input_vector, compensation_rotation_matrix, rotation_point):
    rotated_point = np.dot(compensation_rotation_matrix, rotation_point)
    comp = (np.array([0, rotation_point[1] - rotated_point[1], rotation_point[2] - rotated_point[2]]))
    return np.add(input_vector, comp)


def add_heave(heave_vector,heave):
    return np.add(heave_vector,np.array([0,0,heave]))


def yaw_matrix(yaw):
    return np.array([
                    [cos(yaw), -sin(yaw), 0],
                    [sin(yaw), cos(yaw), 0],
                    [0, 0, 1]
                    ])


def pitch_matrix(pitch):
    return np.array([
                    [cos(pitch), 0, sin(pitch)],
                    [0, 1, 0],
                    [-sin(pitch), 0, cos(pitch)]
                    ])


def roll_matrix(roll):
    return np.array([
                    [1, 0, 0],
                    [0, cos(roll), -sin(roll)],
                    [0, sin(roll), cos(roll)],
                    ])


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
    return r


def rotationpoint_compensation(rotm, rotp):
    rotated_point = np.dot(rotm, rotp)
    xcomp = np.array([0, rotp[1] - rotated_point[1], rotp[2] - rotated_point[2]])
    return xcomp


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
rp_0m = np.array([1.5, 0, 0])

fig = plt.figure()

plt.subplots_adjust(bottom=0.2)
ax = fig.add_subplot(projection='3d')

roll_value = fig.add_axes([0.25, 0.1, 0.65, 0.03])
roll_slider = Slider(ax=roll_value, label='roll', valmin=-90, valmax=90, valinit=0, valstep=1)
pitch_value = fig.add_axes([0.25, 0.12, 0.65, 0.03])
pitch_slider = Slider(ax=pitch_value, label='pitch', valmin=-90, valmax=90, valinit=0, valstep=1)
yaw_value = fig.add_axes([0.25, 0.14, 0.65, 0.03])
yaw_slider = Slider(ax=yaw_value, label='yaw', valmin=-90, valmax=90, valinit=0, valstep=1)
heave_value = fig.add_axes([0.25, 0.16, 0.65, 0.03])
heave_slider = Slider(ax=heave_value, label='heave', valmin=0, valmax=3, valinit=1.5, valstep=0.01)


def update(val):

    # new_b_0r = calculate_position(b_0m, np.deg2rad(roll_slider.val), np.deg2rad(pitch_slider.val), np.deg2rad(yaw_slider.val), rp_0m, rp_0m, heave_slider.val)
    # new_b_1r = calculate_position(b_1m, np.deg2rad(roll_slider.val), np.deg2rad(pitch_slider.val), np.deg2rad(yaw_slider.val), rp_0m, rp_0m, heave_slider.val)
    # new_b_2r = calculate_position(b_2m, np.deg2rad(roll_slider.val), np.deg2rad(pitch_slider.val), np.deg2rad(yaw_slider.val), rp_0m, rp_0m, heave_slider.val)
    # new_b_3r = calculate_position(b_3m, np.deg2rad(roll_slider.val), np.deg2rad(pitch_slider.val), np.deg2rad(yaw_slider.val), rp_0m, rp_0m, heave_slider.val)
    # new_rp_0r = calculate_position(rp_0m, np.deg2rad(roll_slider.val), np.deg2rad(pitch_slider.val), np.deg2rad(yaw_slider.val), rp_0m, rp_0m, heave_slider.val)

    new_rotation = rotation_matrix(np.deg2rad(roll_slider.val),
                                   np.deg2rad(pitch_slider.val),
                                   np.deg2rad(yaw_slider.val))

    new_translation = np.add(np.array([0, 0, heave_slider.val]), rotationpoint_compensation(new_rotation, rp_0m))

    new_b_0r = np.dot(new_rotation, b_0m) + new_translation
    new_b_1r = np.dot(new_rotation, b_1m) + new_translation
    new_b_2r = np.dot(new_rotation, b_2m) + new_translation
    new_b_3r = np.dot(new_rotation, b_3m) + new_translation
    new_rp_0r = np.dot(new_rotation, rp_0m) + new_translation

    # l_0 = np.linalg.norm(new_b_0r - a_0r)
    # l_1 = np.linalg.norm(new_b_1r - a_1r)
    # l_2 = np.linalg.norm(new_b_2r - a_2r)
    # l_3 = np.linalg.norm(new_b_3r - a_3r)
    #
    # print(l_0)
    # print(l_1)
    # print(l_2)
    # print(l_3)

    ax.cla()

    ax.set_xlim3d(-0.5, 3.5)
    ax.set_ylim3d(-2, 2)
    ax.set_zlim3d(0, 4)

    ax.scatter(a_0r[0], a_0r[1], a_0r[2], color='red', s=100)
    ax.scatter(a_1r[0], a_1r[1], a_1r[2], color='red', s=100)
    ax.scatter(a_2r[0], a_2r[1], a_2r[2], color='red', s=100)
    ax.scatter(a_3r[0], a_3r[1], a_3r[2], color='red', s=100)

    ax.scatter(new_rp_0r[0], new_rp_0r[1], new_rp_0r[2], color='black', s=100)

    ax.scatter(new_b_0r[0], new_b_0r[1], new_b_0r[2], color='blue', s=100)
    ax.scatter(new_b_1r[0], new_b_1r[1], new_b_1r[2], color='blue', s=100)
    ax.scatter(new_b_2r[0], new_b_2r[1], new_b_2r[2], color='blue', s=100)
    ax.scatter(new_b_3r[0], new_b_3r[1], new_b_3r[2], color='blue', s=100)

    ax.plot([a_0r[0], new_b_0r[0]], [a_0r[1], new_b_0r[1]], [a_0r[2], new_b_0r[2]], color='purple')
    ax.plot([a_1r[0], new_b_1r[0]], [a_1r[1], new_b_1r[1]], [a_1r[2], new_b_1r[2]], color='purple')
    ax.plot([a_2r[0], new_b_2r[0]], [a_2r[1], new_b_2r[1]], [a_2r[2], new_b_2r[2]], color='purple')
    ax.plot([a_3r[0], new_b_3r[0]], [a_3r[1], new_b_3r[1]], [a_3r[2], new_b_3r[2]], color='purple')

    ax.plot([new_b_0r[0], new_b_2r[0]], [new_b_0r[1], new_b_2r[1]], [new_b_0r[2], new_b_2r[2]], color='green')
    ax.plot([new_b_1r[0], new_b_3r[0]], [new_b_1r[1], new_b_3r[1]], [new_b_1r[2], new_b_3r[2]], color='green')
    ax.plot([new_b_0r[0], new_b_1r[0]], [new_b_0r[1], new_b_1r[1]], [new_b_0r[2], new_b_1r[2]], color='green')
    ax.plot([new_b_2r[0], new_b_3r[0]], [new_b_2r[1], new_b_3r[1]], [new_b_2r[2], new_b_3r[2]], color='green')
    fig.canvas.draw_idle()


update(0)

roll_slider.on_changed(update)
pitch_slider.on_changed(update)
yaw_slider.on_changed(update)
heave_slider.on_changed(update)

plt.show()
