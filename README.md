# Robot Gazebo Simulation
Upgrade URDF in previous assignment to introduce the robot model to Gazebo simulation. 

## Instructions: 
1. (10%) Set up the package.
```bash
cd <your ros workspace>/src
git clone git@github.com:UCAEngineeringPhysics/a3-robot_simulation-<your github username>.git
cd ..
colcon build --packages-select diffbot_gazebo
```
2. (10%) Create your robot's model by modifying the description file: `diffbot_gazebo/urdf/diffbot.urdf.xacro`. You can start from the URDF that were created in the previous assignment.
3. (30%) Include physical properties (`<collision>` and `<inertial>`) for all the links. 
4. (20%) Use `<gazebo reference>` tag to mark the links that need additional properties in Gazebo.
5. (30%) Add [`gazebo_diff_drive`](https://github.com/ros-simulation/gazebo_ros_pkgs/wiki/ROS-2-Migration:-Diff-drive) plugin to your URDF, so that your robot can be controlled by `/cmd_vel` topic (using `geometry_msgs/Twist` messages) in Gazebo.

#### Hint:
- Example repository: [linzhanguca/homeplater](https://github.com/linzhangUCA/homeplater.git).
- To drive the robot in Gazebo, you can fire up `teleop_twist_keboard` to do so.
```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```
