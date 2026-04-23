import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

class Patrol(Node):
    def __init__(self):
        super().__init__('patrol_node')
        self.pub = self.create_publisher(Twist, '/cmd_vel', 10)

    def move(self, linear=0.0, angular=0.0, duration=1.0):
        msg = Twist()
        msg.linear.x = linear
        msg.angular.z = angular

        end_time = time.time() + duration
        while time.time() < end_time:
            self.pub.publish(msg)
            time.sleep(0.1)

        # stop
        msg.linear.x = 0.0
        msg.angular.z = 0.0
        self.pub.publish(msg)

def main():
    rclpy.init()
    node = Patrol()

    try:
        while True:
            # Move forward (hallway)
            node.move(linear=0.3, duration=4)

            # Turn left (enter room)
            node.move(angular=0.5, duration=2)

            # Move inside room
            node.move(linear=0.3, duration=3)

            # Turn right
            node.move(angular=-0.5, duration=2)

            # Continue patrol
            node.move(linear=0.3, duration=4)

    except KeyboardInterrupt:
        pass

    rclpy.shutdown()

if __name__ == '__main__':
    main()
