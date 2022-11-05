import rclpy
from rclpy.node import Node
from person_msgs.msg import Person

def cb(msg):
    node.get_logger().info("Listen: %s" % msg)

rclpy.init()
node = Node("listener")
sub = node.create_subscription(Person, "person", cb, 10)
rclpy.spin(node)
