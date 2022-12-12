import numpy as np
from numpy import sin, cos


class Platform:

    def __init__(self, ground_length, ground_width, ground_height, motion_length, motion_width, roll_yaw_x, roll_yaw_z,
                 pitch_x, pitch_z, roll, pitch, yaw, heave):
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
        self.platform_point_0_reference_frame = []
        self.platform_point_1_reference_frame = []
        self.platform_point_2_reference_frame = []
        self.platform_point_3_reference_frame = []
        self.pitch_point_reference_frame = []
        self.roll_yaw_point_reference_frame = []

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

    def move_system(self):
        self.platform_point_0_reference_frame = self.calculate_position(self.platform_point_0_motion_frame)
        self.platform_point_1_reference_frame = self.calculate_position(self.platform_point_1_motion_frame)
        self.platform_point_2_reference_frame = self.calculate_position(self.platform_point_2_motion_frame)
        self.platform_point_3_reference_frame = self.calculate_position(self.platform_point_3_motion_frame)
        self.pitch_point_reference_frame = self.calculate_position(self.pitch_point_motion_frame)
        self.roll_yaw_point_reference_frame = self.calculate_position(self.roll_yaw_point_motion_frame)


class Example(Platform):
    def __init__(self):
        self.ground_length = 1
        self.ground_width = 1
        self.ground_height = 2
        self.motion_length = 1
        self.motion_width = 0.7
        self.roll_yaw_x = 0.5
        self.roll_yaw_z = 0.3     # 0.3
        self.pitch_x = 0.5
        self.pitch_z = 0
        self.roll = 0
        self.pitch = 0
        self.yaw = 0
        self.heave = 1
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
        self.platform_point_0_reference_frame = []
        self.platform_point_1_reference_frame = []
        self.platform_point_2_reference_frame = []
        self.platform_point_3_reference_frame = []
        self.pitch_point_reference_frame = []
        self.roll_yaw_point_reference_frame = []
