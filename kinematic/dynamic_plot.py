import numpy as np
import matplotlib.pyplot as plt
from platform_constructor import Platform, Example

step = 0.1

roll_range = 30  # +- value deg
roll_speed = 50  # +- value deg/s
roll_acceleration = 250  # +- value deg/s^2

pitch_range = 30  # +- value degrees
pitch_speed = 50  # +- value degrees/s
pitch_acceleration = 250  # +- value deg/s^2

yaw_range = 30  # +- value degrees
yaw_speed = 50  # +- value degrees/s
yaw_acceleration = 250  # +- value deg/s^2

length_min = 0.5
length_max = 2

speed_min = -0.75
speed_max = 0.75

acceleration_min = -5
acceleration_max = 5

fig, ((ax0, ax1, ax2, ax3), (ax4, ax5, ax6, ax7), (ax8, ax9, ax10, ax11)) = plt.subplots(3, 4)
fig.tight_layout(pad=0.01)
fig.canvas.manager.set_window_title('Dynamic')

ax0.set_xlim(-roll_range, roll_range)
ax1.set_xlim(-roll_range, roll_range)
ax2.set_xlim(-roll_range, roll_range)
ax3.set_xlim(-roll_range, roll_range)
ax4.set_xlim(-roll_range, roll_range)
ax5.set_xlim(-roll_range, roll_range)
ax6.set_xlim(-roll_range, roll_range)
ax7.set_xlim(-roll_range, roll_range)
ax8.set_xlim(-roll_range, roll_range)
ax9.set_xlim(-roll_range, roll_range)
ax10.set_xlim(-roll_range, roll_range)
ax11.set_xlim(-roll_range, roll_range)

ax0.set_ylim(length_min, length_max)
ax1.set_ylim(length_min, length_max)
ax2.set_ylim(length_min, length_max)
ax3.set_ylim(length_min, length_max)
ax4.set_ylim(speed_min, speed_max)
ax5.set_ylim(speed_min, speed_max)
ax6.set_ylim(speed_min, speed_max)
ax7.set_ylim(speed_min, speed_max)
ax8.set_ylim(acceleration_min, acceleration_max)
ax9.set_ylim(acceleration_min, acceleration_max)
ax10.set_ylim(acceleration_min, acceleration_max)
ax11.set_ylim(acceleration_min, acceleration_max)

ax0.set_xlabel('angle (deg)')
ax0.set_ylabel('length (m)')
ax1.set_xlabel('angle (deg)')
ax1.set_ylabel('length (m)')
ax2.set_xlabel('angle (deg)')
ax2.set_ylabel('length (m)')
ax3.set_xlabel('angle (deg)')
ax3.set_ylabel('length (m)')
ax4.set_xlabel('angle (deg)')
ax4.set_ylabel('speed (m/s)')
ax5.set_xlabel('angle (deg)')
ax5.set_ylabel('speed (m/s)')
ax6.set_xlabel('angle (deg)')
ax6.set_ylabel('speed (m/s)')
ax7.set_xlabel('angle (deg)')
ax7.set_ylabel('speed (m/s)')
ax8.set_xlabel('angle (deg)')
ax8.set_ylabel('acceleration (m/s^2)')
ax9.set_xlabel('angle (deg)')
ax9.set_ylabel('acceleration (m/s^2)')
ax10.set_xlabel('angle (deg)')
ax10.set_ylabel('acceleration (m/s^2)')
ax11.set_xlabel('angle (deg)')
ax11.set_ylabel('acceleration (m/s^2)')


