# Robot Gazebo Simulation
Upgrade URDF in previous assignment to introduce the robot model to Gazebo simulation. Example repository: [linzhanguca/homeplater](https://github.com/linzhangUCA/homeplater.git) 

## Instructions: 
1. (20%) Set up the package.
```bash
cd <your ros workspace>/src
git clone git@github.com:UCAEngineeringPhysics/a3-robot_simulation-<your github username>.git
cd ..
colcon build --packages-select diffbot_gazebo
```
2. (80%) Create your robot's model by modifying the description file: `diffbot_gazebo/urdf/diffbot.urdf.xacro`. You can start from the URDF that were created in the previous assignment.
3. Include physical properties (`<collision>` and `<inertial>`) for all the links. 
4. Use `<gazebo reference>` tag to mark the links that need additional properties in Gazebo.
5. Use [`gazebo_diff_drive`](https://github.com/ros-simulation/gazebo_ros_pkgs/wiki/ROS-2-Migration:-Diff-drive) plugin, so that your robot can be controlled by `cmd_vel` topic (using `geometry_msgs/Twist` messages).

#### Hint:
After the first time you build the package, don't forget to source the overlay (your package) by `source <your ros workspace>/install/local_setup.bash`. You can automatically source it whenever you open a new terminal by adding the command to `~/.bashrc` (**only need to do this once**). `echo "source <your ros workspace>/install/local_setup.bash" >> ~/.bashrc` will get the job done. You'll replace <your ros workspace> with your actual ROS workspace name.
