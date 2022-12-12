import numpy as np
import matplotlib.pyplot as plt
from platform_constructor import Platform, Example

step = 0.1

roll_range = 30             # +- value deg
roll_speed = 50             # +- value deg/s
roll_acceleration = 250     # +- value deg/s^2


pitch_range = 30            # +- value degrees
pitch_speed = 50            # +- value degrees/s
pitch_acceleration = 250    # +- value deg/s^2

yaw_range = 30              # +- value degrees
yaw_speed = 50              # +- value degrees/s
yaw_acceleration = 250      # +- value deg/s^2


def plot_roll():
    roll_platform = Example()

    roll_values, length_0_values, length_1_values, length_2_values, length_3_values, speed_0_values, speed_1_values, speed_2_values, speed_3_values, acceleration_0_values, acceleration_1_values, acceleration_2_values, acceleration_3_values = roll_platform.roll_platform_limits(
        -roll_range, roll_range, roll_speed, roll_acceleration, 0.1)

    fig, ((ax0, ax1, ax2, ax3), (ax4, ax5, ax6, ax7), (ax8, ax9, ax10, ax11)) = plt.subplots(3, 4)
    fig.tight_layout(pad=0.01)
    fig.canvas.manager.set_window_title('roll')

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

    ax0.plot(roll_values, length_0_values, label='A0')
    ax0.set_xlabel('roll (deg)')
    ax0.set_ylabel('length (m)')
    ax0.legend()

    ax1.plot(roll_values, length_1_values, label='A1')
    ax1.set_xlabel('roll (deg)')
    ax1.set_ylabel('length (m)')
    ax1.legend()

    ax2.plot(roll_values, length_2_values, label='A2')
    ax2.set_xlabel('roll (deg)')
    ax2.set_ylabel('length (m)')
    ax2.legend()

    ax3.plot(roll_values, length_3_values, label='A3')
    ax3.set_xlabel('roll (deg)')
    ax3.set_ylabel('length (m)')
    ax3.legend()

    ax4.plot(roll_values, speed_0_values, label='A0')
    ax4.set_xlabel('roll (deg)')
    ax4.set_ylabel('speed (m/s)')
    ax4.legend()

    ax5.plot(roll_values, speed_1_values, label='A1')
    ax5.set_xlabel('roll (deg)')
    ax5.set_ylabel('speed (m/s)')
    ax5.legend()

    ax6.plot(roll_values, speed_2_values, label='A2')
    ax6.set_xlabel('roll (deg)')
    ax6.set_ylabel('speed (m/s)')
    ax6.legend()

    ax7.plot(roll_values, speed_3_values, label='A3')
    ax7.set_xlabel('roll (deg)')
    ax7.set_ylabel('speed (m/s)')
    ax7.legend()

    ax8.plot(roll_values, acceleration_0_values, label='A0')
    ax8.set_xlabel('roll (deg)')
    ax8.set_ylabel('acceleration (m/s^2)')
    ax8.legend()

    ax9.plot(roll_values, acceleration_1_values, label='A1')
    ax9.set_xlabel('roll (deg)')
    ax9.set_ylabel('acceleration (m/s^2)')
    ax9.legend()

    ax10.plot(roll_values, acceleration_2_values, label='A2')
    ax10.set_xlabel('roll (deg)')
    ax10.set_ylabel('acceleration (m/s^2)')
    ax10.legend()

    ax11.plot(roll_values, acceleration_3_values, label='A3')
    ax11.set_xlabel('roll (deg)')
    ax11.set_ylabel('acceleration (m/s^2)')
    ax11.legend()


def plot_pitch():
    pitch_platform = Example()

    pitch_values, length_0_values, length_1_values, length_2_values, length_3_values, speed_0_values, speed_1_values, speed_2_values, speed_3_values, acceleration_0_values, acceleration_1_values, acceleration_2_values, acceleration_3_values = pitch_platform.pitch_platform_limits(
        -pitch_range, pitch_range, pitch_speed, pitch_acceleration, 0.1)

    fig, ((ax0, ax1, ax2, ax3), (ax4, ax5, ax6, ax7), (ax8, ax9, ax10, ax11)) = plt.subplots(3, 4)
    fig.tight_layout(pad=0.01)
    fig.canvas.manager.set_window_title('pitch')

    ax0.set_xlim(-pitch_range, pitch_range)
    ax1.set_xlim(-pitch_range, pitch_range)
    ax2.set_xlim(-pitch_range, pitch_range)
    ax3.set_xlim(-pitch_range, pitch_range)
    ax4.set_xlim(-pitch_range, pitch_range)
    ax5.set_xlim(-pitch_range, pitch_range)
    ax6.set_xlim(-pitch_range, pitch_range)
    ax7.set_xlim(-pitch_range, pitch_range)
    ax8.set_xlim(-pitch_range, pitch_range)
    ax9.set_xlim(-pitch_range, pitch_range)
    ax10.set_xlim(-pitch_range, pitch_range)
    ax11.set_xlim(-pitch_range, pitch_range)

    ax0.plot(pitch_values, length_0_values, label='A0')
    ax0.set_xlabel('pitch (deg)')
    ax0.set_ylabel('length (m)')
    ax0.legend()

    ax1.plot(pitch_values, length_1_values, label='A1')
    ax1.set_xlabel('pitch (deg)')
    ax1.set_ylabel('length (m)')
    ax1.legend()

    ax2.plot(pitch_values, length_2_values, label='A2')
    ax2.set_xlabel('pitch (deg)')
    ax2.set_ylabel('length (m)')
    ax2.legend()

    ax3.plot(pitch_values, length_3_values, label='A3')
    ax3.set_xlabel('pitch (deg)')
    ax3.set_ylabel('length (m)')
    ax3.legend()

    ax4.plot(pitch_values, speed_0_values, label='A0')
    ax4.set_xlabel('pitch (deg)')
    ax4.set_ylabel('speed (m/s)')
    ax4.legend()

    ax5.plot(pitch_values, speed_1_values, label='A1')
    ax5.set_xlabel('pitch (deg)')
    ax5.set_ylabel('speed (m/s)')
    ax5.legend()

    ax6.plot(pitch_values, speed_2_values, label='A2')
    ax6.set_xlabel('pitch (deg)')
    ax6.set_ylabel('speed (m/s)')
    ax6.legend()

    ax7.plot(pitch_values, speed_3_values, label='A3')
    ax7.set_xlabel('pitch (deg)')
    ax7.set_ylabel('speed (m/s)')
    ax7.legend()

    ax8.plot(pitch_values, acceleration_0_values, label='A0')
    ax8.set_xlabel('pitch (deg)')
    ax8.set_ylabel('acceleration (m/s^2)')
    ax8.legend()

    ax9.plot(pitch_values, acceleration_1_values, label='A1')
    ax9.set_xlabel('pitch (deg)')
    ax9.set_ylabel('acceleration (m/s^2)')
    ax9.legend()

    ax10.plot(pitch_values, acceleration_2_values, label='A2')
    ax10.set_xlabel('pitch (deg)')
    ax10.set_ylabel('acceleration (m/s^2)')
    ax10.legend()

    ax11.plot(pitch_values, acceleration_3_values, label='A3')
    ax11.set_xlabel('pitch (deg)')
    ax11.set_ylabel('acceleration (m/s^2)')
    ax11.legend()


