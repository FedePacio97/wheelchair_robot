import subprocess
import rospy
import os
from os import path

port = "11311"
# Running on another shell
subprocess.Popen(["roscore", "-p", port])

print("Roscore launched!")

# Launch the simulation with the given launchfile name
# Aanonymous=True adds a random number (to ensure unicity) to the name of the node
rospy.init_node("simul", anonymous=True)

fullpath = os.path.join(os.path.dirname(__file__), "main.launch")
if not path.exists(fullpath):
    raise IOError("File " + fullpath + " does not exist")

subprocess.Popen(["roslaunch", "-p", port, fullpath])
print("Gazebo launched!")