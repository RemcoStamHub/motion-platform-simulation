import numpy as np
from numpy import sin, cos
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider


def calculate_position(vector, roll, pitch, yaw, pitch_point, roll_yaw_point, heave_height):
    new_vector = vector
    new_vector = np.dot(yaw_matrix(yaw), new_vector)
    new_vector = compensate_vector_position(new_vector, yaw_matrix(yaw), roll_yaw_point)
    new_vector = np.dot(roll_matrix(roll), new_vector)
    new_vector = compensate_vector_position(new_vector, roll_matrix(roll), roll_yaw_point)
    new_vector = np.dot(pitch_matrix(pitch), new_vector)
    new_vector = compensate_vector_position(new_vector, pitch_matrix(pitch), pitch_point)
    new_vector = add_heave(new_vector, heave_height)
    return new_vector


def compensate_vector_position(input_vector, compensation_rotation_matrix, rotation_point):
    rotated_point = np.dot(compensation_rotation_matrix, rotation_point)
    comp = (np.array([0, rotation_point[1] - rotated_point[1], rotation_point[2] - rotated_point[2]]))
    return np.add(input_vector, comp)


def add_heave(heave_vector, heave):
    return np.add(heave_vector, np.array([0, 0, heave]))


def yaw_matrix(yaw):
    yaw = np.deg2rad(yaw)
    return np.array([
        [cos(yaw), -sin(yaw), 0],
        [sin(yaw), cos(yaw), 0],
        [0, 0, 1]
    ])


def pitch_matrix(pitch):
    pitch = np.deg2rad(pitch)
    return np.array([
        [cos(pitch), 0, sin(pitch)],
        [0, 1, 0],
        [-sin(pitch), 0, cos(pitch)]
    ])


def roll_matrix(roll):
    roll = np.deg2rad(roll)
    return np.array([
        [1, 0, 0],
        [0, cos(roll), -sin(roll)],
        [0, sin(roll), cos(roll)],
    ])


# deg
initial_roll = 0
initial_pitch = 0
initial_yaw = 0
initial_heave = 1

initial_ground_length = 1
initial_ground_width = 1
initial_ground_height = 2  # 0

initial_motion_length = 1
initial_motion_width = 0.7

initial_roll_yaw_x = 0.7
initial_roll_yaw_z = 0.3

initial_pitch_x = 0.5
initial_pitch_z = 0

slider_x = 0.10
slider_y = 0.1
slider_width = 0.3
slider_height = 0.03

fig = plt.figure()

plt.subplots_adjust(bottom=0.05, left=0.4)
ax = fig.add_subplot(projection='3d')
at = fig.add_axes([0.1, 0.6, 0.1, 0.2])

roll_value = fig.add_axes([slider_x, slider_y + 0.02, slider_width, slider_height])
roll_slider = Slider(ax=roll_value, label='roll', valmin=-30, valmax=30, valinit=initial_roll, valstep=1)
pitch_value = fig.add_axes([slider_x, slider_y + 0.04, slider_width, slider_height])
pitch_slider = Slider(ax=pitch_value, label='pitch', valmin=-30, valmax=30, valinit=initial_pitch, valstep=1)
yaw_value = fig.add_axes([slider_x, slider_y + 0.06, slider_width, slider_height])
yaw_slider = Slider(ax=yaw_value, label='yaw', valmin=-30, valmax=30, valinit=initial_yaw, valstep=1)

heave_value = fig.add_axes([slider_x, slider_y + 0.08, slider_width, slider_height])
heave_slider = Slider(ax=heave_value, label='heave', valmin=initial_heave-1, valmax=initial_heave+1,
                      valinit=initial_heave, valstep=0.01)

ground_length_value = fig.add_axes([slider_x, slider_y + 0.10, slider_width, slider_height])
ground_length_slider = Slider(ax=ground_length_value, label='ground_length', valmin=initial_ground_length - 3,
                              valmax=initial_ground_length + 3,
                              valinit=initial_ground_length,
                              valstep=0.01)
ground_width_value = fig.add_axes([slider_x, slider_y + 0.12, slider_width, slider_height])
ground_width_slider = Slider(ax=ground_width_value, label='ground_width', valmin=initial_ground_width - 3,
                             valmax=initial_ground_width + 3,
                             valinit=initial_ground_width,
                             valstep=0.01)

motion_length_value = fig.add_axes([slider_x, slider_y + 0.14, slider_width, slider_height])
motion_length_slider = Slider(ax=motion_length_value, label='motion_length', valmin=initial_motion_length - 3,
                              valmax=initial_motion_length + 3,
                              valinit=initial_motion_length,
                              valstep=0.01)
motion_width_value = fig.add_axes([slider_x, slider_y + 0.16, slider_width, slider_height])
motion_width_slider = Slider(ax=motion_width_value, label='motion_width', valmin=initial_motion_width - 3,
                             valmax=initial_motion_width + 3,
                             valinit=initial_motion_width,
                             valstep=0.01)