def plot_yaw():
    yaw_platform = Example()

    yaw_values, length_0_values, length_1_values, length_2_values, length_3_values, speed_0_values, speed_1_values, speed_2_values, speed_3_values, acceleration_0_values, acceleration_1_values, acceleration_2_values, acceleration_3_values = yaw_platform.yaw_platform_limits(
        -yaw_range, yaw_range, yaw_speed, yaw_acceleration, 0.1)

    fig, ((ax0, ax1, ax2, ax3), (ax4, ax5, ax6, ax7), (ax8, ax9, ax10, ax11)) = plt.subplots(3, 4)
    fig.tight_layout(pad=0.01)
    fig.canvas.manager.set_window_title('yaw')

    ax0.set_xlim(-yaw_range, yaw_range)
    ax1.set_xlim(-yaw_range, yaw_range)
    ax2.set_xlim(-yaw_range, yaw_range)
    ax3.set_xlim(-yaw_range, yaw_range)
    ax4.set_xlim(-yaw_range, yaw_range)
    ax5.set_xlim(-yaw_range, yaw_range)
    ax6.set_xlim(-yaw_range, yaw_range)
    ax7.set_xlim(-yaw_range, yaw_range)
    ax8.set_xlim(-yaw_range, yaw_range)
    ax9.set_xlim(-yaw_range, yaw_range)
    ax10.set_xlim(-yaw_range, yaw_range)
    ax11.set_xlim(-yaw_range, yaw_range)

    ax0.plot(yaw_values, length_0_values, label='A0')
    ax0.set_xlabel('yaw (deg)')
    ax0.set_ylabel('length (m)')
    ax0.legend()

    ax1.plot(yaw_values, length_1_values, label='A1')
    ax1.set_xlabel('yaw (deg)')
    ax1.set_ylabel('length (m)')
    ax1.legend()

    ax2.plot(yaw_values, length_2_values, label='A2')
    ax2.set_xlabel('yaw (deg)')
    ax2.set_ylabel('length (m)')
    ax2.legend()

    ax3.plot(yaw_values, length_3_values, label='A3')
    ax3.set_xlabel('yaw (deg)')
    ax3.set_ylabel('length (m)')
    ax3.legend()

    ax4.plot(yaw_values, speed_0_values, label='A0')
    ax4.set_xlabel('yaw (deg)')
    ax4.set_ylabel('speed (m/s)')
    ax4.legend()

    ax5.plot(yaw_values, speed_1_values, label='A1')
    ax5.set_xlabel('yaw (deg)')
    ax5.set_ylabel('speed (m/s)')
    ax5.legend()

    ax6.plot(yaw_values, speed_2_values, label='A2')
    ax6.set_xlabel('yaw (deg)')
    ax6.set_ylabel('speed (m/s)')
    ax6.legend()

    ax7.plot(yaw_values, speed_3_values, label='A3')
    ax7.set_xlabel('yaw (deg)')
    ax7.set_ylabel('speed (m/s)')
    ax7.legend()

    ax8.plot(yaw_values, acceleration_0_values, label='A0')
    ax8.set_xlabel('yaw (deg)')
    ax8.set_ylabel('acceleration (m/s^2)')
    ax8.legend()

    ax9.plot(yaw_values, acceleration_1_values, label='A1')
    ax9.set_xlabel('yaw (deg)')
    ax9.set_ylabel('acceleration (m/s^2)')
    ax9.legend()

    ax10.plot(yaw_values, acceleration_2_values, label='A2')
    ax10.set_xlabel('yaw (deg)')
    ax10.set_ylabel('acceleration (m/s^2)')
    ax10.legend()

    ax11.plot(yaw_values, acceleration_3_values, label='A3')
    ax11.set_xlabel('yaw (deg)')
    ax11.set_ylabel('acceleration (m/s^2)')
    ax11.legend()


plot_roll()
plot_pitch()
plot_yaw()
plt.show()
