import matplotlib.pyplot as plt

from platform_constructor import Example

step = 0.1
heavestep = 0.01

roll_range = 30  # +- value deg
roll_speed = 50  # +- value deg/s
roll_acceleration = 250  # +- value deg/s^2

pitch_range = 30  # +- value degrees
pitch_speed = 50  # +- value degrees/s
pitch_acceleration = 250  # +- value deg/s^2

yaw_range = 30  # +- value degrees
yaw_speed = 50  # +- value degrees/s
yaw_acceleration = 250  # +- value deg/s^2

heave_range = 0.14
heave_speed = 0.3
heave_acceleration = 5

angle_min = -30
angle_max = 30

length_min = 0.5
length_max = 2

speed_min = -0.75
speed_max = 0.75

acceleration_min = -5
acceleration_max = 5

force_min = -100
force_max = 100

fig, ((ax0, ax1, ax2, ax3), (ax4, ax5, ax6, ax7), (ax8, ax9, ax10, ax11), (ax12, ax13, ax14, ax15)) = plt.subplots(4, 4)
fig.tight_layout(pad=0.01)
fig.canvas.manager.set_window_title('Dynamic')

ax0.set_xlim(angle_min, angle_max)
ax1.set_xlim(angle_min, angle_max)
ax2.set_xlim(angle_min, angle_max)
ax3.set_xlim(angle_min, angle_max)
ax4.set_xlim(angle_min, angle_max)
ax5.set_xlim(angle_min, angle_max)
ax6.set_xlim(angle_min, angle_max)
ax7.set_xlim(angle_min, angle_max)
ax8.set_xlim(angle_min, angle_max)
ax9.set_xlim(angle_min, angle_max)
ax10.set_xlim(angle_min, angle_max)
ax11.set_xlim(angle_min, angle_max)
ax12.set_xlim(angle_min, angle_max)
ax13.set_xlim(angle_min, angle_max)
ax14.set_xlim(angle_min, angle_max)
ax15.set_xlim(angle_min, angle_max)

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
ax12.set_ylim(force_min, force_max)
ax13.set_ylim(force_min, force_max)
ax14.set_ylim(force_min, force_max)
ax15.set_ylim(force_min, force_max)

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
ax12.set_xlabel('angle (deg)')
ax12.set_ylabel('dynamic load (N)')
ax13.set_xlabel('angle (deg)')
ax13.set_ylabel('dynamic load (N)')
ax14.set_xlabel('angle (deg)')
ax14.set_ylabel('dynamic load (N)')
ax15.set_xlabel('angle (deg)')
ax15.set_ylabel('dynamic load (N)')


def plot_roll():
    roll_platform = Example()

    (roll_values,
     length_0_values, length_1_values, length_2_values, length_3_values,
     speed_0_values, speed_1_values, speed_2_values, speed_3_values,
     acceleration_0_values, acceleration_1_values, acceleration_2_values, acceleration_3_values,
     force_0_values, force_1_values, force_2_values, force_3_values
     ) = roll_platform.roll_platform_limits(-roll_range, roll_range, roll_speed, roll_acceleration, step)

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
    ax12.plot(roll_values, force_0_values, label=plot_label)
    ax13.plot(roll_values, force_1_values, label=plot_label)
    ax14.plot(roll_values, force_2_values, label=plot_label)
    ax15.plot(roll_values, force_3_values, label=plot_label)


def plot_pitch():
    pitch_platform = Example()

    (pitch_values,
     length_0_values, length_1_values, length_2_values, length_3_values,
     speed_0_values, speed_1_values, speed_2_values, speed_3_values,
     acceleration_0_values, acceleration_1_values, acceleration_2_values, acceleration_3_values,
     force_0_values, force_1_values, force_2_values, force_3_values
     ) = pitch_platform.pitch_platform_limits(-pitch_range, pitch_range, pitch_speed, pitch_acceleration, step)

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
    ax12.plot(pitch_values, force_0_values, label=plot_label)
    ax13.plot(pitch_values, force_1_values, label=plot_label)
    ax14.plot(pitch_values, force_2_values, label=plot_label)
    ax15.plot(pitch_values, force_3_values, label=plot_label)


def plot_yaw():
    yaw_platform = Example()

    (yaw_values,
     length_0_values, length_1_values, length_2_values, length_3_values,
     speed_0_values, speed_1_values, speed_2_values, speed_3_values,
     acceleration_0_values, acceleration_1_values, acceleration_2_values, acceleration_3_values,
     force_0_values, force_1_values, force_2_values, force_3_values
     ) = yaw_platform.yaw_platform_limits(-yaw_range, yaw_range, yaw_speed, yaw_acceleration, step)

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
    ax12.plot(yaw_values, force_0_values, label=plot_label)
    ax13.plot(yaw_values, force_1_values, label=plot_label)
    ax14.plot(yaw_values, force_2_values, label=plot_label)
    ax15.plot(yaw_values, force_3_values, label=plot_label)