roll_yaw_x_value = fig.add_axes([slider_x, slider_y + 0.18, slider_width, slider_height])
roll_yaw_x_slider = Slider(ax=roll_yaw_x_value, label='roll_yaw_x', valmin=initial_roll_yaw_x - 3,
                           valmax=initial_roll_yaw_x + 3, valinit=initial_roll_yaw_x,
                           valstep=0.01)
roll_yaw_z_value = fig.add_axes([slider_x, slider_y + 0.20, slider_width, slider_height])
roll_yaw_z_slider = Slider(ax=roll_yaw_z_value, label='roll_yaw_z', valmin=initial_roll_yaw_z - 3,
                           valmax=initial_roll_yaw_z + 3, valinit=initial_roll_yaw_z,
                           valstep=0.01)
pitch_x_value = fig.add_axes([slider_x, slider_y + 0.22, slider_width, slider_height])
pitch_x_slider = Slider(ax=pitch_x_value, label='pitch_x', valmin=initial_pitch_x - 3, valmax=initial_pitch_x + 3,
                        valinit=initial_pitch_x,
                        valstep=0.01)
pitch_z_value = fig.add_axes([slider_x, slider_y + 0.24, slider_width, slider_height])
pitch_z_slider = Slider(ax=pitch_z_value, label='pitch_z', valmin=initial_pitch_z - 3, valmax=initial_pitch_z + 3,
                        valinit=initial_pitch_z,
                        valstep=0.01)


