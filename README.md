This is an adaptation of joshnewans/my_bot (uses amend that is the building tool for ROS2), suing cmake (ROS1)
Important to know: 
 -) ROS Transform System (TF): https://www.youtube.com/watch?v=QyvHhY4Y_Y8
To build the package:
    In catkin_ws, execute "catkin_make_isolated"
    
To launch the robot:
    !! Always source /home/fede/DRL-obstacle-avoidance/catkin_ws/
    devel_isolated/setup.bash
    python3 src/wheelchair_robot/launch/robot.gazebo.launch.py

N.B: when adding new files, always "catkin_make_isolated"
Useful info about ROS:
    roscore: -> to start the master node
    rospack: find and retrieve information about packages (list)
    killall -9 rosout roslaunch rosmaster gzserver nodelet robot_state_publisher gzclient python python3 -> to kill nodes belonging to ros

How URDF works:

![alt text](img/URDF_process.png "URDF process")

The URDF files are parsed and compacted into a single file by xacro program. The result is given as input to another program called "robot_state_publisher" which let the URDF file be visible on the topic /robot_description so as the joint transform on the /tf topic. 
The robot_state_publisher expects input of movable joints on /joint_states topic.
For testing purpose, we can fake the movement by changing the joint using the "joint_state_publisher_gui"

For submodules:
https://git-scm.com/book/en/v2/Git-Tools-Submodules