import rclpy
from rclpy.node import Node
from builtin_interfaces.msg import Duration
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from pynput import keyboard as kb


class Trajectory_publisher(Node):

    def __init__(self):
        super().__init__('trajectory_publsiher_node')
        publish_topic = "/joint_trajectory_controller/joint_trajectory"
        self.trajectory_publihser = self.create_publisher(JointTrajectory, publish_topic, 10)
        timer_period = 1
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.joints = ['joint_1', 'joint_2', 'joint_3', 'joint_4', 'joint_5', 'joint_6']
        self.goal_positions = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        self.step_size = 0.1

    def on_press(self, key):
        key_char = key.char
        print(str(key_char))
        if key_char == 'a':
            self.goal_positions[0] += self.step_size
        elif key_char == 's':
            self.goal_positions[0] -= self.step_size
        elif key_char == 'd':
            self.goal_positions[1] += self.step_size
        elif key_char == 'f':
            self.goal_positions[1] -= self.step_size
        elif key_char == 'g':
            self.goal_positions[2] += self.step_size
        elif key_char == 'h':
            self.goal_positions[2] -= self.step_size
        elif key_char == 'z':
            self.goal_positions[3] += self.step_size
        elif key_char == 'x':
            self.goal_positions[3] -= self.step_size   
        elif key_char == 'c':
            self.goal_positions[4] += self.step_size
        elif key_char == 'v':
            self.goal_positions[4] -= self.step_size
        elif key_char == 'b':
            self.goal_positions[5] += self.step_size
        elif key_char == 'n':
            self.goal_positions[5] -= self.step_size     

    def timer_callback(self):
        bazu_trajectory_msg = JointTrajectory()
        bazu_trajectory_msg.joint_names = self.joints
        # Create point with updated positions
        point = JointTrajectoryPoint()
        point.positions = self.goal_positions
        point.time_from_start = Duration(sec=2)
        # Add point to trajectory message
        bazu_trajectory_msg.points.append(point)
        self.trajectory_publihser.publish(bazu_trajectory_msg)

    def start_keyboard_listener(self):
        # Start keyboard listener in a new thread
        listener = kb.Listener(on_press=self.on_press)
        listener.start()

def main(args=None):
    rclpy.init(args=args)
    joint_trajectory_object = Trajectory_publisher()
    joint_trajectory_object.start_keyboard_listener()

    rclpy.spin(joint_trajectory_object)
    joint_trajectory_object.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
