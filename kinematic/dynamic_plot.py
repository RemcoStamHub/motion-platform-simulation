import numpy as np
import matplotlib.pyplot as plt
from platform_constructor import Platform, Example

step = 0.1

roll_range = 30             # +- value deg
roll_speed = 50             # +- value deg/s
roll_acceleration = 250     # +- value deg/s^2

# pitch_range = 30  # +- value degrees
# yaw_range = 30  # +- value degrees
# heave_range = 0.2  # +- value meters
#
# pitch_speed = 20  # +- value degrees/s
# yaw_speed = 20  # +- value degrees/s
# heave_speed = 2  # +- value meter/s

roll_platform = Example()

roll_values, length_0_values, length_1_values, length_2_values, length_3_values, speed_0_values, speed_1_values, speed_2_values, speed_3_values, acceleration_0_values, acceleration_1_values, acceleration_2_values, acceleration_3_values = roll_platform.roll_platform_limits(-roll_range,roll_range,roll_speed,roll_acceleration,0.1)

fig1, ((ax0, ax1, ax2, ax3), (ax4, ax5, ax6, ax7), (ax8, ax9, ax10, ax11)) = plt.subplots(3, 4)
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

plt.show()
