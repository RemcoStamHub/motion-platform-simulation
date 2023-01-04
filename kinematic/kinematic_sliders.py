import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from platform_constructor import Example

new_platform = Example()
slider_x = 0.10
slider_y = 0.1
slider_width = 0.3
slider_height = 0.03

fig = plt.figure()

plt.subplots_adjust(bottom=0.05, left=0.4)
ax = fig.add_subplot(projection='3d')
at = fig.add_axes([0.1, 0.6, 0.1, 0.2])

roll_value = fig.add_axes([slider_x, slider_y + 0.02, slider_width, slider_height])
roll_slider = Slider(ax=roll_value, label='roll',
                     valmin=-30, valmax=30,
                     valinit=new_platform.roll,
                     valstep=1)

pitch_value = fig.add_axes([slider_x, slider_y + 0.04, slider_width, slider_height])
pitch_slider = Slider(ax=pitch_value, label='pitch',
                      valmin=-30,
                      valmax=30,
                      valinit=new_platform.pitch,
                      valstep=1)

yaw_value = fig.add_axes([slider_x, slider_y + 0.06, slider_width, slider_height])
yaw_slider = Slider(ax=yaw_value, label='yaw',
                    valmin=-30,
                    valmax=30,
                    valinit=new_platform.yaw,
                    valstep=1)

heave_value = fig.add_axes([slider_x, slider_y + 0.08, slider_width, slider_height])
heave_slider = Slider(ax=heave_value, label='heave',
                      valmin=new_platform.heave - 1,
                      valmax=new_platform.heave + 1,
                      valinit=new_platform.heave,
                      valstep=0.01)

ground_length_value = fig.add_axes([slider_x, slider_y + 0.10, slider_width, slider_height])
ground_length_slider = Slider(ax=ground_length_value, label='ground_length',
                              valmin=new_platform.ground_length - 3,
                              valmax=new_platform.ground_length + 3,
                              valinit=new_platform.ground_length,
                              valstep=0.01)

ground_width_value = fig.add_axes([slider_x, slider_y + 0.12, slider_width, slider_height])
ground_width_slider = Slider(ax=ground_width_value, label='ground_width',
                             valmin=new_platform.ground_width - 3,
                             valmax=new_platform.ground_width + 3,
                             valinit=new_platform.ground_width,
                             valstep=0.01)

motion_length_value = fig.add_axes([slider_x, slider_y + 0.14, slider_width, slider_height])
motion_length_slider = Slider(ax=motion_length_value, label='motion_length',
                              valmin=new_platform.motion_length - 3,
                              valmax=new_platform.motion_length + 3,
                              valinit=new_platform.motion_length,
                              valstep=0.01)
motion_width_value = fig.add_axes([slider_x, slider_y + 0.16, slider_width, slider_height])
motion_width_slider = Slider(ax=motion_width_value, label='motion_width',
                             valmin=new_platform.motion_width - 3,
                             valmax=new_platform.motion_width + 3,
                             valinit=new_platform.motion_width,
                             valstep=0.01)

roll_yaw_x_value = fig.add_axes([slider_x, slider_y + 0.18, slider_width, slider_height])
roll_yaw_x_slider = Slider(ax=roll_yaw_x_value, label='roll_yaw_x',
                           valmin=new_platform.roll_yaw_x - 3,
                           valmax=new_platform.roll_yaw_x + 3,
                           valinit=new_platform.roll_yaw_x,
                           valstep=0.01)

roll_yaw_z_value = fig.add_axes([slider_x, slider_y + 0.20, slider_width, slider_height])
roll_yaw_z_slider = Slider(ax=roll_yaw_z_value, label='roll_yaw_z',
                           valmin=new_platform.roll_yaw_z - 3,
                           valmax=new_platform.roll_yaw_z + 3,
                           valinit=new_platform.roll_yaw_z,
                           valstep=0.01)

