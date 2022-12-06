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

actuator_length = 3.433
actuator_0_values = []
actuator_0_movement = []

actuator_1_values = []
actuator_2_values = []
actuator_3_values = []

roll_values = []
time_values = []

dt = 0.01
time_start = 0
time_end = 2 * (roll_range / roll_speed)

new_platform.roll = - roll_range
new_platform.build_system()
new_platform.move_system()


def calculate_v_actuator_roll():
    # radius_0 = np.subtract(np.array([0,
    #                                  new_platform.platform_point_0_reference_frame[1],
    #                                  new_platform.platform_point_0_reference_frame[2]]),
    #                        np.array([0,
    #                                  0,
    #                                  new_platform.roll_yaw_point_reference_frame[2]]))
    radius_0 = new_platform.platform_point_0_reference_frame - new_platform.roll_yaw_point_reference_frame
    v_point_0 = np.cross(np.array([np.deg2rad(roll_speed), 0, 0]), radius_0)
    # print(v_point_0)
    actuator_0 = new_platform.platform_point_0_reference_frame-new_platform.ground_point_0_reference_frame
    v_actuator_0 = np.dot(actuator_0/np.linalg.norm(actuator_0), v_point_0)
    print(v_actuator_0)
    return v_actuator_0


for time in np.arange(time_start, time_end, dt):
    new_platform.build_system()
    new_platform.move_system()
    v_0 = calculate_v_actuator_roll()
    actuator_0_values.append(v_0)
    time_values.append(time)
    actuator_length = actuator_length + (v_0 * dt)
    actuator_0_movement.append(actuator_length)
    roll_values.append(new_platform.roll)
    new_platform.roll = new_platform.roll + (roll_speed * dt)

fig = plt.figure()
ax = fig.add_subplot()
ax.scatter(roll_values, actuator_0_movement)
plt.show()