def plot_roll():
    roll_platform = Example()

    roll_values, length_0_values, length_1_values, length_2_values, length_3_values, speed_0_values, speed_1_values, speed_2_values, speed_3_values, acceleration_0_values, acceleration_1_values, acceleration_2_values, acceleration_3_values = roll_platform.roll_platform_limits(
        -roll_range, roll_range, roll_speed, roll_acceleration, 0.1)

    plot_label = 'roll'
    ax0.plot(roll_values, length_0_values, label=plot_label)
    ax1.plot(roll_values, length_1_values, label=plot_label)
    ax2.plot(roll_values, length_2_values, label=plot_label)
    ax3.plot(roll_values, length_3_values, label=plot_label)
    ax4.plot(roll_values, speed_0_values, label=plot_label)
    ax5.plot(roll_values, speed_1_values, label=plot_label)
    ax6.plot(roll_values, speed_2_values, label=plot_label)
    ax7.plot(roll_values, speed_3_values, label=plot_label)
    ax8.plot(roll_values, acceleration_0_values, label=plot_label)
    ax9.plot(roll_values, acceleration_1_values, label=plot_label)
    ax10.plot(roll_values, acceleration_2_values, label=plot_label)
    ax11.plot(roll_values, acceleration_3_values, label=plot_label)


def plot_pitch():
    pitch_platform = Example()

    pitch_values, length_0_values, length_1_values, length_2_values, length_3_values, speed_0_values, speed_1_values, speed_2_values, speed_3_values, acceleration_0_values, acceleration_1_values, acceleration_2_values, acceleration_3_values = pitch_platform.pitch_platform_limits(
        -pitch_range, pitch_range, pitch_speed, pitch_acceleration, 0.1)

    plot_label = 'pitch'
    ax0.plot(pitch_values, length_0_values, label=plot_label)
    ax1.plot(pitch_values, length_1_values, label=plot_label)
    ax2.plot(pitch_values, length_2_values, label=plot_label)
    ax3.plot(pitch_values, length_3_values, label=plot_label)
    ax4.plot(pitch_values, speed_0_values, label=plot_label)
    ax5.plot(pitch_values, speed_1_values, label=plot_label)
    ax6.plot(pitch_values, speed_2_values, label=plot_label)
    ax7.plot(pitch_values, speed_3_values, label=plot_label)
    ax8.plot(pitch_values, acceleration_0_values, label=plot_label)
    ax9.plot(pitch_values, acceleration_1_values, label=plot_label)
    ax10.plot(pitch_values, acceleration_2_values, label=plot_label)
    ax11.plot(pitch_values, acceleration_3_values, label=plot_label)


def plot_yaw():
    yaw_platform = Example()

    yaw_values, length_0_values, length_1_values, length_2_values, length_3_values, speed_0_values, speed_1_values, speed_2_values, speed_3_values, acceleration_0_values, acceleration_1_values, acceleration_2_values, acceleration_3_values = yaw_platform.yaw_platform_limits(
        -yaw_range, yaw_range, yaw_speed, yaw_acceleration, 0.1)

    plot_label = 'yaw'
    ax0.plot(yaw_values, length_0_values, label=plot_label)
    ax1.plot(yaw_values, length_1_values, label=plot_label)
    ax2.plot(yaw_values, length_2_values, label=plot_label)
    ax3.plot(yaw_values, length_3_values, label=plot_label)
    ax4.plot(yaw_values, speed_0_values, label=plot_label)
    ax5.plot(yaw_values, speed_1_values, label=plot_label)
    ax6.plot(yaw_values, speed_2_values, label=plot_label)
    ax7.plot(yaw_values, speed_3_values, label=plot_label)
    ax8.plot(yaw_values, acceleration_0_values, label=plot_label)
    ax9.plot(yaw_values, acceleration_1_values, label=plot_label)
    ax10.plot(yaw_values, acceleration_2_values, label=plot_label)
    ax11.plot(yaw_values, acceleration_3_values, label=plot_label)


plot_roll()
plot_pitch()
plot_yaw()

ax0.legend()
ax1.legend()
ax2.legend()
ax3.legend()
ax4.legend()
ax5.legend()
ax6.legend()
ax7.legend()
ax8.legend()
ax9.legend()
ax10.legend()
ax11.legend()

plt.show()