pitch_x_value = fig.add_axes([slider_x, slider_y + 0.22, slider_width, slider_height])
pitch_x_slider = Slider(ax=pitch_x_value, label='pitch_x',
                        valmin=new_platform.pitch_x - 3,
                        valmax=new_platform.pitch_x + 3,
                        valinit=new_platform.pitch_x,
                        valstep=0.01)

pitch_z_value = fig.add_axes([slider_x, slider_y + 0.24, slider_width, slider_height])
pitch_z_slider = Slider(ax=pitch_z_value, label='pitch_z',
                        valmin=new_platform.pitch_z - 3,
                        valmax=new_platform.pitch_z + 3,
                        valinit=new_platform.pitch_z,
                        valstep=0.01)


def update_platform(val):
    new_platform.ground_length = ground_length_slider.val
    new_platform.ground_width = ground_width_slider.val
    new_platform.motion_length = motion_length_slider.val
    new_platform.motion_width = motion_width_slider.val
    new_platform.roll_yaw_x = roll_yaw_x_slider.val
    new_platform.roll_yaw_z = roll_yaw_z_slider.val
    new_platform.pitch_x = pitch_x_slider.val
    new_platform.pitch_z = pitch_z_slider.val

    new_platform.build_system()
    update(val)


def update(val):
    new_platform.roll = roll_slider.val
    new_platform.pitch = pitch_slider.val
    new_platform.yaw = yaw_slider.val
    new_platform.heave = heave_slider.val

    new_platform.move_system()

    l_0, l_1, l_2, l_3 = new_platform.actuator_lengths()

    ax.cla()
    at.cla()

    ax.set_xlim3d(-1.5, 2.5)
    ax.set_ylim3d(-2, 2)
    ax.set_zlim3d(0, 4)

    ax.scatter(new_platform.ground_point_0_reference_frame[0],
               new_platform.ground_point_0_reference_frame[1],
               new_platform.ground_point_0_reference_frame[2],
               color='red', s=100)
    ax.scatter(new_platform.ground_point_1_reference_frame[0],
               new_platform.ground_point_1_reference_frame[1],
               new_platform.ground_point_1_reference_frame[2],
               color='red', s=100)
    ax.scatter(new_platform.ground_point_2_reference_frame[0],
               new_platform.ground_point_2_reference_frame[1],
               new_platform.ground_point_2_reference_frame[2],
               color='red', s=100)
    ax.scatter(new_platform.ground_point_3_reference_frame[0],
               new_platform.ground_point_3_reference_frame[1],
               new_platform.ground_point_3_reference_frame[2],
               color='red', s=100)

    ax.text(new_platform.ground_point_0_reference_frame[0],
            new_platform.ground_point_0_reference_frame[1],
            new_platform.ground_point_0_reference_frame[2]+0.2,
            '0',
            color='black')
    ax.text(new_platform.ground_point_1_reference_frame[0],
            new_platform.ground_point_1_reference_frame[1],
            new_platform.ground_point_1_reference_frame[2]+0.2,
            '1',
            color='black')
    ax.text(new_platform.ground_point_2_reference_frame[0],
            new_platform.ground_point_2_reference_frame[1],
            new_platform.ground_point_2_reference_frame[2]+0.2,
            '2',
            color='black')
    ax.text(new_platform.ground_point_3_reference_frame[0],
            new_platform.ground_point_3_reference_frame[1],
            new_platform.ground_point_3_reference_frame[2]+0.2,
            '3',
            color='black')

    ax.scatter(new_platform.pitch_point_reference_frame[0],
               new_platform.pitch_point_reference_frame[1],
               new_platform.pitch_point_reference_frame[2],
               color='black', s=100)
    ax.scatter(new_platform.roll_yaw_point_reference_frame[0],
               new_platform.roll_yaw_point_reference_frame[1],
               new_platform.roll_yaw_point_reference_frame[2],
               color='orange', s=100)
    ax.scatter(new_platform.gravity_point_reference_frame[0],
               new_platform.gravity_point_reference_frame[1],
               new_platform.gravity_point_reference_frame[2],
               color='grey', s=100)

    ax.scatter(new_platform.platform_point_0_reference_frame[0],
               new_platform.platform_point_0_reference_frame[1],
               new_platform.platform_point_0_reference_frame[2],
               color='blue', s=100)
    ax.scatter(new_platform.platform_point_1_reference_frame[0],
               new_platform.platform_point_1_reference_frame[1],
               new_platform.platform_point_1_reference_frame[2],
               color='blue', s=100)
    ax.scatter(new_platform.platform_point_2_reference_frame[0],
               new_platform.platform_point_2_reference_frame[1],
               new_platform.platform_point_2_reference_frame[2],
               color='blue', s=100)
    ax.scatter(new_platform.platform_point_3_reference_frame[0],
               new_platform.platform_point_3_reference_frame[1],
               new_platform.platform_point_3_reference_frame[2],
               color='blue', s=100)

    ax.plot([new_platform.ground_point_0_reference_frame[0], new_platform.platform_point_0_reference_frame[0]],
            [new_platform.ground_point_0_reference_frame[1], new_platform.platform_point_0_reference_frame[1]],
            [new_platform.ground_point_0_reference_frame[2], new_platform.platform_point_0_reference_frame[2]],
            color='purple')
    ax.plot([new_platform.ground_point_1_reference_frame[0], new_platform.platform_point_1_reference_frame[0]],
            [new_platform.ground_point_1_reference_frame[1], new_platform.platform_point_1_reference_frame[1]],
            [new_platform.ground_point_1_reference_frame[2], new_platform.platform_point_1_reference_frame[2]],
            color='purple')
    ax.plot([new_platform.ground_point_2_reference_frame[0], new_platform.platform_point_2_reference_frame[0]],
            [new_platform.ground_point_2_reference_frame[1], new_platform.platform_point_2_reference_frame[1]],
            [new_platform.ground_point_2_reference_frame[2], new_platform.platform_point_2_reference_frame[2]],
            color='purple')
    ax.plot([new_platform.ground_point_3_reference_frame[0], new_platform.platform_point_3_reference_frame[0]],
            [new_platform.ground_point_3_reference_frame[1], new_platform.platform_point_3_reference_frame[1]],
            [new_platform.ground_point_3_reference_frame[2], new_platform.platform_point_3_reference_frame[2]],
            color='purple')

    ax.plot([new_platform.platform_point_0_reference_frame[0], new_platform.platform_point_2_reference_frame[0]],
            [new_platform.platform_point_0_reference_frame[1], new_platform.platform_point_2_reference_frame[1]],
            [new_platform.platform_point_0_reference_frame[2], new_platform.platform_point_2_reference_frame[2]],
            color='green')
    ax.plot([new_platform.platform_point_1_reference_frame[0], new_platform.platform_point_3_reference_frame[0]],
            [new_platform.platform_point_1_reference_frame[1], new_platform.platform_point_3_reference_frame[1]],
            [new_platform.platform_point_1_reference_frame[2], new_platform.platform_point_3_reference_frame[2]],
            color='green')
    ax.plot([new_platform.platform_point_0_reference_frame[0], new_platform.platform_point_1_reference_frame[0]],
            [new_platform.platform_point_0_reference_frame[1], new_platform.platform_point_1_reference_frame[1]],
            [new_platform.platform_point_0_reference_frame[2], new_platform.platform_point_1_reference_frame[2]],
            color='green')
    ax.plot([new_platform.platform_point_2_reference_frame[0], new_platform.platform_point_3_reference_frame[0]],
            [new_platform.platform_point_2_reference_frame[1], new_platform.platform_point_3_reference_frame[1]],
            [new_platform.platform_point_2_reference_frame[2], new_platform.platform_point_3_reference_frame[2]],
            color='green')

    ax.plot([new_platform.platform_point_0_reference_frame[0], new_platform.roll_yaw_point_reference_frame[0]],
            [new_platform.platform_point_0_reference_frame[1], new_platform.roll_yaw_point_reference_frame[1]],
            [new_platform.platform_point_0_reference_frame[2], new_platform.roll_yaw_point_reference_frame[2]],
            color='cyan')
    ax.plot([new_platform.platform_point_1_reference_frame[0], new_platform.roll_yaw_point_reference_frame[0]],
            [new_platform.platform_point_1_reference_frame[1], new_platform.roll_yaw_point_reference_frame[1]],
            [new_platform.platform_point_1_reference_frame[2], new_platform.roll_yaw_point_reference_frame[2]],
            color='cyan')
    ax.plot([new_platform.platform_point_2_reference_frame[0], new_platform.roll_yaw_point_reference_frame[0]],
            [new_platform.platform_point_2_reference_frame[1], new_platform.roll_yaw_point_reference_frame[1]],
            [new_platform.platform_point_2_reference_frame[2], new_platform.roll_yaw_point_reference_frame[2]],
            color='cyan')
    ax.plot([new_platform.platform_point_3_reference_frame[0], new_platform.roll_yaw_point_reference_frame[0]],
            [new_platform.platform_point_3_reference_frame[1], new_platform.roll_yaw_point_reference_frame[1]],
            [new_platform.platform_point_3_reference_frame[2], new_platform.roll_yaw_point_reference_frame[2]],
            color='cyan')

    ax.plot([new_platform.platform_point_0_reference_frame[0], new_platform.gravity_point_reference_frame[0]],
            [new_platform.platform_point_0_reference_frame[1], new_platform.gravity_point_reference_frame[1]],
            [new_platform.platform_point_0_reference_frame[2], new_platform.gravity_point_reference_frame[2]],
            color='magenta')
    ax.plot([new_platform.platform_point_1_reference_frame[0], new_platform.gravity_point_reference_frame[0]],
            [new_platform.platform_point_1_reference_frame[1], new_platform.gravity_point_reference_frame[1]],
            [new_platform.platform_point_1_reference_frame[2], new_platform.gravity_point_reference_frame[2]],
            color='magenta')
    ax.plot([new_platform.platform_point_2_reference_frame[0], new_platform.gravity_point_reference_frame[0]],
            [new_platform.platform_point_2_reference_frame[1], new_platform.gravity_point_reference_frame[1]],
            [new_platform.platform_point_2_reference_frame[2], new_platform.gravity_point_reference_frame[2]],
            color='magenta')
    ax.plot([new_platform.platform_point_3_reference_frame[0], new_platform.gravity_point_reference_frame[0]],
            [new_platform.platform_point_3_reference_frame[1], new_platform.gravity_point_reference_frame[1]],
            [new_platform.platform_point_3_reference_frame[2], new_platform.gravity_point_reference_frame[2]],
            color='magenta')

    at.axis('off')
    at.table(cellText=np.array([[("{:.3f}".format(l_0))],
                                [("{:.3f}".format(l_1))],
                                [("{:.3f}".format(l_2))],
                                [("{:.3f}".format(l_3))]]),
             rowLabels=('l0', 'l1', 'l2', 'l3'), loc='top', bbox=[0, 0, 1, 1])

    fig.canvas.draw_idle()


update_platform(0)

roll_slider.on_changed(update)
pitch_slider.on_changed(update)
yaw_slider.on_changed(update)
heave_slider.on_changed(update)
ground_length_slider.on_changed(update_platform)
ground_width_slider.on_changed(update_platform)
motion_length_slider.on_changed(update_platform)
motion_width_slider.on_changed(update_platform)
roll_yaw_x_slider.on_changed(update_platform)
roll_yaw_z_slider.on_changed(update_platform)
pitch_x_slider.on_changed(update_platform)
pitch_z_slider.on_changed(update_platform)

plt.show()
