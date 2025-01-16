from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([

        Node(
            package='traversability_gridmap',
            executable='traversability_node',
            name='traversability_node',
            output ='screen',
            parameters=[
                {"pc_topic": "/pcd_topic"},
            	{"resolution": 0.2},
                {"half_size": 75.},
                {"security_distance": 0.15},
                {"max_slope": 0.6}, 
                {"ground_clearance": 0.15}, 
                {"robot_height": 1.5}, #above lidar
                {"robot_width":0.8},
                {"robot_length":1.1},
                {"draw_isodistance_each": 1.},
                {"frame_id":"world"},
                {"global_mapping":True},

            ],
        )
    ])
