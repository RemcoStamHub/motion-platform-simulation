import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from platform_constructor import Platform, Example

step = 0.1

roll_range = 30  # +- value degrees
pitch_range = 30  # +- value degrees
yaw_range = 30  # +- value degrees
heave_range = 0.2  # +- value meters
roll_speed = 20  # +- value degrees/s
pitch_speed = 20  # +- value degrees/s
yaw_speed = 20  # +- value degrees/s
heave_speed = 2  # +- value meter/s

new_platform = Example()

actuator_0_length = 0
actuator_1_length = 0
actuator_2_length = 0
actuator_3_length = 0

actuator_0_values = []
actuator_0_movement = []

actuator_1_values = []
actuator_1_movement = []

actuator_2_values = []
actuator_2_movement = []

actuator_3_values = []
actuator_3_movement = []

roll_values = []
time_values = []

dt = 0.01
time_start = 0
time_end = 2 * (roll_range / roll_speed)

new_platform.roll = - roll_range
new_platform.build_system()
new_platform.move_system()


def calculate_v_actuator_0_roll():
    radius_0 = new_platform.platform_point_0_reference_frame - new_platform.roll_yaw_point_reference_frame
    v_point_0 = np.cross(np.array([np.deg2rad(roll_speed), 0, 0]), radius_0)
    actuator_0 = new_platform.platform_point_0_reference_frame-new_platform.ground_point_0_reference_frame
    v_actuator_0 = np.dot(actuator_0/np.linalg.norm(actuator_0), v_point_0)
    return v_actuator_0


def calculate_v_actuator_1_roll():
    radius_1 = new_platform.platform_point_1_reference_frame - new_platform.roll_yaw_point_reference_frame
    v_point_1 = np.cross(np.array([np.deg2rad(roll_speed), 0, 0]), radius_1)
    actuator_1 = new_platform.platform_point_1_reference_frame-new_platform.ground_point_1_reference_frame
    v_actuator_1 = np.dot(actuator_1/np.linalg.norm(actuator_1), v_point_1)
    return v_actuator_1


def calculate_v_actuator_2_roll():
    radius_2 = new_platform.platform_point_2_reference_frame - new_platform.roll_yaw_point_reference_frame
    v_point_2 = np.cross(np.array([np.deg2rad(roll_speed), 0, 0]), radius_2)
    actuator_2 = new_platform.platform_point_2_reference_frame-new_platform.ground_point_2_reference_frame
    v_actuator_2 = np.dot(actuator_2/np.linalg.norm(actuator_2), v_point_2)
    return v_actuator_2


def calculate_v_actuator_3_roll():
    radius_3 = new_platform.platform_point_3_reference_frame - new_platform.roll_yaw_point_reference_frame
    v_point_3 = np.cross(np.array([np.deg2rad(roll_speed), 0, 0]), radius_3)
    actuator_3 = new_platform.platform_point_3_reference_frame-new_platform.ground_point_3_reference_frame
    v_actuator_3 = np.dot(actuator_3/np.linalg.norm(actuator_3), v_point_3)
    return v_actuator_3


for time in np.arange(time_start, time_end, dt):
    new_platform.build_system()
    new_platform.move_system()

    v_0 = calculate_v_actuator_0_roll()
    actuator_0_values.append(v_0)
    actuator_0_length = actuator_0_length + (v_0 * dt)
    actuator_0_movement.append(actuator_0_length)

    v_1 = calculate_v_actuator_1_roll()
    actuator_1_values.append(v_1)
    actuator_1_length = actuator_1_length + (v_1 * dt)
    actuator_1_movement.append(actuator_1_length)

    v_2 = calculate_v_actuator_2_roll()
    actuator_2_values.append(v_2)
    actuator_2_length = actuator_2_length + (v_2 * dt)
    actuator_2_movement.append(actuator_2_length)

    v_3 = calculate_v_actuator_3_roll()
    actuator_3_values.append(v_3)
    actuator_3_length = actuator_3_length + (v_3 * dt)
    actuator_3_movement.append(actuator_3_length)

    roll_values.append(new_platform.roll)
    time_values.append(time)
    new_platform.roll = new_platform.roll + (roll_speed * dt)


fig1, ((ax0, ax1, ax2, ax3), (ax4, ax5, ax6, ax7)) = plt.subplots(2, 4)
fig1.tight_layout(pad=0.01)

ax0.plot(roll_values, actuator_0_movement, label='A0')
ax0.set_xlabel('roll (deg)')
ax0.set_ylabel('length (m)')
ax0.legend()

ax1.plot(roll_values, actuator_1_movement, label='A1')
ax1.set_xlabel('roll (deg)')
ax1.set_ylabel('length (m)')
ax1.legend()

ax2.plot(roll_values, actuator_0_values, label='A0')
ax2.set_xlabel('roll (deg)')
ax2.set_ylabel('speed (m/s)')
ax2.legend()

ax3.plot(roll_values, actuator_1_values, label='A1')
ax3.set_xlabel('roll (deg)')
ax3.set_ylabel('speed (m/s)')
ax3.legend()

ax4.plot(roll_values, actuator_2_movement, label='A2')
ax4.set_xlabel('roll (deg)')
ax4.set_ylabel('length (m)')
ax4.legend()

ax5.plot(roll_values, actuator_3_movement, label='A3')
ax5.set_xlabel('roll (deg)')
ax5.set_ylabel('length (m)')
ax5.legend()

ax6.plot(roll_values, actuator_2_values, label='A2')
ax6.set_xlabel('roll (deg)')
ax6.set_ylabel('speed (m/s)')
ax6.legend()

ax7.plot(roll_values, actuator_3_values, label='A3')
ax7.set_xlabel('roll (deg)')
ax7.set_ylabel('speed (m/s)')
ax7.legend()

plt.show()
