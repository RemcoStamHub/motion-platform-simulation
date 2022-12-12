import numpy as np
import matplotlib.pyplot as plt
from platform_constructor import Platform, Example

step = 0.1

roll_range = 30  # +- value degrees
pitch_range = 30  # +- value degrees
yaw_range = 30  # +- value degrees
heave_range = 0.2  # +- value meters
roll_speed = 50  # +- value degrees/s
pitch_speed = 20  # +- value degrees/s
yaw_speed = 20  # +- value degrees/s
heave_speed = 2  # +- value meter/s

roll_platform = Example()

actuator_0_length = 0
actuator_1_length = 0
actuator_2_length = 0
actuator_3_length = 0
actuator_0_speed_values = []
actuator_0_length_values = []
actuator_0_accelration_values = []
actuator_1_speed_values = []
actuator_1_length_values = []
actuator_1_accelration_values = []
actuator_2_speed_values = []
actuator_2_length_values = []
actuator_2_accelration_values = []
actuator_3_speed_values = []
actuator_3_length_values = []
actuator_3_accelration_values = []


roll_values = []
time_values = []

dt = 0.01
time_start = 0
time_end = 2 * (roll_range / roll_speed)

roll_platform.roll = - roll_range
roll_platform.build_system()
roll_platform.move_system()


def calculate_v_actuator_0_roll():
    radius_0 = roll_platform.platform_point_0_reference_frame - roll_platform.roll_yaw_point_reference_frame
    v_point_0 = np.cross(np.array([np.deg2rad(roll_speed), 0, 0]), radius_0)
    actuator_0 = roll_platform.platform_point_0_reference_frame - roll_platform.ground_point_0_reference_frame
    v_actuator_0 = np.dot(actuator_0/np.linalg.norm(actuator_0), v_point_0)
    return v_actuator_0


def calculate_v_actuator_1_roll():
    radius_1 = roll_platform.platform_point_1_reference_frame - roll_platform.roll_yaw_point_reference_frame
    v_point_1 = np.cross(np.array([np.deg2rad(roll_speed), 0, 0]), radius_1)
    actuator_1 = roll_platform.platform_point_1_reference_frame - roll_platform.ground_point_1_reference_frame
    v_actuator_1 = np.dot(actuator_1/np.linalg.norm(actuator_1), v_point_1)
    return v_actuator_1


def calculate_v_actuator_2_roll():
    radius_2 = roll_platform.platform_point_2_reference_frame - roll_platform.roll_yaw_point_reference_frame
    v_point_2 = np.cross(np.array([np.deg2rad(roll_speed), 0, 0]), radius_2)
    actuator_2 = roll_platform.platform_point_2_reference_frame - roll_platform.ground_point_2_reference_frame
    v_actuator_2 = np.dot(actuator_2/np.linalg.norm(actuator_2), v_point_2)
    return v_actuator_2


def calculate_v_actuator_3_roll():
    radius_3 = roll_platform.platform_point_3_reference_frame - roll_platform.roll_yaw_point_reference_frame
    v_point_3 = np.cross(np.array([np.deg2rad(roll_speed), 0, 0]), radius_3)
    actuator_3 = roll_platform.platform_point_3_reference_frame - roll_platform.ground_point_3_reference_frame
    v_actuator_3 = np.dot(actuator_3/np.linalg.norm(actuator_3), v_point_3)
    return v_actuator_3


for time in np.arange(time_start, time_end, dt):
    time_values.append(time)


actuator_0_speed_old = 0
actuator_1_speed_old = 0
actuator_2_speed_old = 0
actuator_3_speed_old = 0

