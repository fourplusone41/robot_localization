# Copyright 2018 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from launch import LaunchDescription
import launch_ros.actions
import os
import yaml
from launch.substitutions import EnvironmentVariable
import pathlib
import launch.actions
from launch.actions import DeclareLaunchArgument

def generate_launch_description():
    parameters_file_dir = pathlib.Path(__file__).resolve().parent
    parameters_file_path = parameters_file_dir /'test_ekf_localization_node_bag2.yaml'    
    os.environ['FILE_PATH'] = str(parameters_file_dir)
    return LaunchDescription([
        launch.actions.DeclareLaunchArgument(
            'output_final_position',
            default_value='false'),
        launch.actions.DeclareLaunchArgument(
            'output_location',
	    default_value='ekf3.txt'),	

	 #*****test_ekf_localization_node_bag3.test***** 
	launch_ros.actions.Node(
            package='robot_localization', node_executable='se_node', node_name='test_ekf_localization_node_bag3_ekf',
	    output='screen',
	    parameters=[
                parameters_file_path,
                str(parameters_file_path),
                [EnvironmentVariable(name='FILE_PATH'), os.sep, 'test_ekf_localization_node_bag3.yaml'],
           ],
           ),
        launch_ros.actions.Node(
            package='robot_localization', node_executable='test_ekf_localization_node_bag3', node_name='test_ekf_localization_node_bag3_pose',
            output='screen',
	parameters=[
                parameters_file_path,
                str(parameters_file_path),
                [EnvironmentVariable(name='FILE_PATH'), os.sep, 'test_ekf_localization_node_bag3.yaml'],
        ],
	),
])













