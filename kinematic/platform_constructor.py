import numpy as np
from numpy import sin, cos
from rigid_construction import construction_matrix


class Platform:

    def __init__(self,
                 ground_length, ground_width, ground_height,
                 motion_length, motion_width,
                 roll_yaw_x, roll_yaw_z, pitch_x, pitch_z,
                 roll, pitch, yaw, heave,
                 load_length, load_width, load_height, load_x, load_y, load_z, load_mass):
        self.ground_length = ground_length
        self.ground_width = ground_width
        self.ground_height = ground_height
        self.motion_length = motion_length
        self.motion_width = motion_width
        self.roll_yaw_x = roll_yaw_x
        self.roll_yaw_z = roll_yaw_z
        self.pitch_x = pitch_x
        self.pitch_z = pitch_z
        self.roll = roll
        self.pitch = pitch
        self.yaw = yaw
        self.heave = heave
        self.ground_point_0_reference_frame = []
        self.ground_point_1_reference_frame = []
        self.ground_point_2_reference_frame = []
        self.ground_point_3_reference_frame = []
        self.platform_point_0_motion_frame = []
        self.platform_point_1_motion_frame = []
        self.platform_point_2_motion_frame = []
        self.platform_point_3_motion_frame = []
        self.pitch_point_motion_frame = []
        self.roll_yaw_point_motion_frame = []
        self.gravity_point_motion_frame = []
        self.platform_point_0_reference_frame = np.array([])
        self.platform_point_1_reference_frame = np.array([])
        self.platform_point_2_reference_frame = np.array([])
        self.platform_point_3_reference_frame = np.array([])
        self.pitch_point_reference_frame = []
        self.roll_yaw_point_reference_frame = []
        self.gravity_point_reference_frame = []
        self.load_length = load_length
        self.load_width = load_width
        self.load_height = load_height
        self.load_x = load_x
        self.load_y = load_y
        self.load_z = load_z
        self.load_mass = load_mass

    def calculate_position(self, vector):
        new_vector = vector
        new_vector = np.dot(self.yaw_matrix(), new_vector)
        new_vector = self.compensate_vector_position(new_vector, self.yaw_matrix(), self.roll_yaw_point_motion_frame)
        new_vector = np.dot(self.roll_matrix(), new_vector)
        new_vector = self.compensate_vector_position(new_vector, self.roll_matrix(), self.roll_yaw_point_motion_frame)
        new_vector = np.dot(self.pitch_matrix(), new_vector)
        new_vector = self.compensate_vector_position(new_vector, self.pitch_matrix(), self.pitch_point_motion_frame)
        new_vector = self.add_heave(new_vector)
        return new_vector

    def compensate_vector_position(self, input_vector, compensation_rotation_matrix, rotation_point):
        rotated_point = np.dot(compensation_rotation_matrix, rotation_point)
        comp = (np.array([0, rotation_point[1] - rotated_point[1], rotation_point[2] - rotated_point[2]]))
        return np.add(input_vector, comp)

    def add_heave(self, vector):
        return np.add(vector, np.array([0, 0, self.heave]))

    def yaw_matrix(self):
        yaw = np.deg2rad(self.yaw)
        return np.array([
            [cos(yaw), -sin(yaw), 0],
            [sin(yaw), cos(yaw), 0],
            [0, 0, 1]
        ])

    def pitch_matrix(self):
        pitch = np.deg2rad(self.pitch)
        return np.array([
            [cos(pitch), 0, sin(pitch)],
            [0, 1, 0],
            [-sin(pitch), 0, cos(pitch)]
        ])

    def roll_matrix(self):
        roll = np.deg2rad(self.roll)
        return np.array([
            [1, 0, 0],
            [0, cos(roll), -sin(roll)],
            [0, sin(roll), cos(roll)],
        ])

    def build_system(self):
        self.ground_point_0_reference_frame = np.array([0, self.ground_width / 2, self.ground_height])
        self.ground_point_1_reference_frame = np.array([0, -self.ground_width / 2, self.ground_height])

        self.ground_point_2_reference_frame = np.array([self.ground_length, self.ground_width / 2,
                                                        self.ground_height])
        self.ground_point_3_reference_frame = np.array([self.ground_length, -self.ground_width / 2,
                                                        self.ground_height])

        self.platform_point_0_motion_frame = np.array([0, 0, 0])
        self.platform_point_1_motion_frame = np.array([0, 0, 0])

        self.platform_point_2_motion_frame = np.array([self.motion_length, self.motion_width / 2, 0])
        self.platform_point_3_motion_frame = np.array([self.motion_length, -self.motion_width / 2, 0])

        self.pitch_point_motion_frame = np.array([self.pitch_x, 0, self.pitch_z])
        self.roll_yaw_point_motion_frame = np.array([self.roll_yaw_x, 0, self.roll_yaw_z])

        self.gravity_point_motion_frame = np.array([self.motion_length / 2, self.load_y, self.load_z])

    def move_system(self):
        self.platform_point_0_reference_frame = self.calculate_position(self.platform_point_0_motion_frame)
        self.platform_point_1_reference_frame = self.calculate_position(self.platform_point_1_motion_frame)
        self.platform_point_2_reference_frame = self.calculate_position(self.platform_point_2_motion_frame)
        self.platform_point_3_reference_frame = self.calculate_position(self.platform_point_3_motion_frame)
        self.pitch_point_reference_frame = self.calculate_position(self.pitch_point_motion_frame)
        self.roll_yaw_point_reference_frame = self.calculate_position(self.roll_yaw_point_motion_frame)
        self.gravity_point_reference_frame = self.calculate_position(self.gravity_point_motion_frame)
        # print(self.platform_point_0_reference_frame, self.platform_point_1_reference_frame,
        #       self.platform_point_2_reference_frame, self.platform_point_3_reference_frame)

    def actuator_lengths(self):
        length_0 = np.linalg.norm(self.platform_point_0_reference_frame - self.ground_point_0_reference_frame)
        length_1 = np.linalg.norm(self.platform_point_1_reference_frame - self.ground_point_1_reference_frame)
        length_2 = np.linalg.norm(self.platform_point_2_reference_frame - self.ground_point_2_reference_frame)
        length_3 = np.linalg.norm(self.platform_point_3_reference_frame - self.ground_point_3_reference_frame)
        return length_0, length_1, length_2, length_3

    def actuator_speeds(self, rollspeed, pitchspeed, yawspeed, rotationpoint):
        radius_0 = self.platform_point_0_reference_frame - rotationpoint
        v_point_0 = np.cross(np.array([np.deg2rad(rollspeed), np.deg2rad(pitchspeed), np.deg2rad(yawspeed)]), radius_0)
        actuator_0 = self.platform_point_0_reference_frame - self.ground_point_0_reference_frame
        speed_0 = np.dot(actuator_0 / np.linalg.norm(actuator_0), v_point_0)

        radius_1 = self.platform_point_1_reference_frame - rotationpoint
        v_point_1 = np.cross(np.array([np.deg2rad(rollspeed), np.deg2rad(pitchspeed), np.deg2rad(yawspeed)]), radius_1)
        actuator_1 = self.platform_point_1_reference_frame - self.ground_point_1_reference_frame
        speed_1 = np.dot(actuator_1 / np.linalg.norm(actuator_1), v_point_1)

        radius_2 = self.platform_point_2_reference_frame - rotationpoint
        v_point_2 = np.cross(np.array([np.deg2rad(rollspeed), np.deg2rad(pitchspeed), np.deg2rad(yawspeed)]), radius_2)
        actuator_2 = self.platform_point_2_reference_frame - self.ground_point_2_reference_frame
        speed_2 = np.dot(actuator_2 / np.linalg.norm(actuator_2), v_point_2)

        radius_3 = self.platform_point_3_reference_frame - rotationpoint
        v_point_3 = np.cross(np.array([np.deg2rad(rollspeed), np.deg2rad(pitchspeed), np.deg2rad(yawspeed)]), radius_3)
        actuator_3 = self.platform_point_3_reference_frame - self.ground_point_3_reference_frame
        speed_3 = np.dot(actuator_3 / np.linalg.norm(actuator_3), v_point_3)

        return speed_0, speed_1, speed_2, speed_3

    def actuator_accelerations(self, rollacceleration, pitchacceleration, yawacceleration, rotationpoint):
        radius_0 = self.platform_point_0_reference_frame - rotationpoint
        a_point_0 = np.cross(np.array([np.deg2rad(rollacceleration),
                                       np.deg2rad(pitchacceleration),
                                       np.deg2rad(yawacceleration)]), radius_0)
        actuator_0 = self.platform_point_0_reference_frame - self.ground_point_0_reference_frame
        acceleration_0 = np.dot(actuator_0 / np.linalg.norm(actuator_0), a_point_0)

        radius_1 = self.platform_point_1_reference_frame - rotationpoint
        a_point_1 = np.cross(np.array([np.deg2rad(rollacceleration),
                                       np.deg2rad(pitchacceleration),
                                       np.deg2rad(yawacceleration)]), radius_1)
        actuator_1 = self.platform_point_1_reference_frame - self.ground_point_1_reference_frame
        acceleration_1 = np.dot(actuator_1 / np.linalg.norm(actuator_1), a_point_1)

        radius_2 = self.platform_point_2_reference_frame - rotationpoint
        a_point_2 = np.cross(np.array([np.deg2rad(rollacceleration),
                                       np.deg2rad(pitchacceleration),
                                       np.deg2rad(yawacceleration)]), radius_2)
        actuator_2 = self.platform_point_2_reference_frame - self.ground_point_2_reference_frame
        acceleration_2 = np.dot(actuator_2 / np.linalg.norm(actuator_2), a_point_2)

        radius_3 = self.platform_point_3_reference_frame - rotationpoint
        a_point_3 = np.cross(np.array([np.deg2rad(rollacceleration),
                                       np.deg2rad(pitchacceleration),
                                       np.deg2rad(yawacceleration)]), radius_3)
        actuator_3 = self.platform_point_3_reference_frame - self.ground_point_3_reference_frame
        acceleration_3 = np.dot(actuator_3 / np.linalg.norm(actuator_3), a_point_3)

        return acceleration_0, acceleration_1, acceleration_2, acceleration_3

    def actuator_forces(self):
        a = construction_matrix(self.ground_point_0_reference_frame, self.ground_point_1_reference_frame,
                                self.ground_point_2_reference_frame, self.ground_point_3_reference_frame,
                                self.platform_point_0_reference_frame, self.gravity_point_reference_frame,
                                self.platform_point_2_reference_frame, self.platform_point_3_reference_frame,
                                self.roll_yaw_point_reference_frame)
        fz = self.load_mass * -9.81
        f = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, fz, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        x = np.dot(np.linalg.inv(a), f)
        return x[0], x[1], x[2], x[3]

    def roll_platform_limits(self, rollmin, rollmax, rollspeed, rollacceleration, resolution):
        roll_values = []
        length_0_values = []
        length_1_values = []
        length_2_values = []
        length_3_values = []
        speed_0_values = []
        speed_1_values = []
        speed_2_values = []
        speed_3_values = []
        acceleration_0_values = []
        acceleration_1_values = []
        acceleration_2_values = []
        acceleration_3_values = []
        force_0_values = []
        force_1_values = []
        force_2_values = []
        force_3_values = []

        for roll in np.arange(rollmin, rollmax, resolution):
            self.roll = roll
            self.build_system()
            self.move_system()
            roll_values.append(roll)

            length_0, length_1, length_2, length_3 = self.actuator_lengths()
            length_0_values.append(length_0)
            length_1_values.append(length_1)
            length_2_values.append(length_2)
            length_3_values.append(length_3)

            speed_0, speed_1, speed_2, speed_3 = self.actuator_speeds(rollspeed, 0, 0,
                                                                      self.roll_yaw_point_reference_frame)
            speed_0_values.append(speed_0)
            speed_1_values.append(speed_1)
            speed_2_values.append(speed_2)
            speed_3_values.append(speed_3)

            (acceleration_0, acceleration_1,
             acceleration_2, acceleration_3) = self.actuator_accelerations(rollacceleration, 0, 0,
                                                                           self.roll_yaw_point_reference_frame)
            acceleration_0_values.append(acceleration_0)
            acceleration_1_values.append(acceleration_1)
            acceleration_2_values.append(acceleration_2)
            acceleration_3_values.append(acceleration_3)

            force_0, force_1, force_2, force_3 = self.actuator_forces()
            force_0_values.append(force_0)
            force_1_values.append(force_1)
            force_2_values.append(force_2)
            force_3_values.append(force_3)

        return (roll_values,
                length_0_values, length_1_values, length_2_values, length_3_values,
                speed_0_values, speed_1_values, speed_2_values, speed_3_values,
                acceleration_0_values, acceleration_1_values, acceleration_2_values, acceleration_3_values,
                force_0_values, force_1_values, force_2_values, force_3_values)

    def pitch_platform_limits(self, pitchmin, pitchmax, pitchspeed, pitchacceleration, resolution):
        pitch_values = []
        length_0_values = []
        length_1_values = []
        length_2_values = []
        length_3_values = []
        speed_0_values = []
        speed_1_values = []
        speed_2_values = []
        speed_3_values = []
        acceleration_0_values = []
        acceleration_1_values = []
        acceleration_2_values = []
        acceleration_3_values = []
        force_0_values = []
        force_1_values = []
        force_2_values = []
        force_3_values = []

        for pitch in np.arange(pitchmin, pitchmax, resolution):
            self.pitch = pitch
            self.build_system()
            self.move_system()
            pitch_values.append(pitch)

            length_0, length_1, length_2, length_3 = self.actuator_lengths()
            length_0_values.append(length_0)
            length_1_values.append(length_1)
            length_2_values.append(length_2)
            length_3_values.append(length_3)

            speed_0, speed_1, speed_2, speed_3 = self.actuator_speeds(0, pitchspeed, 0,
                                                                      self.pitch_point_reference_frame)
            speed_0_values.append(speed_0)
            speed_1_values.append(speed_1)
            speed_2_values.append(speed_2)
            speed_3_values.append(speed_3)

            (acceleration_0, acceleration_1,
             acceleration_2, acceleration_3) = self.actuator_accelerations(0, pitchacceleration, 0,
                                                                           self.pitch_point_reference_frame)
            acceleration_0_values.append(acceleration_0)
            acceleration_1_values.append(acceleration_1)
            acceleration_2_values.append(acceleration_2)
            acceleration_3_values.append(acceleration_3)

            force_0, force_1, force_2, force_3 = self.actuator_forces()
            force_0_values.append(force_0)
            force_1_values.append(force_1)
            force_2_values.append(force_2)
            force_3_values.append(force_3)

        return (pitch_values,
                length_0_values, length_1_values, length_2_values, length_3_values,
                speed_0_values, speed_1_values, speed_2_values, speed_3_values,
                acceleration_0_values, acceleration_1_values, acceleration_2_values, acceleration_3_values,
                force_0_values, force_1_values, force_2_values, force_3_values)

    def yaw_platform_limits(self, yawmin, yawmax, yawspeed, yawacceleration, resolution):
        yaw_values = []
        length_0_values = []
        length_1_values = []
        length_2_values = []
        length_3_values = []
        speed_0_values = []
        speed_1_values = []
        speed_2_values = []
        speed_3_values = []
        acceleration_0_values = []
        acceleration_1_values = []
        acceleration_2_values = []
        acceleration_3_values = []
        force_0_values = []
        force_1_values = []
        force_2_values = []
        force_3_values = []

        for yaw in np.arange(yawmin, yawmax, resolution):
            self.yaw = yaw
            self.build_system()
            self.move_system()
            yaw_values.append(yaw)

            length_0, length_1, length_2, length_3 = self.actuator_lengths()
            length_0_values.append(length_0)
            length_1_values.append(length_1)
            length_2_values.append(length_2)
            length_3_values.append(length_3)

            speed_0, speed_1, speed_2, speed_3 = self.actuator_speeds(0, 0, yawspeed,
                                                                      self.roll_yaw_point_reference_frame)
            speed_0_values.append(speed_0)
            speed_1_values.append(speed_1)
            speed_2_values.append(speed_2)
            speed_3_values.append(speed_3)

            (acceleration_0, acceleration_1,
             acceleration_2, acceleration_3) = self.actuator_accelerations(0, 0, yawacceleration,
                                                                           self.roll_yaw_point_reference_frame)
            acceleration_0_values.append(acceleration_0)
            acceleration_1_values.append(acceleration_1)
            acceleration_2_values.append(acceleration_2)
            acceleration_3_values.append(acceleration_3)

            force_0, force_1, force_2, force_3 = self.actuator_forces()
            force_0_values.append(force_0)
            force_1_values.append(force_1)
            force_2_values.append(force_2)
            force_3_values.append(force_3)

        return (yaw_values,
                length_0_values, length_1_values, length_2_values, length_3_values,
                speed_0_values, speed_1_values, speed_2_values, speed_3_values,
                acceleration_0_values, acceleration_1_values, acceleration_2_values, acceleration_3_values,
                force_0_values, force_1_values, force_2_values, force_3_values)

    def linear_actuator_speeds(self, x_speed, y_speed, z_speed):
        speed_vector = np.array([x_speed, y_speed, z_speed])

        actuator_0 = self.platform_point_0_reference_frame - self.ground_point_0_reference_frame
        speed_0 = np.dot(actuator_0 / np.linalg.norm(actuator_0), speed_vector)

        actuator_1 = self.platform_point_1_reference_frame - self.ground_point_1_reference_frame
        speed_1 = np.dot(actuator_1 / np.linalg.norm(actuator_1), speed_vector)

        actuator_2 = self.platform_point_2_reference_frame - self.ground_point_2_reference_frame
        speed_2 = np.dot(actuator_2 / np.linalg.norm(actuator_2), speed_vector)

        actuator_3 = self.platform_point_3_reference_frame - self.ground_point_3_reference_frame
        speed_3 = np.dot(actuator_3 / np.linalg.norm(actuator_3), speed_vector)

        return speed_0, speed_1, speed_2, speed_3

    def linear_actuator_accelerations(self, x_acceleration, y_acceleration, z_acceleration):
        acceleration_vector = np.array([x_acceleration, y_acceleration, z_acceleration])

        actuator_0 = self.platform_point_0_reference_frame - self.ground_point_0_reference_frame
        acceleration_0 = np.dot(actuator_0 / np.linalg.norm(actuator_0), acceleration_vector)

        actuator_1 = self.platform_point_1_reference_frame - self.ground_point_1_reference_frame
        acceleration_1 = np.dot(actuator_1 / np.linalg.norm(actuator_1), acceleration_vector)

        actuator_2 = self.platform_point_2_reference_frame - self.ground_point_2_reference_frame
        acceleration_2 = np.dot(actuator_2 / np.linalg.norm(actuator_2), acceleration_vector)

        actuator_3 = self.platform_point_3_reference_frame - self.ground_point_3_reference_frame
        acceleration_3 = np.dot(actuator_3 / np.linalg.norm(actuator_3), acceleration_vector)

        return acceleration_0, acceleration_1, acceleration_2, acceleration_3

    def heave_platform_limits(self, heavemin, heavemax, heavespeed, heaveacceleration, resolution):
        heave_values = []
        length_0_values = []
        length_1_values = []
        length_2_values = []
        length_3_values = []
        speed_0_values = []
        speed_1_values = []
        speed_2_values = []
        speed_3_values = []
        acceleration_0_values = []
        acceleration_1_values = []
        acceleration_2_values = []
        acceleration_3_values = []
        force_0_values = []
        force_1_values = []
        force_2_values = []
        force_3_values = []

        for heave in np.arange(heavemin, heavemax, resolution):
            self.heave = heave
            self.build_system()
            self.move_system()
            heave_values.append(heave)

            length_0, length_1, length_2, length_3 = self.actuator_lengths()
            length_0_values.append(length_0)
            length_1_values.append(length_1)
            length_2_values.append(length_2)
            length_3_values.append(length_3)

            speed_0, speed_1, speed_2, speed_3 = self.linear_actuator_speeds(0, 0, heavespeed)
            speed_0_values.append(speed_0)
            speed_1_values.append(speed_1)
            speed_2_values.append(speed_2)
            speed_3_values.append(speed_3)

            (acceleration_0, acceleration_1,
             acceleration_2, acceleration_3) = self.linear_actuator_accelerations(0, 0, heaveacceleration)
            acceleration_0_values.append(acceleration_0)
            acceleration_1_values.append(acceleration_1)
            acceleration_2_values.append(acceleration_2)
            acceleration_3_values.append(acceleration_3)

            force_0, force_1, force_2, force_3 = self.actuator_forces()
            force_0_values.append(force_0)
            force_1_values.append(force_1)
            force_2_values.append(force_2)
            force_3_values.append(force_3)

        return (heave_values,
                length_0_values, length_1_values, length_2_values, length_3_values,
                speed_0_values, speed_1_values, speed_2_values, speed_3_values,
                acceleration_0_values, acceleration_1_values, acceleration_2_values, acceleration_3_values,
                force_0_values, force_1_values, force_2_values, force_3_values)