def update(val):
    ground_point_0_reference_frame = np.array([0, ground_width_slider.val / 2, initial_ground_height])
    ground_point_1_reference_frame = np.array([0, -ground_width_slider.val / 2, initial_ground_height])
    ground_point_2_reference_frame = np.array([ground_length_slider.val, ground_width_slider.val / 2,
                                               initial_ground_height])
    ground_point_3_reference_frame = np.array([ground_length_slider.val, -ground_width_slider.val / 2,
                                               initial_ground_height])

    platform_point_0_motion_frame = np.array([0, 0, 0])
    platform_point_1_motion_frame = np.array([0, 0, 0])
    platform_point_2_motion_frame = np.array([motion_length_slider.val, motion_width_slider.val / 2, 0])
    platform_point_3_motion_frame = np.array([motion_length_slider.val, -motion_width_slider.val / 2, 0])

    pitch_point_motion_frame = np.array([pitch_x_slider.val, 0, pitch_z_slider.val])
    roll_yaw_point_motion_frame = np.array([roll_yaw_x_slider.val, 0, roll_yaw_z_slider.val])

    platform_point_0_reference_frame = calculate_position(platform_point_0_motion_frame, roll_slider.val,
                                                          pitch_slider.val,
                                                          yaw_slider.val, pitch_point_motion_frame,
                                                          roll_yaw_point_motion_frame,
                                                          heave_slider.val)
    platform_point_1_reference_frame = calculate_position(platform_point_1_motion_frame, roll_slider.val,
                                                          pitch_slider.val,
                                                          yaw_slider.val, pitch_point_motion_frame,
                                                          roll_yaw_point_motion_frame,
                                                          heave_slider.val)
    platform_point_2_reference_frame = calculate_position(platform_point_2_motion_frame, roll_slider.val,
                                                          pitch_slider.val,
                                                          yaw_slider.val, pitch_point_motion_frame,
                                                          roll_yaw_point_motion_frame,
                                                          heave_slider.val)
    platform_point_3_reference_frame = calculate_position(platform_point_3_motion_frame, roll_slider.val,
                                                          pitch_slider.val,
                                                          yaw_slider.val, pitch_point_motion_frame,
                                                          roll_yaw_point_motion_frame,
                                                          heave_slider.val)
    pitch_point_reference_frame = calculate_position(pitch_point_motion_frame, roll_slider.val, pitch_slider.val,
                                                     yaw_slider.val, pitch_point_motion_frame,
                                                     roll_yaw_point_motion_frame,
                                                     heave_slider.val)
    roll_yaw_point_reference_frame = calculate_position(roll_yaw_point_motion_frame, roll_slider.val,
                                                        pitch_slider.val,
                                                        yaw_slider.val, pitch_point_motion_frame,
                                                        roll_yaw_point_motion_frame,
                                                        heave_slider.val)

    l_0 = np.linalg.norm(platform_point_0_reference_frame - ground_point_0_reference_frame)
    l_1 = np.linalg.norm(platform_point_1_reference_frame - ground_point_1_reference_frame)
    l_2 = np.linalg.norm(platform_point_2_reference_frame - ground_point_2_reference_frame)
    l_3 = np.linalg.norm(platform_point_3_reference_frame - ground_point_3_reference_frame)

    ax.cla()
    at.cla()

    ax.set_xlim3d(-0.5, 3.5)
    ax.set_ylim3d(-2, 2)
    ax.set_zlim3d(0, 4)

    ax.scatter(ground_point_0_reference_frame[0], ground_point_0_reference_frame[1], ground_point_0_reference_frame[2],
               color='red', s=100)
    ax.scatter(ground_point_1_reference_frame[0], ground_point_1_reference_frame[1], ground_point_1_reference_frame[2],
               color='red', s=100)
    ax.scatter(ground_point_2_reference_frame[0], ground_point_2_reference_frame[1], ground_point_2_reference_frame[2],
               color='red', s=100)
    ax.scatter(ground_point_3_reference_frame[0], ground_point_3_reference_frame[1], ground_point_3_reference_frame[2],
               color='red', s=100)

    ax.scatter(pitch_point_reference_frame[0], pitch_point_reference_frame[1], pitch_point_reference_frame[2],
               color='black', s=100)
    ax.scatter(roll_yaw_point_reference_frame[0], roll_yaw_point_reference_frame[1], roll_yaw_point_reference_frame[2],
               color='orange', s=100)

    ax.scatter(platform_point_0_reference_frame[0], platform_point_0_reference_frame[1],
               platform_point_0_reference_frame[2], color='blue', s=100)
    ax.scatter(platform_point_1_reference_frame[0], platform_point_1_reference_frame[1],
               platform_point_1_reference_frame[2], color='blue', s=100)
    ax.scatter(platform_point_2_reference_frame[0], platform_point_2_reference_frame[1],
               platform_point_2_reference_frame[2], color='blue', s=100)
    ax.scatter(platform_point_3_reference_frame[0], platform_point_3_reference_frame[1],
               platform_point_3_reference_frame[2], color='blue', s=100)

    ax.plot([ground_point_0_reference_frame[0], platform_point_0_reference_frame[0]],
            [ground_point_0_reference_frame[1], platform_point_0_reference_frame[1]],
            [ground_point_0_reference_frame[2], platform_point_0_reference_frame[2]], color='purple')
    ax.plot([ground_point_1_reference_frame[0], platform_point_1_reference_frame[0]],
            [ground_point_1_reference_frame[1], platform_point_1_reference_frame[1]],
            [ground_point_1_reference_frame[2], platform_point_1_reference_frame[2]], color='purple')
    ax.plot([ground_point_2_reference_frame[0], platform_point_2_reference_frame[0]],
            [ground_point_2_reference_frame[1], platform_point_2_reference_frame[1]],
            [ground_point_2_reference_frame[2], platform_point_2_reference_frame[2]], color='purple')
    ax.plot([ground_point_3_reference_frame[0], platform_point_3_reference_frame[0]],
            [ground_point_3_reference_frame[1], platform_point_3_reference_frame[1]],
            [ground_point_3_reference_frame[2], platform_point_3_reference_frame[2]], color='purple')

    ax.plot([platform_point_0_reference_frame[0], platform_point_2_reference_frame[0]],
            [platform_point_0_reference_frame[1], platform_point_2_reference_frame[1]],
            [platform_point_0_reference_frame[2], platform_point_2_reference_frame[2]], color='green')
    ax.plot([platform_point_1_reference_frame[0], platform_point_3_reference_frame[0]],
            [platform_point_1_reference_frame[1], platform_point_3_reference_frame[1]],
            [platform_point_1_reference_frame[2], platform_point_3_reference_frame[2]], color='green')
    ax.plot([platform_point_0_reference_frame[0], platform_point_1_reference_frame[0]],
            [platform_point_0_reference_frame[1], platform_point_1_reference_frame[1]],
            [platform_point_0_reference_frame[2], platform_point_1_reference_frame[2]], color='green')
    ax.plot([platform_point_2_reference_frame[0], platform_point_3_reference_frame[0]],
            [platform_point_2_reference_frame[1], platform_point_3_reference_frame[1]],
            [platform_point_2_reference_frame[2], platform_point_3_reference_frame[2]], color='green')

    at.axis('off')
    at.table(cellText=np.array([[("{:.2f}".format(l_0))],
                                [("{:.2f}".format(l_1))],
                                [("{:.2f}".format(l_2))],
                                [("{:.2f}".format(l_3))]]),
             rowLabels=('l0', 'l1', 'l2', 'l3'), loc='top', bbox=[0, 0, 1, 1])

    fig.canvas.draw_idle()


update(0)

roll_slider.on_changed(update)
pitch_slider.on_changed(update)
yaw_slider.on_changed(update)
heave_slider.on_changed(update)
ground_length_slider.on_changed(update)
ground_width_slider.on_changed(update)
motion_length_slider.on_changed(update)
motion_width_slider.on_changed(update)
roll_yaw_x_slider.on_changed(update)
roll_yaw_z_slider.on_changed(update)
pitch_x_slider.on_changed(update)
pitch_z_slider.on_changed(update)

plt.show()