def plot_heave():
    figheave, ((bx0, bx1, bx2, bx3), (bx4, bx5, bx6, bx7), (bx8, bx9, bx10, bx11), (bx12, bx13, bx14, bx15)) = plt.subplots(
        4, 4)
    figheave.tight_layout(pad=0.01)
    figheave.canvas.manager.set_window_title('Dynamic_heave')

    bx0.set_xlabel('height (m)')
    bx0.set_ylabel('length (m)')
    bx1.set_xlabel('height (m)')
    bx1.set_ylabel('length (m)')
    bx2.set_xlabel('height (m)')
    bx2.set_ylabel('length (m)')
    bx3.set_xlabel('height (m)')
    bx3.set_ylabel('length (m)')
    bx4.set_xlabel('height (m)')
    bx4.set_ylabel('speed (m/s)')
    bx5.set_xlabel('height (m)')
    bx5.set_ylabel('speed (m/s)')
    bx6.set_xlabel('height (m)')
    bx6.set_ylabel('speed (m/s)')
    bx7.set_xlabel('height (m)')
    bx7.set_ylabel('speed (m/s)')
    bx8.set_xlabel('height (m)')
    bx8.set_ylabel('acceleration (m/s^2)')
    bx9.set_xlabel('height (m)')
    bx9.set_ylabel('acceleration (m/s^2)')
    bx10.set_xlabel('height (m)')
    bx10.set_ylabel('acceleration (m/s^2)')
    bx11.set_xlabel('height (m)')
    bx11.set_ylabel('acceleration (m/s^2)')
    bx12.set_xlabel('height (m)')
    bx12.set_ylabel('dynamic load (N)')
    bx13.set_xlabel('height (m)')
    bx13.set_ylabel('dynamic load (N)')
    bx14.set_xlabel('height (m)')
    bx14.set_ylabel('dynamic load (N)')
    bx15.set_xlabel('height (m)')
    bx15.set_ylabel('dynamic load (N)')
    
    heave_platform = Example()
    heave_centre = heave_platform.heave
    (heave_values,
     length_0_values, length_1_values, length_2_values, length_3_values,
     speed_0_values, speed_1_values, speed_2_values, speed_3_values,
     acceleration_0_values, acceleration_1_values, acceleration_2_values, acceleration_3_values,
     force_0_values, force_1_values, force_2_values, force_3_values
     ) = heave_platform.heave_platform_limits(-heave_range + heave_centre, heave_range + heave_centre, heave_speed, heave_acceleration, heavestep)
    
    plot_label = 'Heave'
    bx0.plot(heave_values, length_0_values, label=plot_label)
    bx1.plot(heave_values, length_1_values, label=plot_label)
    bx2.plot(heave_values, length_2_values, label=plot_label)
    bx3.plot(heave_values, length_3_values, label=plot_label)
    bx4.plot(heave_values, speed_0_values, label=plot_label)
    bx5.plot(heave_values, speed_1_values, label=plot_label)
    bx6.plot(heave_values, speed_2_values, label=plot_label)
    bx7.plot(heave_values, speed_3_values, label=plot_label)
    bx8.plot(heave_values, acceleration_0_values, label=plot_label)
    bx9.plot(heave_values, acceleration_1_values, label=plot_label)
    bx10.plot(heave_values, acceleration_2_values, label=plot_label)
    bx11.plot(heave_values, acceleration_3_values, label=plot_label)
    bx12.plot(heave_values, force_0_values, label=plot_label)
    bx13.plot(heave_values, force_1_values, label=plot_label)
    bx14.plot(heave_values, force_2_values, label=plot_label)
    bx15.plot(heave_values, force_3_values, label=plot_label)

    bx0.legend()
    bx1.legend()
    bx2.legend()
    bx3.legend()
    bx4.legend()
    bx5.legend()
    bx6.legend()
    bx7.legend()
    bx8.legend()
    bx9.legend()
    bx10.legend()
    bx11.legend()
    bx12.legend()
    bx13.legend()
    bx14.legend()
    bx15.legend()


plot_roll()
plot_pitch()
plot_yaw()
plot_heave()

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
ax12.legend()
ax13.legend()
ax14.legend()
ax15.legend()

plt.show()