class Example(Platform):
    def __init__(self):
        self.ground_length = 1  # 1
        self.ground_width = 1.2
        self.ground_height = 0  # 0
        self.motion_length = 1  # 1
        self.motion_width = 1
        self.roll_yaw_x = 0.7
        self.roll_yaw_z = -0.2  # 0.3
        self.pitch_x = 0.5
        self.pitch_z = 0.2
        self.roll = 0
        self.pitch = 0
        self.yaw = 0
        self.heave = 0.9
        self.ground_point_0_reference_frame = []
        self.ground_point_1_reference_frame = []
        self.ground_point_2_reference_frame = []
        self.ground_point_3_reference_frame = []
        self.platform_point_0_motion_frame = []
        self.platform_point_1_motion_frame = []
        self.platform_point_2_motion_frame = []
        self.platform_point_3_motion_frame = []
        self.pitch_point_motion_frame = []
        self.roll_yaw_point_motion_frame = []
        self.gravity_point_motion_frame = []
        self.platform_point_0_reference_frame = []
        self.platform_point_1_reference_frame = []
        self.platform_point_2_reference_frame = []
        self.platform_point_3_reference_frame = []
        self.pitch_point_reference_frame = []
        self.roll_yaw_point_reference_frame = []
        self.gravity_point_reference_frame = []
        self.load_length = 1
        self.load_width = 1
        self.load_height = 1
        self.load_x = 0.5
        self.load_y = 0
        self.load_z = -0.1
        self.load_mass = 200