for t in time_values:
    roll_platform.build_system()
    roll_platform.move_system()

    actuator_0_speed = calculate_v_actuator_0_roll()
    actuator_0_speed_values.append(actuator_0_speed)
    actuator_0_length = actuator_0_length + (actuator_0_speed * dt)
    actuator_0_length_values.append(actuator_0_length)
    actuator_0_acceleration = (actuator_0_speed - actuator_0_speed_old) / dt
    actuator_0_accelration_values.append(actuator_0_acceleration)
    actuator_0_speed_old = actuator_0_speed

    actuator_1_speed = calculate_v_actuator_1_roll()
    actuator_1_speed_values.append(actuator_1_speed)
    actuator_1_length = actuator_1_length + (actuator_1_speed * dt)
    actuator_1_length_values.append(actuator_1_length)
    actuator_1_acceleration = (actuator_1_speed - actuator_1_speed_old) / dt
    actuator_1_accelration_values.append(actuator_1_acceleration)
    actuator_1_speed_old = actuator_1_speed

    actuator_2_speed = calculate_v_actuator_2_roll()
    actuator_2_speed_values.append(actuator_2_speed)
    actuator_2_length = actuator_2_length + (actuator_2_speed * dt)
    actuator_2_length_values.append(actuator_2_length)
    actuator_2_acceleration = (actuator_2_speed - actuator_2_speed_old) / dt
    actuator_2_accelration_values.append(actuator_2_acceleration)
    actuator_2_speed_old = actuator_2_speed

    actuator_3_speed = calculate_v_actuator_3_roll()
    actuator_3_speed_values.append(actuator_3_speed)
    actuator_3_length = actuator_3_length + (actuator_3_speed * dt)
    actuator_3_length_values.append(actuator_3_length)
    actuator_3_acceleration = (actuator_3_speed - actuator_3_speed_old) / dt
    actuator_3_accelration_values.append(actuator_3_acceleration)
    actuator_3_speed_old = actuator_3_speed



    roll_values.append(roll_platform.roll)

    roll_platform.roll = roll_platform.roll + (roll_speed * dt)


fig1, ((ax0, ax1, ax2, ax3), (ax4, ax5, ax6, ax7),(ax8, ax9, ax10, ax11)) = plt.subplots(3, 4)
fig1.tight_layout(pad=0.01)

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


ax0.plot(roll_values, actuator_0_length_values, label='A0')
ax0.set_xlabel('roll (deg)')
ax0.set_ylabel('length (m)')
ax0.legend()

ax1.plot(roll_values, actuator_1_length_values, label='A1')
ax1.set_xlabel('roll (deg)')
ax1.set_ylabel('length (m)')
ax1.legend()

ax2.plot(roll_values, actuator_2_length_values, label='A2')
ax2.set_xlabel('roll (deg)')
ax2.set_ylabel('length (m)')
ax2.legend()

ax3.plot(roll_values, actuator_3_length_values, label='A3')
ax3.set_xlabel('roll (deg)')
ax3.set_ylabel('length (m)')
ax3.legend()

ax4.plot(roll_values, actuator_0_speed_values, label='A0')
ax4.set_xlabel('roll (deg)')
ax4.set_ylabel('speed (m/s)')
ax4.legend()

ax5.plot(roll_values, actuator_1_speed_values, label='A1')
ax5.set_xlabel('roll (deg)')
ax5.set_ylabel('speed (m/s)')
ax5.legend()

ax6.plot(roll_values, actuator_2_speed_values, label='A2')
ax6.set_xlabel('roll (deg)')
ax6.set_ylabel('speed (m/s)')
ax6.legend()

ax7.plot(roll_values, actuator_3_speed_values, label='A3')
ax7.set_xlabel('roll (deg)')
ax7.set_ylabel('speed (m/s)')
ax7.legend()

ax8.plot(roll_values[1:], actuator_0_accelration_values[1:], label='A0')
ax8.set_xlabel('roll (deg)')
ax8.set_ylabel('acceleration (m/s^2)')
ax8.legend()

ax9.plot(roll_values[1:], actuator_1_accelration_values[1:], label='A1')
ax9.set_xlabel('roll (deg)')
ax9.set_ylabel('acceleration (m/s^2)')
ax9.legend()

ax10.plot(roll_values[1:], actuator_2_accelration_values[1:], label='A2')
ax10.set_xlabel('roll (deg)')
ax10.set_ylabel('acceleration (m/s^2)')
ax10.legend()

ax11.plot(roll_values[1:], actuator_3_accelration_values[1:], label='A3')
ax11.set_xlabel('roll (deg)')
ax11.set_ylabel('acceleration (m/s^2)')
ax11.legend()

plt.show()
